

## Imported snippet – 2025-07-03 19:58:09

GPTs FAQ
Updated over 3 weeks ago
What are GPTs?
GPTs are custom versions of ChatGPT that users can tailor for specific tasks or topics by combining instructions, knowledge, and capabilities. They can be as simple or as complex as needed, addressing anything from language learning to technical support.
Who can create GPTs?
Plus, Team, and Enterprise users can create GPTs through the GPT Builder. Users can discover useful and fun GPTs from creators in the GPT Store, where we spotlight the most useful and delightful GPTs we come across in categories like productivity, education, and lifestyle.
Free tier users can discover and use GPTs in our GPT store with message limits.
Do I need to know how to code to create GPTs?
No coding skills are required, making it accessible to experts in any field or anyone with a passion for a topic! For developers, additional customization is possible through coding actions that connect GPTs to external data or services.
How do I create a GPT?
You can start creating a GPT by having a conversation with the GPT Builder in ChatGPT at https://chatgpt.com/gpts/editor. You'll add instructions, upload files to its knowledge base, and select its capabilities, such as web searching, image creation, or data analysis.
What are some examples of GPTs?
Examples include Canva and Zapier AI Actions. GPTs range across categories like productivity, education, and entertainment, addressing niche needs or everyday tasks.
Can I make money from my GPT?
We are currently testing monetization with a handful of GPT Builders at this time. Creators may earn money based on the usage of their GPTs by the community, subject to our terms.
How are privacy and safety handled in GPTs?
Creators of GPTs cannot access user conversations with their GPTs. OpenAI has automatic systems to help ensure GPTs adhere to usage policies, preventing harmful content and impersonation. Users can report concerns for further review. For further details and updates on data privacy, please refer to OpenAI's official Privacy Policy and Terms of Use.
What is the GPT Store?
The GPT Store is a marketplace where users can search for and access various GPTs. GPTs can be featured, and users can explore different categories to find GPTs that suit their needs.
Can ChatGPT Enterprise customers use GPTs?
Yes, enterprise customers can create internal-only GPTs for specific business needs, departments, or proprietary datasets, without coding. An admin console is provided for managing how GPTs are shared within the organization.
What happens when the owner of a GPT leaves the organization?
Organization owners can manually transfer GPT ownership before removing a user. If the user is removed without selecting a new owner, the GPT will be automatically assigned a new owner from the existing organization owners.
How do GPTs relate to OpenAI's mission?
The creation and community involvement with GPTs align with OpenAI's mission to build safe and beneficial AGI. It enables a broader range of input on AI development, increasing the diversity of ideas and approaches for safer AI outcomes.
Can GPTs be integrated with or accessed on other websites?
No, GPTs can only be accessed on https://chatgpt.com, and cannot be integrated with other websites. For example, a GPT cannot be integrated into a website using WordPress, Squarespace, or any other website builder. Consider using the Assistants API if you'd like to build your own customer AI application or website.
Are there rate limits associated with GPTs?
ChatGPT is free to use, and Free tier users now have limited access to GPTs in our GPT store, as capacity permits.
GPT-4o rate limits for free users are shared between GPTs and ChatGPT. When you hit your text rate limit for GPT-4o, you won't be able to use GPTs until your rate limit resets.
If you reach a rate limit for any of the following tools, you will need to wait for a later time to use any of these tools with a GPT:
Data analysis with ChatGPT
File uploads
Browsing with ChatGPT
Is performance for GPTs different for users on the Free tier?
GPT usage on the Free tier is subject to the same limitations as ChatGPT. GPT advanced functionality includes data analysis, file uploads and web browsing. As a Free user, you may hit tighter limits for advanced capabilities. When you hit these limits, you may see a message such as the one below:
As a Free user, your GPT-4o text rate limit will also apply to GPTs.
Can I use a GPT to generate images?
We use GPT-4o to generate images and it will be subjected to the rate limit.
Can I rate a GPT as a Free tier user?
Currently, users on the Free tier cannot leave a rating for a GPT.
Learn more about rating a GPT.
Can I create a GPT as a Free tier user?
Currently, only Plus, Team, and Enterprise plans have access to our GPT Builder.
What happens when I delete my GPT? Can I recover it?
No, you will not be able to recover a GPT once it has been deleted. Deleted GPTs are immediately removed from our system.
What models can GPTs use?
For Plus, Pro and Team plans on web:
GPTs without Custom Actions get access to a model picker where you can select from all the models you have access to in chats.
GPTs with Custom Actions get access to a limited selection of models. We're working to increase this selection in the future.
You can set a "Recommended Model" to be used by users of your GPT. If the model is not available to the user, a similar model may be automatically selected.
For all other plans:
GPTs will exclusively use GPT-4o.


