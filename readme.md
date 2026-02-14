# Google ADK Agent Examples

This repository serves as a collection of diverse AI agent implementations built using Google's Agents Development Kit (ADK). It showcases various agent types, architectures, and capabilities, providing practical examples for developers looking to understand and leverage the ADK framework for building intelligent applications.

## Overview

The projects within this folder demonstrate fundamental concepts of agent-based programming with Google ADK, including single agents, sequential workflows, parallel processing, and iterative feedback loops. Each project focuses on a distinct use case, illustrating how different agent configurations can solve specific problems.

## Projects Included

Here's a summary of the AI agent projects available in this collection:

### 1. Travel Planner with Parallel Agents (`parallel_agent`)
*   **Description:** A sophisticated travel planning system that leverages a `ParallelAgent` architecture to gather comprehensive travel information (weather, tickets, destinations, food, accommodation) concurrently. It then aggregates this information into a cohesive travel plan.
*   **Key Concept:** Demonstrates parallel execution of multiple sub-agents for efficient information gathering.

### 2. README Creation Agent (`readme_creation_agent`)
*   **Description:** An intelligent agent designed to automate the creation of professional and insightful `README.md` files for code repositories. It reads a given Python file, analyzes its contents, and generates a structured README.
*   **Key Concept:** Illustrates how an agent can understand code and generate descriptive documentation, utilizing custom tools for file operations.

### 3. LinkedIn Caption Writing Agent (`sequential_agent`)
*   **Description:** An agent that automates the generation of engaging LinkedIn captions through a `SequentialAgent` workflow. It first uses a research agent to gather information on a given topic and then passes it to a writing agent to craft the caption.
*   **Key Concept:** Showcases sequential processing, where tasks are performed in a defined order, with the output of one agent serving as input for the next.

### 4. Collaborative Story Writing Agent with Iterative Feedback (`loop_agent`)
*   **Description:** This project implements an iterative story writing system where an initial draft is refined through a feedback loop. A `LoopAgent` orchestrates a critic agent (providing suggestions) and a writer agent (incorporating changes) until the story is approved or a maximum iteration count is reached.
*   **Key Concept:** Highlights the use of `LoopAgent` for iterative processes, feedback mechanisms, and controlled refinement workflows.

### 5. Chitti - The First Agent (`chitti - the first agent`)
*   **Description:** A foundational AI assistant capable of leveraging Google Search to provide current and accurate information. Chitti serves as a basic yet powerful example of a single, intelligent agent integrated with external tools.
*   **Key Concept:** Introduces the fundamental structure of an `Agent` with an LLM and external tools (Google Search) for enhanced knowledge retrieval.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The primary framework for building and deploying all agents.
*   **Gemini-2.5-flash / Gemini-2.5-flash-lite Models:** The underlying large language models from Google that power the intelligence, natural language understanding, and generation capabilities of the agents.
*   **Google Search Tool:** Frequently used across various agents to enable real-time information retrieval from the web.
*   **Python:** The programming language for implementing all agent logic and custom tools.

## Getting Started

Each project folder contains its own `agent.py` file, which defines the agent(s) and their logic. To explore a specific project, navigate to its respective directory.

*(Further instructions on setting up the ADK environment, installing dependencies, and running these agents would typically be provided in a more comprehensive repository.)*
