# Travel Planner with Parallel Agents

This project showcases a sophisticated travel planning system built using Google's Agents Development Kit (ADK). It leverages a parallel agent architecture to efficiently gather and present comprehensive travel information, making trip planning seamless and insightful.

## Overview

The system is designed to act as a personal travel assistant, capable of providing detailed information across various travel aspects simultaneously. By utilizing `ParallelAgent`, it ensures that multiple queries (e.g., weather, tickets, accommodation) are processed concurrently, leading to faster response times and a more integrated travel plan.

## Features

The travel planner integrates several specialized agents to cover all essential aspects of trip planning:

*   **Weather Checking Agent:** Provides real-time current weather status and relevant climate information for any specified location.
*   **Tickets Checking Agent:** Searches for flight, train, and bus ticket availability between given locations, highlighting the cheapest options for each mode of transport.
*   **Tourist Destination Suggestion Agent:** Identifies and recommends the top 5 major tourist attractions at the user's destination.
*   **Food Suggestion Agent:** Curates a list of 5 must-try famous and regional cuisines or dishes specific to the travel destination.
*   **Accommodation Checking Agent:** Traces available accommodations, including hotels, lodges, and paying guests, returning the top 5 cheapest and highly-rated options.
*   **Aggregator Agent:** Gathers and synthesizes all the information collected by the parallel agents into a concise, well-structured travel itinerary.

## Architecture

The project employs a robust agent architecture built with Google ADK:

*   **`ParallelAgent`**: This agent orchestrates the concurrent execution of five specialized sub-agents: `whether_check_agent`, `tickets_checking_agent`, `tourist_destination_suggestion_agent`, `food_suggestion_agent`, and `accommodation_checking_agent`. This parallel processing significantly enhances the efficiency of information retrieval.
*   **`AggregatorAgent`**: After the parallel agents complete their tasks, this agent takes their individual outputs and intelligently combines them into a coherent and user-friendly summary, presenting a complete travel plan.
*   **`SequentialAgent` (Root Agent)**: This is the top-level agent that defines the overall flow. It first initiates the `ParallelAgent` to gather diverse information and then passes the results to the `AggregatorAgent` for final compilation and presentation.

## Technologies Used

*   **Google ADK (Agents Development Kit):** The core framework for building and managing the agents.
*   **Gemini-2.5-flash-lite Model:** The underlying large language model powering the intelligence of each agent.
*   **Google Search Tool:** Utilized by most agents to perform real-time information retrieval from the web.

## Usage

To utilize this travel planner, you would typically interact with the `root_agent` by providing your travel queries (e.g., destination, dates). The system will then autonomously execute the defined agent workflow to fetch and compile your personalized travel plan.

*(Further instructions on setting up the environment, installing dependencies, and running the agent would be provided here, assuming the full project context was available.)*