import json
import os
import pandas as pd
from typing import List, Dict, Any, Optional
from agno.agent import Agent
from agno.models.groq import Groq
from storage.structured_store import engine
from sqlalchemy import text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ComparisonAgent:
    def __init__(self):
        # The Agno Groq model expects GROQ_API_KEY
        # If your .env has GROK_API_KEY, we map it here
        if not os.getenv("GROQ_API_KEY") and os.getenv("GROK_API_KEY"):
            os.environ["GROQ_API_KEY"] = os.getenv("GROK_API_KEY")
            
        self.model_id = os.getenv("GROK_MODEL", "llama-3.3-70b-versatile")
        self.agent = Agent(
            name="Comparison_Agent",
            model=Groq(id=self.model_id),
            instructions=[
                "You are a senior equity research analyst comparing multiple companies.",
                "CRITICAL: YOUR ENTIRE RESPONSE MUST BE A SINGLE VALID JSON OBJECT.",
                "DO NOT INCLUDE ANY INTRODUCTORY TEXT, HEADERS, OR MARKDOWN BULLETS OUTSIDE THE JSON.",
                "You will receive structured financial data (Quarterly and Annual) for each company.",
                "Your task: produce a detailed comparison across these dimensions:",
                "  - Growth (revenue, net income, cash flow trends)",
                "  - Profitability (margins, ROCE, ROE)",
                "  - Financial leverage (debt/equity, interest coverage)",
                "  - Operational efficiency (inventory days, debtor days)",
                "  - Risk (one-time gains, legal issues, management tone)",
                "",
                "IMPORTANT: Compare Quarterly shifts (short-term) against Yearly trends (long-term).",
                "If data for a company is missing, mark its scores as 0 and state 'Data missing' in strengths.",
                "Output structure MUST be a single valid JSON object exactly like this:",
                "{",
                '  "overall_ranking": ["TICKER1", "TICKER2", ...],',
                '  "side_by_side_metrics": [',
                '    {"metric": "Sales (Q)", "TICKER1": "val", "TICKER2": "val", "comparison": "TICKER1 is higher by X%"},',
                '    {"metric": "Net Profit (Y)", "TICKER1": "val", "TICKER2": "val", "comparison": "..."},',
                '    ...',
                '  ],',
                '  "dimension_scores": {',
                '    "growth": {"TICKER1": score, "TICKER2": score, ...},',
                '    ...',
                '  },',
                '  "strengths_weaknesses": {',
                '    "TICKER1": {"strengths": ["...", "..."], "weaknesses": ["...", "..."]},',
                '    ...',
                '  },',
                '  "recommendation": "Best pick: TICKER1 because ...",',
                '  "summary_period_analysis": "Context on Q vs Y performance..."',
                "}",
                "DO NOT USE MARKDOWN CODE BLOCKS. START THE RESPONSE WITH { AND END WITH }."
            ],
            markdown=False
        )

    async def get_comparison(self, tickers: List[str], metrics_list: List[str], period: str = "both") -> Dict[str, Any]:
        data_context = ""
        
        for ticker in tickers:
            data_context += f"### DATA FOR {ticker} ###\n"
            
            # 1. Fetch Quarterly Data (From financials_quarterly)
            q_sql = text("""
                SELECT quarter as period, metric_name, metric_value, unit 
                FROM financials_quarterly 
                WHERE company_name = :ticker 
                AND metric_name IN :metrics
                ORDER BY created_at DESC, quarter DESC
                LIMIT 40
            """)
            
            # 2. Fetch Yearly Data (Fallback logic)
            # First try financials_yearly, if it fails, fallback to Mar entries in financials_quarterly
            y_sql_primary = text("""
                SELECT year as period, metric_name, metric_value, unit 
                FROM financials_yearly 
                WHERE company_name = :ticker 
                AND metric_name IN :metrics
                ORDER BY year DESC
                LIMIT 20
            """)
            
            y_sql_fallback = text("""
                SELECT quarter as period, metric_name, metric_value, unit 
                FROM financials_quarterly 
                WHERE company_name = :ticker 
                AND (quarter LIKE 'Mar %' OR quarter LIKE '%FY%')
                AND metric_name IN :metrics
                ORDER BY quarter DESC
                LIMIT 20
            """)

            with engine.connect() as conn:
                # Fetch Quarterly
                if period in ["quarterly", "both"]:
                    try:
                        q_df = pd.read_sql(q_sql, conn, params={"ticker": ticker, "metrics": tuple(metrics_list)})
                        if not q_df.empty:
                            data_context += "QUARTERLY RESULTS (Recent):\n" + q_df.to_string(index=False) + "\n\n"
                    except Exception:
                        pass

                # Fetch Yearly
                if period in ["yearly", "both"]:
                    try:
                        # Try primary yearly table first
                        y_df = pd.read_sql(y_sql_primary, conn, params={"ticker": ticker, "metrics": tuple(metrics_list)})
                        if not y_df.empty:
                            data_context += "ANNUAL RESULTS (Historical Trends):\n" + y_df.to_string(index=False) + "\n\n"
                        else:
                            # Fallback to financials_quarterly Mar entries
                            y_fallback_df = pd.read_sql(y_sql_fallback, conn, params={"ticker": ticker, "metrics": tuple(metrics_list)})
                            if not y_fallback_df.empty:
                                data_context += "ANNUAL RESULTS (Estimated from Q4/Historical):\n" + y_fallback_df.to_string(index=False) + "\n\n"
                    except Exception:
                        # If table doesn't exist, use fallback
                        try:
                            y_fallback_df = pd.read_sql(y_sql_fallback, conn, params={"ticker": ticker, "metrics": tuple(metrics_list)})
                            if not y_fallback_df.empty:
                                data_context += "ANNUAL RESULTS (Extracted from Quarterly DB):\n" + y_fallback_df.to_string(index=False) + "\n\n"
                        except Exception:
                            pass

        response = self.agent.run(f"Compare these companies based on the following data:\n\n{data_context}")
        output_text = response.content
        
        try:
            if "```json" in output_text:
                json_str = output_text.split("```json")[1].split("```")[0]
            elif "```" in output_text:
                json_str = output_text.split("```")[1].split("```")[0]
            else:
                json_str = output_text
            return json.loads(json_str.strip())
        except Exception as e:
            return {"error": "Failed to parse JSON", "raw_output": output_text}