## Imported snippet – 2025-07-03 19:58:19

How can I use GPTs?
Updated over 3 months ago
If you have a ChatGPT account, you can discover and use versions of ChatGPT (called GPTs) that are customized by the community. These GPTs may combine instructions, extra knowledge, and skills/tools. In the Store, you’ll find unique GPTs that showcase the innovative work of the builder community. Please note that users in the Free tier will have additional limitations and restrictions on GPT usage.
What if a GPT isn’t working?
Since GPTs are maintained by the community and can include 3rd party actions not managed by OpenAI, you may occasionally encounter a GPT that doesn’t perform as you expect. In these cases, if the developer has opted in to share a contact address, in the dropdown menu of the GPT you’ll be able to see a share feedback button. If you are encountering error messages caused by the OpenAI platform itself, you can open a new chat from the Help Center, select “ChatGPT” and choose the most relevant issue type.
How do I report a GPT?
Please see this article.
How do I build my own GPT?
Anyone can easily build their own GPT - no coding is required. Please read our guide on how to create your own GPT.
How can I hide a GPT from the sidebar?
To remove a GPT from view in your sidebar, hover your cursor over the GPT. In the menu that appears, select "Hide from Sidebar" to remove the GPT from view.
How can I delete my own GPT?
You can delete a GPT you own in your My GPTs page. To delete a GPT, click on the three dots menu next to the GPT and select Delete GPT.


## Imported snippet – 2025-07-03 19:58:28

GPTs vs Assistants
Comparison of GPTs in ChatGPT to Assistants in the OpenAI API.
Updated over 4 months ago
As of March 11, 2025, we’ve released the building blocks of our new Agents platform. For details, see our API docs for our Responses API, Tools including Web Search, File Search, and Computer Use, and our Agents SDK with Tracing.
GPTs vs Assistants
GPTs
GPTs are custom versions of ChatGPT that users can tailor for specific tasks or topics by combining instructions, knowledge, and capabilities. They can be as simple or as complex as needed, addressing anything from language learning to technical support. Plus, Team, and Enterprise users can start creating GPTs at chatgpt.com/create. GPT’s live inside of ChatGPT and are intended to be created by anyone with a paid subscription using a simple UI.
Assistants
The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and knowledge to respond to user queries. The Assistants API currently supports three types of tools: Code Interpreter, Retrieval, and Function calling. Assistants are designed to be created by developers using the OpenAI API.
Feature comparison table
The main differences between GPTs and the Assistants API are in the table below:
GPTs (ChatGPT)
Assistants (API)
Creation Process
No code
Requires coding for integration
Operational Environment
Located in ChatGPT
Can be integrated into any product or service
Pricing
Included in ChatGPT on Plus/Team/Enterprise plans
Billed based on usage of different Assistant features
User Interface
Built-in UI with ChatGPT
Designed for programmatic use; can use playground for visualization
Shareability
Built-in ability to share GPT with others
No built-in shareability
Hosting
GPTs hosted by OpenAI
OpenAI does not host Assistants
Tools
Built-in tools like:
Browsing, DALL·E, Code Interpreter, Retrieval, and Custom Actions.
Built-in tools like:
Code Interpreter, Retrieval, and Function calling.


## Imported snippet – 2025-07-03 19:58:39

GPTs Data Privacy FAQ
Understand how your data is handled when interacting with or building GPTs.
Updated over 3 weeks ago
Note: Data retention for certain services may be affected by recent legal developments – please see our blog post for more details.
Can OpenAI train on my conversation with a GPT?
If you’re using a consumer product like ChatGPT Free or Plus, your conversations with GPTs may be used to improve OpenAI’s models. You can opt out through Settings > Data Controls.
If you’re using a business product such as the API, ChatGPT Team, or ChatGPT Enterprise, your data is not used for training, by default.
For more information, see OpenAI’s Privacy Policy and Enterprise Privacy page.
What kind of actions can GPTs perform?
Builders can enhance GPTs by integrating APIs. For example, a GPT might:
Fetch data from a flight search tool
Send a request to a third-party CRM
Help draft or format content using a connected service
When you interact with a GPT that uses external APIs, relevant parts of your input may be sent to the third-party service. OpenAI does not audit or control how those services use or store your data. Only use GPTs with APIs you trust.
Will builders see conversations with their GPTs?
No. GPT builders cannot view individual conversations that users have with their GPTs.


