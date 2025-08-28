

## Imported snippet – 2025-07-03 20:01:47

Creating a GPT
How to create a GPT
Updated over 3 months ago
Creating a GPT is only available to paid users and is currently powered by GPT-4o.
GPTs are custom versions of ChatGPT that users can tailor for specific tasks or topics by combining instructions, knowledge, and capabilities. They can be as simple or as complex as needed, addressing anything from language learning to technical support. Plus, Team, and Enterprise users can start creating GPTs at chatgpt.com/create.
Here’s how to create a GPT
Either head to https://chatgpt.com/gpts/editor
or head to https://chatgpt.com/gpts and in the top right cornet click “+ Create”
You will see two tabs: 'Configure' and 'Create'. In the Create tab, you can message the GPT Builder to help you build a new GPT. You can say something like, "Make a creative who helps generate visuals for new products" or "Make a software engineer who helps format my code."
To name and set the description of your GPT, head to the Configure tab. Here, you will also be able to select the actions you would like your GPT to take, like browsing the web or creating images. You can add Instructions and conversation starters as well.
When you’re ready to publish your GPT, select “Publish” and share it with other people if you’d like.
Now you’ve created a GPT!
Settings in the Configure tab
Adding an image: You can ask the GPT Builder to create an image for your GPT or you can upload your own under the Configure tab. This image will serve as an icon for your GPT when it appears in the list of GPTs in the Library.
Instructions: Here you can provide detailed instructions or guidelines on how the GPT should behave, its functionalities, and any behavior to avoid.
Prompt Starters: These are examples of prompts for the user to start the conversation.
Knowledge: This allows you to provide additional context for your GPT to reference. Please note that content from the files that are uploaded could be included in the output. For file formats and size, as well as per-GPT limits, please consult the File Uploads FAQ.
Capabilities: Enabling Web Search, Canvas, Image Generation, and Code Interpreter & Data Analysis, will allow the GPT to perform additional functionality.
Custom Actions: You can make third-party APIs available to your GPT by providing details about the endpoints, parameters, and a description about how the model should use it. Actions for GPTs can also be imported from an OpenAPI schema. So if you’ve already built a plugin, you will be able to use your existing plugin manifests to define actions for your GPT.
Managing your GPTs
Once a GPT is created, certain Management capabilities will appear in the top right hand corner. You will see the 'Copy link', 'Version History', 'Duplicate GPT', and 'Delete GPT' options, as well as sharing settings.
​
Update option will allow you to create a new version of the GPT.
​
Depending on your plan, there are various further configurations available.
​
When on a Teams, Enterprise or Edu plan, sharing capabilities and various actions and integration settings, can be limited by workspace owners.
​
As a workspace owner, within the account settings at the top left of the screen, click on your Profile, then "Manage workspace" to navigate to your workspace settings and on the right hand side, find the "GPTs" tab. Alternatively, just navigate to https://chatgpt.com/admin/gpts. You should see the following settings:
​
1. Sharing: Choose who the GPTs can be shared with.
2. GPT Actions: Control whether action calls are restricted to specific domains. By unchecking 'Allow all domains for GPT actions,' you can specify particular domains and actions, ensuring that users are only permitted to make calls to the domains you designate.
​
3. Third-party: Allow users in your workspace to access and use GPTs that were created outside of it.
​
As the owner of your ChatGPT workspace, you can view all GPTs within the workspace, along with their creation and update timestamps, assignees, and usage statistics. Simply scroll down to the table view, where you can manage ownership and access settings for each individual GPT. You can also use the filter at the top right of the table to narrow down GPTs based on their capabilities and access permissions.
​
If you are a User on a Plus or Pro plan, the management limitations above do not apply, and you can simply view your usage statistics under https://chatgpt.com/gpts/mine.
Understanding your GPT metrics
In this same view within your GPTs list, you can see how much your GPT has been used. The "Chats" column shows the total number of chats initiated within the GPT since its creation.
If your number is 10+ or 100+, that means the total number of chats is between 10-20 or 100-200.
FAQ
Q: How many files can I upload to a GPT?
A: We allow up to 20 files to be uploaded to a custom GPT.
​
​Q: My GPT isn't generating certain files, creating graphs, or handling analytical tasks well. Why is that?
​A: Please ensure that the Code Interpreter & Data Analysis capability is enabled.
​
Q: The custom GPT management page is loading very slowly, likely because I have many custom chats. How can I fix this?
​A: We are aware of the issue and are actively working on performance improvements for this page.


