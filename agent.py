import os
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from paypal_service import create_sandbox_order

USER_BUDGET_LIMIT = 100.00 

@tool
def execute_paypal_checkout(amount: float, product_name: str) -> str:
    """Executes a secure PayPal sandbox payment if the price is within budget limits."""
    if amount > USER_BUDGET_LIMIT:
        return f"BLOCKED: Transaction of ${amount} for '{product_name}' exceeds the user's safety budget limit of ${USER_BUDGET_LIMIT}."
    
    result = create_sandbox_order(str(amount))
    if result["status"] == "success":
        return f"SUCCESS: Approved and created PayPal Sandbox Order ID: {result['order_id']} for item: '{product_name}' (${amount})."
    else:
        return f"FAILED: PayPal transaction error - {result['message']}"
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Initialize ChatGroq using the environment variable
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-20b",
    temperature=0
).bind_tools([execute_paypal_checkout])