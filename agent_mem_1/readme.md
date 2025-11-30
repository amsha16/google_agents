# Agent with memory

## Overall design

Session : A session is a container for conversations. It encapsulates the conversation history in a chronological manner and also records all tool interactions and responses for a single, continuous conversation. A session is tied to a user and agent; it is not shared with other users. Similarly, a session history for an Agent is not shared with other Agents.

In ADK, a Session is comprised of two key components Events and State:

📝 Session.Events:

While a session is a container for conversations, Events are the building blocks of a conversation.

Example of Events:

User Input: A message from the user (text, audio, image, etc.)
Agent Response: The agent's reply to the user
Tool Call: The agent's decision to use an external tool or API
Tool Output: The data returned from a tool call, which the agent uses to continue its reasoning
{} Session.State:

session.state is the Agent's scratchpad, where it stores and updates dynamic details needed during the conversation. Think of it as a global {key, value} pair storage which is available to all subagents and tools.

<img width="381" height="378" alt="image" src="https://github.com/user-attachments/assets/8ab33649-5cc8-4b6c-b29e-c08712880427" />

## How to manage sessions?
An agentic application can have multiple users and each user may have multiple sessions with the application. To manage these sessions and events, ADK offers a Session Manager and Runner.

SessionService: The storage layer

Manages creation, storage, and retrieval of session data
Different implementations for different needs (memory, database, cloud)
Runner: The orchestration layer

Manages the flow of information between user and agent
Automatically maintains conversation history
Handles the Context Engineering behind the scenes
Think of it like this:

Session = A notebook 📓
Events = Individual entries in a single page 📝
SessionService = The filing cabinet storing notebooks 🗄️
Runner = The assistant managing the conversation 🤖

## Chat

<img width="1346" height="477" alt="image" src="https://github.com/user-attachments/assets/8079e738-8f82-4739-8d2e-f6370578fed4" />

## Events

### 1

<img width="526" height="717" alt="image" src="https://github.com/user-attachments/assets/cc7329af-0b0f-4130-a45d-1cd81277e4c1" />

### 2

<img width="522" height="717" alt="image" src="https://github.com/user-attachments/assets/46465c1b-8ebd-46d8-845b-bc2350eb2ba2" />

### 3

<img width="516" height="710" alt="image" src="https://github.com/user-attachments/assets/abb4fed4-78b5-442c-9753-72d6bc53a83b" />