## Imported snippet – 2025-07-03 20:01:58

GPT Builder
What is the GPT Builder for in ChatGPT and why did we make it?
Updated over 10 months ago
The GPT Builder is an easy starting point to build custom GPTs. Builders can use a conversational interface to create their GPT without having to manually fill out the required fields.
Under the hood, the GPT Builder is built as a custom GPT with instructions and an action that allows it to write to the fields of the GPT that’s currently being built.
The process of building it helped us discover what GPT builders might want in the product and we were pleasantly surprised at its instruction following capabilities.
More advanced builders should use the manual configuration UI to edit the fields of their GPT but the GPT Builder can always serve as a starting place.
We're continuing to evolve GPT Builder over time to become a better tool for both new and advanced builders
Behind the scenes
Since the GPT Builder is a custom GPT itself, we are able to share the configuration we use as an example of how to create robust GPTs.
Instructions
The following are the core of the instructions we use to power the GPT Builder as of January 3rd, 2024. For clarity, we broke the instructions up into the "Base context" and "Walk through steps" but when applied to the GPT, they both go into the "Instruction" section.
Base context
Walk through steps
Action
All of the information made available to a GPT, including the prompt, instructions, and attached files, may be used by the model to construct a response to the user. Don't include information you do not want the user to know.


## Imported snippet – 2025-07-03 20:02:06

How do I verify my builder profile with social media?
Updated over a year ago
Builders can now link their social profiles using Twitter, GitHub, and LinkedIn in addition to a website domain. Please note for LinkedIn, it's only possible to link to a personal page (company page links are not supported at this time).


## Imported snippet – 2025-07-03 20:02:16

Knowledge in GPTs
Here is what you need to know about the GPT knowledge feature
Updated over a year ago
What is Knowledge?
Using the knowledge feature in a GPT, builders can upload files containing additional context. GPTs then use a variety of methods to access this data in response to user prompts.
How does Knowledge work?
You can use the GPT editor to attach up to 20 files to a GPT. Each file can be up to 512 MB in size and can contain 2,000,000 tokens. You can include files containing images, but only the text is currently processed. When you upload a file, the GPT breaks the text up into chunks, creates embeddings (a mathematical way of representing text), and stores them for later use.
When a user interacts with your GPT, the GPT can access the uploaded files to get additional context to augment the user’s query. The GPT chooses one of the following methods based on the requirements of the user’s prompt:
Semantic search - Returns relevant text chunks as described above.
Preferred when responding to “Q&A” style prompts, where a specific portion of the source document is required.
Document review - Entire short documents and/or relevant excerpts of larger documents are returned and included along with the prompt as additional context.
Preferred when responding to summarization or translation prompts, where the entire source document is required.
When to use Knowledge
Currently, the only way to manage the files attached to a GPT is using the GPT Builder UI. This means it is best for applications where context changes infrequently (employee handbooks, policy documents, school curricula, etc).
Tips for getting the most out of Knowledge
The file parser we use to extract text from documents work best with simple formatting. A single column of text is best. The parser can struggle with multi-column PDFs, and won’t understand the nuance conveyed by the relative positions of text on a PowerPoint slide.
Using Instructions in the GPT editor, you can encourage the GPT to rely on Knowledge first before searching the internet.
By default, GPTs will avoid revealing the names of uploaded files. If you want GPTs to “cite their sources,” indicate that in the Instructions.


## Imported snippet – 2025-07-03 20:02:26

