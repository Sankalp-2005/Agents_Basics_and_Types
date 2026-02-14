# Collaborative Story Writing Agent with Iterative Feedback

This project introduces an intelligent agent system designed for collaborative and iterative story writing, built upon Google's Agents Development Kit (ADK). It simulates a creative process where an initial draft is refined through a feedback loop involving a critic and a writer, showcasing the power of `LoopAgent` for iterative tasks.

## Overview

The Collaborative Story Writing Agent automates the process of drafting and refining textual content, such as a story. It starts with an initial concept from the user, generates a first draft, and then enters a feedback loop where a "critic" agent provides suggestions, and a "writer" agent incorporates these changes. This cycle continues until the critic approves the story or a maximum number of iterations is reached, ensuring a well-developed and polished final output.

## Features

The system is composed of several specialized agents working in concert:

*   **Initial Writer Agent (`initial_writer`):**
    *   **Functionality:** Generates the very first draft of a story or text based on the user's initial request and any provided suggestions.
    *   **Output:** Produces the `current_story` which serves as the starting point for refinement.
*   **Critic Agent (`critic_agent`):**
    *   **Functionality:** Acts as an editor, critically reviewing the `current_story`.
    *   **Task:** Provides constructive suggestions to make the story more interesting and creative.
    *   **Approval Mechanism:** If the critic deems the story satisfactory, it returns the string `'Approved'`, signaling the end of the refinement loop.
    *   **Output:** Generates `critic` feedback or an approval status.
*   **Writer Agent (`writer_agent`):**
    *   **Functionality:** Incorporates feedback and updates the story.
    *   **Task:** Takes the `current_story` and the `critic`'s suggestions as input, then revises the story accordingly.
    *   **Loop Termination:** If the `critic`'s feedback is `'Approved'`, this agent calls the `exit_loop` function to terminate the iterative process.
    *   **Output:** Produces the `current_story`, which is the updated draft.
*   **Exit Loop Function (`exit_loop`):**
    *   **Functionality:** A simple tool called by the `writer_agent` when the story is approved.
    *   **Purpose:** Provides a structured way to signal the successful completion and exit the `LoopAgent`.

## Architecture

The project's architecture is built around a `SequentialAgent` and a `LoopAgent` to manage the multi-stage story creation process:

*   **`SequentialAgent` (`root`):**
    *   This is the top-level agent that orchestrates the entire workflow.
    *   It first invokes the `initial_writer` to get the base story.
    *   Once the initial draft is ready, it passes control to the `loop_agent` for iterative refinement.
*   **`LoopAgent` (`loop_agent`):**
    *   This agent is responsible for the iterative feedback cycle.
    *   **Sub-agents:** It sequentially runs the `critic_agent` and then the `writer_agent` within its loop.
    *   **Max Iterations:** Configured with `max_iterations=2` (in this example), meaning the loop will run at most two times if the story isn't approved earlier. This prevents infinite loops.
    *   **Exit Condition:** The loop continues until the `writer_agent` explicitly calls the `exit_loop` function (triggered by the critic's 'Approved' status).

This design ensures a structured flow: initial creation followed by a controlled, iterative refinement process.

## How it Works

1.  **Initial Draft:** The `root_agent` first activates the `initial_writer` based on the user's prompt to generate the first version of the story.
2.  **Enter Loop:** The `current_story` from the `initial_writer` is then passed to the `loop_agent`.
3.  **Critic's Feedback:** Inside the `loop_agent`, the `critic_agent` reviews the `current_story` and provides suggestions.
4.  **Writer's Revision:** Next, the `writer_agent` receives the `current_story` and the `critic`'s suggestions. It revises the story accordingly.
5.  **Approval or Iteration:**
    *   If the `critic` returned `'Approved'`, the `writer_agent` calls the `exit_loop` function, and the `loop_agent` terminates.
    *   If not approved, the `loop_agent` continues to the next iteration (up to `max_iterations`), and the revised `current_story` is sent back to the `critic_agent` for another round of feedback.
6.  **Final Output:** The process concludes when the story is approved or `max_iterations` is reached, providing a refined version of the text.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The core framework for building and managing sequential and looping agent workflows.
*   **Gemini-2.5-flash-lite Model:** The underlying large language model powering the intelligence of all agents for understanding context, generating text, and providing critical feedback.
*   **Python:** The programming language used for implementing the agents and the custom `exit_loop` function.
*   **FunctionTool:** Used to expose the `exit_loop` Python function as a callable tool for the `writer_agent`.

## Usage

To use this collaborative story writing agent, you would typically interact with the `root_agent` by providing the initial prompt or concept for your story. The agent system will then autonomously manage the drafting and refinement process, eventually presenting you with a polished story.

Example interaction (conceptual):

```python
# Assuming 'root_agent' is instantiated and ready to run
user_story_prompt = "Write a short fantasy story about a brave knight and a hidden magical forest."
final_story = root_agent.run(user_story_prompt)
print(final_story)
```

This would initiate the `initial_writer`, followed by the `loop_agent`'s iterative feedback and revision cycle, culminating in a refined fantasy story.
