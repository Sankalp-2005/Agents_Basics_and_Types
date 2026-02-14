# Chitti - The First Agent

This project introduces "Chitti," a foundational AI agent built using Google's Agents Development Kit (ADK). Chitti serves as a helpful assistant, capable of leveraging Google Search to provide current and accurate information, embodying a basic yet powerful example of an intelligent agent.

## Overview

"Chitti" is designed as a general-purpose helpful assistant. Its core capability lies in its ability to understand and respond to user queries by performing real-time searches via Google Search. This makes Chitti an excellent starting point for demonstrating how to integrate external tools with an LLM agent for enhanced functionality.

## Features

*   **Helpful Assistant:** Chitti is programmed to be a cooperative and informative assistant, aiming to provide relevant answers to a wide range of questions.
*   **Google Search Integration:** The agent is equipped with the `google_search` tool, allowing it to access up-to-date information directly from the web. This is crucial for queries requiring current events, facts, or information not present in its training data.
*   **Intelligent Decision Making:** Chitti's instructions guide it to use Google Search whenever current information is needed or if it's unsure about an answer, promoting accuracy and comprehensiveness.

## Agent Architecture

The project consists of a single, well-defined agent:

*   **`root_agent` (Named `chitti`):**
    *   **Name:** `chitti`
    *   **Model:** `gemini-2.5-flash` - A powerful and efficient large language model from Google, providing the core intelligence for understanding prompts and generating responses.
    *   **Description:** "Speed one teraHz memory one ZetaByte" (This is a playful, self-referential description for the agent, indicating its advanced capabilities).
    *   **Instruction:** "You are a helpful assistant. Use Google Search for current info or if unsure." - This critical instruction guides the agent's behavior, emphasizing the use of its tools for accuracy.
    *   **Tools:** `[google_search]` - The essential tool that allows Chitti to perform web searches and retrieve external information.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The framework used for defining, configuring, and deploying the AI agent.
*   **Gemini-2.5-flash Model:** Google's advanced large language model that powers the agent's natural language understanding and generation capabilities.
*   **Google Search Tool:** An integrated tool within the ADK, enabling the agent to perform web searches and access real-world information.
*   **Python:** The programming language used to define the agent.

## Usage

To interact with "Chitti," you would typically send it a query or a request. The agent will then process your input, decide whether to use Google Search, and provide a helpful response.

Example interaction (conceptual):

```python
# Assuming 'root_agent' is instantiated and ready to run
query = "What is the capital of France?"
response = root_agent.run(query)
print(response)

query = "What are the latest developments in AI?"
response = root_agent.run(query)
print(response)
```

In the first query, Chitti might use its internal knowledge. In the second, it would likely invoke the `google_search` tool to fetch the most recent information.
