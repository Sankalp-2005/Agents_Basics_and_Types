# README Creation Agent

This project features a specialized AI agent designed to automate the creation of professional and insightful `README.md` files for code repositories. Built using Google's Agents Development Kit (ADK), this agent streamlines the documentation process, making it easier for developers to maintain high-quality project documentation on platforms like GitHub.

## Overview

The `README Creation Agent` is an intelligent assistant that takes a file path to a Python script, analyzes its contents, and then generates a comprehensive `README.md` file. Its primary goal is to provide a detailed and professional overview of the code, making it readily understandable for anyone exploring the repository.

## Features

The agent is equipped with the following capabilities:

*   **File Reading:** It can read the content of any specified Python file, extracting the raw code for analysis.
*   **Code Analysis:** The agent thoroughly analyzes the provided code to understand its functionality, purpose, and key components.
*   **README Generation:** Based on its analysis, it constructs a professional and insightful `README.md` file content. This includes sections like:
    *   Project Title
    *   Overview/Introduction
    *   Features
    *   Architecture/How it Works
    *   Technologies Used
    *   Usage Instructions
*   **File Writing:** It writes the generated `README.md` content to a new file named `readme.md` in the current directory.

## How it Works

The `read_me_creation_agent` operates through a defined workflow:

1.  **Input Reception:** The agent receives a file path from the user as input.
2.  **Code Retrieval:** It utilizes the `readme_file_read_fn` tool to open and read the contents of the file at the given path.
3.  **Content Analysis:** The agent's core intelligence (powered by the `gemini-2.5-flash` model) processes the retrieved code, identifying its structure, functionality, and the overall intent of the script.
4.  **README Content Generation:** Based on its understanding, the agent crafts a markdown string suitable for a `README.md` file, incorporating all necessary sections for effective documentation.
5.  **File Creation:** Finally, it employs the `readme_file_write_fn` tool to write the generated markdown string into a new `readme.md` file.

## Agent Architecture

The project is structured around a single, powerful agent:

*   **`read_me_creation_agent`**: This is the root agent responsible for the entire `README.md` generation process.
    *   **Model**: `gemini-2.5-flash` - A highly capable language model enabling advanced code comprehension and text generation.
    *   **Description**: "You are an helpful agent to create a readme.md file for the given code."
    *   **Instruction**: A detailed directive guiding the agent through the steps of reading a file, analyzing its content, generating a `README.md` string, and writing it to a file.
    *   **Tools**:
        *   `readme_file_read_fn`: A custom `FunctionTool` to read content from a specified file path.
        *   `readme_file_write_fn`: A custom `FunctionTool` to write a given text string to a `readme.md` file.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The foundational framework for building and deploying the AI agent.
*   **Gemini-2.5-flash Model:** The advanced large language model that provides the intelligence for understanding code and generating human-quality text.
*   **Python:** The programming language used for implementing the agent and its custom tools.

## Usage

To use the `README Creation Agent`, you would provide it with the file path to the Python code you wish to document. The agent will then process the file and create a `readme.md` in the directory where the agent is executed.

Example interaction (conceptual):

```
user_input = "C:\\path\\to\\your\\code.py"
root_agent.run(user_input)
```

This would trigger the agent to read `code.py`, generate the `README.md` content, and then save it.