Retrieval Augmented Generation (RAG) and Semantic Search for GPTs
Learn about RAG and how it is useful to GPT builders
Updated over 3 months ago
What is Retrieval Augmented Generation (RAG), and why is it valuable for GPT builders?
Retrieval Augmented Generation (RAG) is a technique that improves a model’s responses by injecting external context into its prompt at runtime. Instead of relying solely on the model’s pre-trained knowledge, RAG retrieves relevant information from connected data sources and uses it to generate a more accurate and context-aware response.
In GPTs, RAG is performed automatically when knowledge retrieval is enabled and files have been uploaded. The model dynamically retrieves relevant information from those files to supplement the user’s prompt.
Basic RAG workflow
Why is RAG valuable?
RAG is especially helpful when your GPT needs to answer questions about content that isn’t part of its training data — such as company-specific documentation, internal processes, or recent events.
Example:
Imagine you're building a GPT to help your support team answer product questions. GPT-4 has general reasoning capabilities, but it doesn’t know your product’s latest update logs or help center content.
With RAG, your GPT can retrieve and use relevant internal support tickets or FAQs from uploaded files and respond using that custom knowledge — without you needing to hard-code every answer.
What is Semantic Search?
Semantic search is the method GPTs use to find relevant information across uploaded files. Unlike keyword search, which looks for exact word matches, semantic search finds conceptually similar content — even if the exact terms don’t match.
This is done using a vector database, where text is stored as embeddings (numerical representations of meaning). When a user asks a question, the GPT converts that question into a vector and compares it to the stored vectors, retrieving the most relevant text chunks.
Data source
Search method
Document management systems (Google Drive, Sharepoint, etc.)
Keyword search, custom query string
Relational databases (Postgres, MySQL, etc.)
SQL query
Vector databases
Semantic search query
How does GPT knowledge retrieval work?
When you upload files to a custom GPT and enable knowledge retrieval, the following happens behind the scenes:
Chunking: Files are automatically broken into smaller sections (e.g., paragraphs or logical blocks).
Embedding: Each chunk is converted into an embedding using OpenAI’s embedding models.
Storage: The embeddings are stored in OpenAI’s internal vector store.
Querying: When a user asks a question, the GPT creates a vector for the prompt and retrieves semantically similar chunks.
Response generation: The retrieved chunks are included as context in the GPT's prompt to generate a more informed answer.
You don’t need to manage a vector database manually — this all happens seamlessly within the GPT builder.
Example Use Case
If you’re building a customer support GPT, you might:
Upload your knowledge base PDFs or internal wiki content
Enable knowledge retrieval
Let the GPT semantically search those documents and return helpful, accurate answers based on them
The GPT can now answer user questions like:
“How can I reset my password?”
→ Using context from your own documentation — even if that exact question wasn’t trained into the base model.
Summary
RAG boosts response quality by incorporating real-time knowledge from your files.
Semantic search allows GPTs to retrieve conceptually relevant content, not just keywords.
GPTs with knowledge retrieval automatically use these methods — no extra setup required beyond uploading your files.


## Imported snippet – 2025-07-03 20:02:35

Why aren't my GPT links clickable?
Making Links Clickable in Your Custom GPT
Updated over 3 months ago
If your GPT is generating links that cannot be clicked, you may need to update your GPT’s instructions to use markdown syntax when creating links.
Add guidance in your GPT instructions such as:
“When generating links, format them in markdown, like: [https://www.chatgpt.com](https://www.chatgpt.com)"
This will allow your links to be clickable, such as: https://www.chatgpt.com


## Imported snippet – 2025-07-03 20:02:43

Why does my GPT not have any ratings?
Updated over a year ago
A GPT needs a minimum of 5 ratings in order for them to be displayed.


## Imported snippet – 2025-07-03 20:02:53

How do I customize my GPT's About page?
Updated over a year ago
The About page of your GPT helps users in the GPT Store more easily learn about your GPT. This will include your GPT name, profile picture, and description, as well as information like the GPT’s rating, category, capabilities, starter prompts, Builder information, and other GPTs by the same builder.
You can customize these fields in the "Configure" tab of the GPT editor and in the Builder Profile. The "Category" can be modified under the "Save" dropdown of your GPT.
Example About page for the Wolfram GPT:


## Imported snippet – 2025-07-03 20:03:01

How do I view version history?
Updated over a year ago
When collaborating on GPTs, it can be helpful to view your version history. Version history is available for all GPT Builders on Plus, Team and Enterprise subscriptions.
You can view “Version History” when editing a GPT. You’ll be able to see a log of previous versions of your GPT, from where you can copy over text or configurations from previous versions. Note that you won’t be able to see an API Key or OAuth client secret using version history. You can also revert to a previous version if needed. Note that if you revert to a previous version of your GPT, any authentication API Key or OAuth client secret will be deleted and need to be added anew.


## Imported snippet – 2025-07-03 20:03:10

Why can't I download files generated by my custom GPT?
Solving the error "Failed to get upload status" in a custom GPT
Updated over 2 months ago
Custom GPTs can be very useful for all sorts of tasks, and you may want to ask your custom GPT to generate a file such as a data analysis, creative brief, or agenda so that you can share it with others.
​
Some users find that they run into an error when they try to download a file generated by a custom GPT.
You can resolve this error by enabling the Code Interpreter & Data Analysis tool for the GPT. This will need to be done by the owner of the GPT, or anyone who has edit permissions for the GPT. With this tool enabled, the GPT will be able to generate real files for download.
