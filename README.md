# Cani — Autonomous Payment Safeguard Bot 🛡️🌌

An agentic commerce application that intercepts natural language purchase requests, enforces real-time budgetary safety guardrails, and executes transactions via the PayPal Sandbox REST API.

## 🚀 Category
**Option B:** Agentic Commerce & Autonomous Payment Safeguard Bot

## ✨ Features
* **Natural Language Purchase Processing:** Parses buy intent from free-form user prompts using Groq / Llama 3.
* **Autonomous Safeguards:** Real-time policy interceptor that blocks purchases exceeding the user's `$100.00` safety limit.
* **PayPal REST API Integration:** Generates real PayPal Sandbox Order IDs dynamically upon approval.
* **Antigravity Glassmorphism UI:** Built with Streamlit featuring glowing status cards, live metrics, and test triggers.

## 🛠️ Stack
* **Frontend:** Streamlit (Custom Glassmorphism CSS)
* **AI Orchestration:** LangChain, Groq API (`llama-3.3-70b-versatile`)
* **Payment Gateway:** PayPal Sandbox REST API (`/v2/checkout/orders`)
* **Environment Management:** Python `dotenv`

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/kit25csebdeepikaj-spec/cani-agent.git](https://github.com/kit25csebdeepikaj-spec/cani-agent.git)
cd cani-agent