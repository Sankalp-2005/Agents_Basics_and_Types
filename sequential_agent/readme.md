# LinkedIn Caption Writing Agent

This project presents an intelligent LinkedIn caption writing agent, developed using Google's Agents Development Kit (ADK). This sequential agent automates the process of generating engaging LinkedIn captions by first conducting thorough research on a given topic and then crafting a concise and informative post.

## Overview

The LinkedIn Caption Writing Agent is designed to streamline content creation for professionals and marketers on LinkedIn. By leveraging a two-stage sequential process, it ensures that captions are not only well-written but also backed by relevant and up-to-date information, making it an invaluable tool for enhancing professional online presence.

## Features

The agent comprises two specialized sub-agents, each contributing to the caption generation process:

*   **Research Agent (`research_agent`):**
    *   **Functionality:** Acts as a dedicated research assistant.
    *   **Task:** Utilizes Google Search to extensively research a user-provided topic.
    *   **Output:** Provides comprehensive and relevant information gathered from its research.
*   **Writing Agent (`writing_agent`):**
    *   **Functionality:** A skilled content writer.
    *   **Task:** Takes the detailed information supplied by the `research_agent` and synthesizes it into a LinkedIn-appropriate caption.
    *   **Output:** Generates a LinkedIn caption, typically 1-2 paragraphs long, highlighting the main points and key information from the research.

## Architecture

The project's architecture is built around a `SequentialAgent` to manage the logical flow of information processing:

*   **`SequentialAgent` (`root_pipeline`):** This is the main orchestrator that defines the order of execution for the sub-agents. It ensures that research is completed before caption writing begins.
    *   **Sub-agents:**
        1.  **`research_agent`**: The first agent in the sequence. Its `output_key` (`research_output`) feeds directly into the `writing_agent`.
        2.  **`writing_agent`**: The second agent, which consumes the `research_output` to perform its task of caption generation. Its `output_key` (`final_caption`) represents the ultimate output of the entire pipeline.

This sequential design guarantees a structured approach, where information gathering precedes content creation, leading to well-informed and coherent LinkedIn captions.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The foundational framework for building, configuring, and deploying the AI agents.
*   **Gemini-2.5-flash-lite Model:** The underlying large language model powering the intelligence of both the `research_agent` and the `writing_agent` for understanding queries, processing information, and generating text.
*   **Google Search Tool:** Integrated into the `research_agent` to enable real-time information retrieval from the web, ensuring the captions are based on current data.

## Usage

To use the LinkedIn Caption Writing Agent, you would interact with the `root_pipeline` by providing the topic for which you need a LinkedIn caption. The agent will then autonomously execute the research and writing tasks in sequence, delivering a polished caption as its final output.

Example interaction (conceptual):

```
# Assuming 'root_pipeline' is instantiated and ready to run
topic = "The Future of AI in Healthcare"
caption = root_pipeline.run(topic)
print(caption)
```

This would initiate the `research_agent` to search for information on "The Future of AI in Healthcare," and subsequently, the `writing_agent` would use this information to compose a compelling LinkedIn caption.
