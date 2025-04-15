import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent, LlmAgent
from .tools.listing_tools import get_all_symbols, get_industries_icb, get_symbols_by_exchange, get_symbols_by_group, get_symbols_by_industries

listing_agent = LlmAgent(
    name="listing_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to query stock listing information",
    instruction="You are a helpful stock analyst providing stock listing information",
    tools=[get_all_symbols, get_industries_icb, get_symbols_by_exchange, get_symbols_by_group, get_symbols_by_industries],
)

root_agent = Agent(
    name="vn_stock_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Agent to answer questions about Vietnamese stock market."
    ),
    instruction=(
        "You are a helpful stock analyst who can answer user questions about the Vietnamese stock market."
    ),
    sub_agents=[listing_agent],
)