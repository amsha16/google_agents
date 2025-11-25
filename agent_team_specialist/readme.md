# Multi-agent System

This is a team of simple, specialized agents that collaborate, just like a real-world team. Each agent has one clear job (e.g., one agent only does research, another only writes).
This makes them easier to build, easier to test, and much more powerful and reliable when working together.

## Overall design
<img width="1630" height="632" alt="multi-agent-team" src="https://github.com/user-attachments/assets/02eccce9-bb3b-4f50-b105-420340cf0372" />

After executing query in chat window
<img width="1148" height="666" alt="image" src="https://github.com/user-attachments/assets/f843daab-25e0-4590-bfe6-38e0351fcd5e" />

Flow of events where it becomes interesting
STEP 1 - Call to ResearchAgent
<img width="663" height="861" alt="image" src="https://github.com/user-attachments/assets/60e07d40-71a6-41c6-9102-12c9ceb59052" />
STEP 2 - functionResponse:ResearchAgent
<img width="681" height="870" alt="image" src="https://github.com/user-attachments/assets/2d0223ad-706d-4663-8cc3-97e34852fe92" />
STEP 3 - Call to SummarizerAgent
<img width="686" height="867" alt="image" src="https://github.com/user-attachments/assets/96d2a7f4-5b84-48ae-9832-fd81e5254afc" />
STEP 4 - functionResponse:SummarizerAgent
<img width="682" height="873" alt="image" src="https://github.com/user-attachments/assets/2922ca48-97e1-4aaa-95a7-8837e3ef817e" />
STEP 5 - Response to user
<img width="678" height="870" alt="image" src="https://github.com/user-attachments/assets/d088658d-7812-4155-b68d-593cb7244e69" />








