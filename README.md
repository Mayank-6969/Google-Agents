# Google-Agents: Multi-Tool AI Personal Assistant

A production-ready, agentic system that bridges a clean Python **Streamlit** frontend chat interface with an **n8n orchestration backend** to deliver a fully autonomous executive assistant. 

Instead of acting as a simple AI chatbot wrapper, this system processes unstructured human text commands, dynamically determines intent, routes logic across a native tool network, and executes complex physical operations like sending emails, organizing calendars, and updating tasks in real-time.

---

## 🧠 How It Works (The Architecture)

The system isolates user interaction from core automation logic using a lightweight frontend and an event-driven webhook architecture:

1. **User Command (Streamlit Frontend):** The user enters a natural language request (e.g., *"Check my latest email from John, summarize it, add any action items to my Google Tasks, and send a reply saying I'm on it"*). Streamlit packages this text along with a persistent `sessionId` to maintain conversation memory.
2. **Webhook Trigger:** The payload is securely delivered to an active n8n webhook listener.
3. **Agentic Router (The Brain):** An n8n AI Agent node (powered by an OpenRouter LLM model) evaluates the user's prompt against a structured system prompt (`sysprompt.md`). It uses a loop to intelligently select, string together, and execute the exact tools needed to fulfill the request.
4. **Action Execution:** The agent interacts natively with Google APIs and external search engines, performing sequential tasks autonomously before sending a unified final response back through the webhook to the chat UI.

---

## 🛠️ Core Agent Capabilities

By utilizing an active multi-tool canvas, the agent can perform the following operations from a single chat prompt:

### 📬 Gmail Automation
- **Read & Analyze:** Fetches single or batch unread messages from your inbox.
- **Intelligent Summarization:** Extracts key action items, tone, and priority details from complex threads.
- **Smart Replies:** Dynamically structures and sends professional email responses or drafts new emails on command.

### 📅 Google Calendar Management
- **Event Creation:** Parses ambiguous date/time phrasing (e.g., *"Schedule a meeting for next Tuesday at 3 PM"*) and creates full calendar invites.
- **Schedule Auditing:** Retrieves and lists your agenda for the day or week to prevent scheduling conflicts.

### ✅ Task & To-Do Tracking
- **Google Tasks Sync:** Creates, lists, and updates specific task lists based on your workflow conversation.
- **Automated Deletion:** Safely removes completed items or specific tasks when explicitly requested.

### 🔍 Real-Time Web Search
- **SerpApi Engine:** When asked about current events, market data, or factual information outside the model's static training knowledge, the agent autonomously falls back to a Google Search tool to fetch accurate, up-to-date data.

---

## 💻 Tech Stack
- **Frontend UI:** Streamlit (Python 3.12+)
- **Automation Backend:** n8n (Advanced Tool-Node Routing Framework)
- **Language Model Gateway:** OpenRouter API
- **Local Tunneling Engine:** Ngrok 

---

## 🚀 Getting Started

### 1. Clone & Install Dependencies
Ensure you have Python 3.12+ configured locally.
```bash
git clone [https://github.com/Mayank-6969/Google-Agents.git](https://github.com/Mayank-6969/Google-Agents.git)
cd Google-Agents
pip install -r requirements.txt
