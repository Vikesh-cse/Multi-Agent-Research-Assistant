# Multi-Agent Research Assistant

A powerful AI-powered research system built using **LangChain**, **Groq LLM**, **Tavily Search**, and **BeautifulSoup**.

The system uses multiple specialized agents to:
- Search the web for recent information
- Scrape and analyze webpages
- Generate detailed research reports
- Critically review generated reports

---

## Features

### Search Agent
Searches the internet using Tavily and retrieves:
- Recent information
- Reliable sources
- Relevant URLs
- Research snippets

### Reader Agent
Scrapes webpages using BeautifulSoup and extracts:
- Main content
- Article text
- Relevant information
- Clean readable text

### Writer Agent
Creates a professional research report including:
- Executive Summary
- Key Findings
- Detailed Analysis
- Sources
- Conclusion

### Critic Agent
Reviews the generated report and evaluates:
- Accuracy
- Completeness
- Evidence quality
- Source credibility
- Logical consistency

---

## Architecture

```text
User Topic
     │
     ▼
Search Agent
(Tavily Search)
     │
     ▼
URLs & Research Results
     │
     ▼
Reader Agent
(BeautifulSoup Scraper)
     │
     ▼
Research Notes
     │
     ▼
Writer Agent
(Groq LLM)
     │
     ▼
Research Report
     │
     ▼
Critic Agent
(Groq LLM)
     │
     ▼
Final Evaluation
```

---

## Project Structure

```text
project/
│
├── main.py
├── agent.py
├── tools.py
├── .env
├── requirements.txt
└── README.md
```

### Files

#### agent.py

Contains:
- Search Agent
- Reader Agent
- Writer Chain
- Critic Chain

#### tools.py

Contains:
- Tavily Search Tool
- Web Scraping Tool

#### main.py

Executes the complete research pipeline:
1. Search
2. Read
3. Write
4. Critique

---

## Technologies Used

### LangChain

Agent creation and orchestration.

### Groq

Large Language Model provider.

Model:

```python
llama-3.3-70b-versatile
```

### Tavily

Real-time web search engine for AI agents.

### BeautifulSoup

Web scraping and HTML parsing.

### Requests

HTTP requests for webpage retrieval.

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/multi-agent-research-assistant.git

cd multi-agent-research-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Required Packages

```bash
pip install langchain
pip install langchain-groq
pip install tavily-python
pip install beautifulsoup4
pip install requests
pip install python-dotenv
pip install rich
```

Or:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Execute:

```bash
python main.py
```

Example:

```text
Enter research topic:

Future of AI Agents
```

---

## Sample Output

### Generated Report

```text
# Executive Summary

AI agents are becoming increasingly capable of
performing autonomous tasks...

# Key Findings

1. Multi-agent systems improve specialization.

2. Agentic workflows outperform traditional
chatbots in complex tasks.

3. AI agents are being integrated into
enterprise software ecosystems.

# Sources

https://...

https://...

# Conclusion

AI agents are expected to become a major
component of future software systems.
```

### Critic Review

```text
Overall Score: 9/10

Strengths:
- Well structured
- Good evidence
- Reliable sources

Weaknesses:
- Missing economic impact discussion

Suggested Improvements:
- Add recent market statistics
- Include additional research sources

Final Verdict:
PASS
```

---

## Future Improvements

- LangGraph workflow orchestration
- Parallel research agents
- Source ranking
- Citation verification
- PDF report generation
- Vector database integration
- RAG support
- Human-in-the-loop review
- Research memory
- Streamlit interface

---

## Learning Objectives

This project demonstrates:

- Multi-Agent Systems
- Tool Calling
- Web Search Integration
- Web Scraping
- Prompt Engineering
- Research Automation
- Report Generation
- Agent Collaboration
- LangChain Development
- LLM Application Development

---

## Author

Vikesh Kumar

B.Tech Computer Science Engineering

Generative AI & Agentic AI Enthusiast
