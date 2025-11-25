# Sequential Agents


When tasks need to happen in a **certain, specific order**, we can use a `SequentialAgent`. This is like an assembly line, running each sub-agent in the exact order as listed. The output of one agent\step automatically becomes the input for the next, creating a predictable and reliable workflow.

Here is a system with three specialized agents:
1. **Outline Agent** - Creates a blog outline for a given topic
2. **Writer Agent** - Writes a blog post
3. **Editor Agent** - Edits a blog post draft for clarity and structure

## Typical Flow
<img width="1072" height="73" alt="image" src="https://github.com/user-attachments/assets/4c72e66c-24b2-48bb-9a29-978ea6e956fe" />

## Chat example 
<img width="1347" height="767" alt="Chat" src="https://github.com/user-attachments/assets/56f44b20-bc8b-4b8a-8822-3fa7ed2f7146" />

## Events
## STEP 1 - OutlinerAgent - title attribute is the output that will be fed to the next agent

<img width="517" height="820" alt="Chat_1" src="https://github.com/user-attachments/assets/3f0c05c3-71f4-493d-a361-ee13ba4202c8" />

## STEP 2 - WriterAgent - Content > parts > 0 is the output from above and title is the generated draft.

<img width="502" height="886" alt="Chat_2" src="https://github.com/user-attachments/assets/b67fc922-fead-48f0-8607-553430a57418" />

## STEP 3 - EditorAgent - title contains the final output

<img width="502" height="885" alt="Chat_3" src="https://github.com/user-attachments/assets/50941979-a0e5-4d28-8d1d-69b1df83740b" />