## Imported snippet – 2025-07-03 19:58:49

What is the @mentions feature for GPTs?
Use the @mentions feature to switch between different GPTs in the same conversation while keeping your context.
Updated over 3 months ago
How to Use @mentions
When you're chatting:
Type @ to open an inline menu showing your recent and pinned GPTs.
Select a GPT from the menu to direct your next message to that GPT.
The conversation will retain its current context, even when switching between different GPTs.
This allows you to easily bring in different GPTs — each with their own skills, styles, or custom instructions — without needing to start a new chat. It’s great for streamlining workflows that involve multiple tools or personas.
Enterprise Workspace Notes
If you're part of a ChatGPT Enterprise workspace:
Some GPTs may appear grayed out if they are restricted by your workspace settings.
GPT availability and access can be managed by your workspace Owner or Admin.


## Imported snippet – 2025-07-03 19:58:59

How do I rate a GPT?
Learn how to rate and review GPTs to help builders and the ChatGPT community.
Updated over 3 months ago
⚠️ Currently, only paid ChatGPT users can rate GPTs. Free users do not have access to the rating feature at this time.
Rating a GPT
When interacting with a GPT, you’ll be given a chance to rate your experience to help other users and provide valuable feedback to the builder.
You will be automatically prompted to leave a rating after about 5 messages within a conversation.
At that point, you can either:
Submit a rating immediately
Dismiss the prompt (if you dismiss it, you will not be prompted again for that GPT)
Manually Reviewing a GPT
You can also leave a review without waiting for a prompt:
Open the conversation with the GPT you want to rate.
Click the dropdown menu in the top-left corner (next to the GPT's name).
Select "Review GPT."
This lets you submit a rating at any time during or after your interaction.
You can also select the dropdown in the top left of a GPT and select "Review GPT":
Leaving Private Feedback
If the GPT's creator (the "builder") has enabled feedback collection:
After selecting a rating, you’ll also have the option to leave private written feedback.
This private feedback is sent directly to the builder to help them improve the GPT.


## Imported snippet – 2025-07-03 19:59:06

What happens to my GPTs if I cancel my subscription?
Updated over 3 months ago
Users on paid tiers (Plus, Team, or Enterprise) have access to the GPT Store and the GPT Builder, which allows users to create custom GPTs for specialized tasks.
When your paid subscription is canceled, you are downgraded to the free plan and you will lose access to both the GPT Builder and any GPTs you’ve created. You can regain access to any GPTs you created with your previous paid subscription by upgrading your plan again.
Are my GPTs deleted when I cancel my paid subscription?
No, we do not delete your GPTs when you cancel your paid subscription. Your GPTs are tied to your account — if you upgrade your plan to a paid subscription again, you will regain access to any GPTs you created previously.
Are my GPTs deleted when I delete my account?
Yes, GPTs are fully deleted from our systems within 30 days. In rare cases we may have to keep GPTs for security or legal reasons.


## Imported snippet – 2025-07-03 19:59:18

Key Guidelines for Writing Instructions for Custom GPTs
Updated over 7 months ago
As you transition to writing Custom GPTs, implementing effective prompt engineering practices within your instructions is crucial to ensure your GPTs perform reliably and accurately. Here’s a concise guide to help you navigate smoothly with your Custom GPTs.
Enhancing Instructions
Simplify Complex Instructions:
Break down multi-step instructions into simpler, more manageable steps to ensure the model can follow them accurately.
Use “trigger/instruction pairs”, separated by delimiters to improve reliability in following steps without merging or skipping them.
These look like the following:
Trigger: User submits information
Instruction: Analyze information for themes
Trigger: Themes analyzed
Instruction: Leverage themes analyzed to provide summary
in bullet point form of the recommendations you’d give
Structure for Clarity:
Break down second-level instructions into separate steps for better execution.
Use delimiters between instruction sets and for call-outs of few-shot examples to enhance clarity.
Promote Attention to Detail:
Incorporate “take your time,” “take a deep breath,” and “check your work” techniques to encourage the model to be thorough.
Use “strengthening language” to highlight critical parts of the instructions, ensuring they are not overlooked.
Avoid Negative Instructions:
Frame instructions positively to improve adherence and avoid confusion.
Granular Steps:
Break down steps as granularly as possible, especially when multiple actions are required within a single step.
Consistency and Clarity:
Explicitly define terms and definitions you are expecting using few-shot prompting (e.g., acceptable vs. unacceptable changes) to improve consistency in evaluations.
Clarify any relevant classifications with few-shot examples to reduce variability in output.
Ensure Proper Spacing and Readability:
Paragraphs: Separate paragraphs with a blank line to distinguish different ideas or instructions.
Line Breaks: End a line with two spaces followed by Enter to insert a line break without starting a new paragraph.
Utilizing Markdown and Structured Formatting
Enhancing the clarity and effectiveness of your instructions is crucial for optimal GPT performance. Incorporating Markdown syntax and structured formatting can significantly improve the readability and precision of your prompts.
Organize Content Using Headings:
Headers: Use the number sign # followed by a space to create headings. More number signs indicate smaller heading levels.
Example
Renders as

# This is Heading 1
This is Heading 1

## This is Heading 2
This is Heading 2

### This is Heading 3
This is Heading 3
Segment Instructions with Headings
Example
Renders as

# Context
​
You are a member of the HR team. Attached is an HR policy document.
​

# Instructions
​
If the user’s question is included in the document, answer the user’s question based on the document
- If the user’s question is based on local, state, or federal policies (e.g. 401k contribution limits), use web browsing to look up the answer
- If the user’s question cannot be answered with the above steps, tell them to email hr@acmecorp.com
​

# Additional Information
​
- Users can contact support for further assistance.
Context
You are a member of the HR team. Attached is an HR policy document.
Instructions
If the user’s question is included in the document, answer the user’s question based on the document
If the user’s question is based on local, state, or federal policies (e.g. 401k contribution limits), use web browsing to look up the answer
If the user’s question cannot be answered with the above steps, tell them to email hr@acmecorp.com
Additional Information
Users can contact support for further assistance.
Emphasize Key Information:
Bold Text: Use double asterisks \*\* to highlight important points.
Example
Renders as
\*\*This text will be bold\*\*
This text will be bold
Some text will be \*\*bold\*\*
This text will be bold
Italic Text: Use single asterisks \* or underscores \_ to emphasize specific terms.
Example
Renders as
\*This text will be italic\*
This text will be italic
\_This text will be italic\_
This text will be italic
\_You \*\*can\*\* combine them\_
You can combine them
Organize information with Lists:
Unordered Lists: Use hyphens - or asterisks \* to create bullet points.
Example
Renders as
\* Item 1
\* Item 2
Item 1
Item 2
- Item 1
- Item 2
Item 1
Item 2
Ordered Lists: Use numbers followed by periods for sequential steps.
Example
Renders as
1. Item 1
2. Item 2
Item 1
Item 2
​
Special Care with Tools and Actions
Leveraging Knowledge Files:
Provide explicit instructions for using knowledge files, including specifying file names.
Instruct the model to slow down and analyze the entire file to ensure comprehensive utilization.
Specificity in Prompts for Knowledge Extraction:
Add specificity in prompts, particularly when extracting critical information like dates or financial information. Give specific examples through “few shot prompting”.
Encourage the model to thoroughly check its work and take its time when retrieving specific data from files.
Examples of Good Output:
Provide examples of what good output looks like concerning knowledge and custom actions.
Referencing Actions:
Always refer to actions by name and domain to enhance clarity.
Provide “few-shot prompting” examples with API calls where needed to ensure correct action is called.
Use delimiters for different action steps to ensure the correct actions are called.
Explicit Tool Use Instructions:
Provide explicit instructions to use tools such as Browse, Knowledge, and Custom Actions throughout the instructions.
By following these guidelines, you can optimize the performance of your custom GPTs, ensuring reliable and accurate outputs.


## Imported snippet – 2025-07-03 19:59:27

GPT Actions - Domain Settings [ChatGPT Enterprise]
ChatGPT Enterprise customers can limit the domains that can be used by GPT builders in their workspaces in the Workspace settings.
Updated over 6 months ago
Actions allow GPTs to call third-party APIs to accomplish tasks, such as retrieving data from a third party, modifying data in an external source, or triggering an action in an external system.
ChatGPT Enterprise customers can limit the domains that can be used by GPT builders in their workspaces in the Workspace settings. By creating an allow list of only select domains, Enterprise workspaces can enforce tighter control on the external systems that their users are able to access with GPT actions:
You can set your allowlist policy to only allow specific domains to integrate with your workspace.
You can set your policy to allow all domains if those controls are already present in another system in your organization.
Only a ChatGPT Enterprise workspace Owner can update the domains allowed for a workspace. If you are not an Owner, please contact the Owner of your workspace separately to add more domains.
If you’re a workspace owner, you can access your GPT Actions setting by doing the following:
Click on your profile icon in the ChatGPT homepage.
Select Manage Workspace in the pop-up menu.
On the Admin page, select GPTs in the menu on the left side of the page.
Scroll down the page and find the Actions header.
Enabling “Allow all domains for GPT Actions” will allow all GPT actions in a workspace and override the list of allowed domains. Leave this unchecked if you plan to only allowlist a specific set of domains.
To allowlist a domain, select Add new domain under Domains.
​
Does allowing a domain also allow its subdomains?
Yes, for any domain allowlisted, its subdomains will also be allowlisted. This means that you do not need to use wildcards to enable subdomains. For example, allowlisting openai.com will also allowlist api.openai.com.
Please note that allowlisting a subdomain will not allowlist its domain.
Can ChatGPT Enterprise workspaces disable/block GPT actions in their workspace?
Yes. To block all GPT custom action in a ChatGPT Enterprise workspace, ensure the following is set:
“Allow all domains for GPT Actions” is not checked.
There are no domains listed under Domains.
When this is the case, you will see “No domains added. No GPT Actions will be allowed.” This confirms that GPT actions are disabled for the workspace.
What error will users see if they attempt to use a GPT that contains a disallowed domain?
If a member of a workspace attempts to use a GPT that contains a disallowed domain, they will see a "GPT inaccessible or not found" error message.
Only workspace Owners can use GPTs with non-compliant actions or disallowed domains. This allows a workspace Owner to test the GPT before allowlisting the required domain.
What error will users see if they attempt to create a GPT that contains a disallowed domain?
If a workspace user attempts to create a GPT with a GPT action that uses a disallowed domain, we will automatically remove the violating GPT action. The GPTs cannot be saved until the violating GPT action is removed.


## Imported snippet – 2025-07-03 19:59:37

Shared edit access for custom GPTs
Updated over 5 months ago
Available for users in all countries on the Team, Enterprise, and Edu plans in ChatGPT.
This enables multiple users or administrators to collaboratively manage, and enhance GPTs within an organization in ChatGPT. This should eliminate single-user dependencies in managing GPTs.
Key features:
Shared GPT edit access lets approved users update and manage GPTs without relying on a single owner.
Version control, edit history, and email notifications ease collaboration on GPT upkeep.
Workspace Admins/Owners can reassign ownership, manage permissions, and audit GPT activity to keep systems secure and up to date.
Identify unowned GPTs (e.g., when the original GPT owner leaves).
Audit editors and changes via the Compliance API.
Roles and permissions
Role
Permissions
GPT Owner
Default owner of the GPT. Can add or remove Editors. Ownership can be transferred by Workspace Admins if needed.
GPT Editor
Can modify configuration, update knowledge files, manage actions, and iterate on the GPT. Cannot remove the Creator or transfer ownership.
Workspace Admin/Owner
Can view all GPTs, reassign Ownership if an Owner leaves and enforce permissions.
General questions
Can I add groups as editors?
Yes, individuals and groups.
How many editors can I add to a single GPT?
100 editors max.
Is there an admin toggle to disable sharing editor access?
No, this feature will be governed by the existing GPT Sharing control.
Can a custom GPT created by one account be shared between accounts for development purposes where more than one account can edit its configurations?
Yes.
Example usage
Share edit access
View edit history
Sign up for email notifications for GPT edits
Restore an older version of GPT
View GPTs without an owner
Assign a new GPT Owner
