# 📝 OpenAI Agents Assignments
This repository includes three mini-projects using the OpenAI Agents SDK, each demonstrating a unique agent use-case with tools, orchestration, and agent handoff logic.

# ⿡ Smart Store Agent
📄 File: product_suggester.py

**🔍 Description**
An AI agent that suggests a product (e.g. medicine) based on user needs or symptoms.

**✅ Example**
User: I have a headache
Agent: You may try Panadol. It's effective for headaches due to its paracetamol content.

🚀 Run
```bash
uv run product_suggester.py
```

# ⿢ Mood Analyzer with Handoff
📄 File: mood_handoff.py

**🔍 Description**
A multi-agent setup where:

Agent 1 analyzes the user's mood

Agent 2 suggests an activity if the user is sad or stressed

**✅ Example**
User: I'm feeling low today
→ Mood: Sad
→ Suggested Activity: Try journaling or taking a walk.

🚀 Run
```bash
uv run mood_handoff.py
```

# ⿣ Country Info Bot (Using Tools)
📄 File: country_info_toolkit.py

**🔍 Description**
Uses tool agents to provide complete information about a country.

**🧰 Tools**
Capital Tool 🏛

Language Tool 🗣

Population Tool 👥

An orchestrator agent uses all three tools to compile a full summary.

**✅ Example**
User: Pakistan
→ Capital: Islamabad
→ Language: Urdu
→ Population: 240 million

🚀 Run
```bash
uv run country_info_toolkit.py
```

# 📦 Requirements

Python 3.10+

uv add openai-agents python-dotenv

uv-package-manager

**Made with ❤ by [Faria Mustaqim](https://github.com/Zaibunis)**
