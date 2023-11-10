Welcome to Universal Profile API DOcs

[//]: # (> Introductory section - no heading)

[//]: # (>   In this section, include 1-2 sentences to briefly explain this architecture. )

[//]: # (>   The full scenario info will go in the "Scenario details" section, which is below the "Alternatives" header, and above the "Considerations" header. That includes the "Potential use cases" H3 section, which goes under the "Scenario details" section.)

[//]: # ()
[//]: # (## Architecture)

[//]: # ()
[//]: # (> Architecture diagram goes here. Use the following format:)

[//]: # ()
[//]: # (![Diagram of the <solution name> architecture.]&#40;./images/<file-name>.png&#41;)

[//]: # ()
[//]: # (> Under the architecture diagram, include this sentence and a link to the Visio file or the PowerPoint file: )

[//]: # ()
[//]: # (*Download a [Visio file]&#40;https://arch-center.azureedge.net/[file-name].vsdx&#41; of this architecture.*)

[//]: # ()
[//]: # (> Note that you must send the Visio or PowerPoint file to the AAC contact.)

[//]: # ()
[//]: # (### Dataflow)

[//]: # ()
[//]: # (> An alternate title for this sub-section is "Workflow" &#40;if data isn't really involved&#41;.)

[//]: # (> In this section, include a numbered list that annotates/describes the dataflow or workflow through the solution. Explain what each step does. Start from the user or external data source, and then follow the flow through the rest of the solution &#40;as shown in the diagram&#41;.)

[//]: # ()
[//]: # (The following workflow &#40;or dataflow&#41; corresponds to the above diagram:)

[//]: # (1. Admin 1 adds, updates, or deletes an entry in Admin 1's fork of the Microsoft 365 config file.)

[//]: # (2. Admin 1 commits and syncs the changes to Admin 1's forked repository.)

[//]: # (3. Admin 1 creates a pull request &#40;PR&#41; to merge the changes to the main repository.)

[//]: # (4. The build pipeline runs on the PR.)

[//]: # ()
[//]: # (### Components)

[//]: # ()
[//]: # (> A bullet list of components in the architecture &#40;including all relevant Azure services&#41; with links to the product service pages on Azure.com.)

[//]: # ()
[//]: # (> Why is each component there?)

[//]: # (> What does it do and why was it necessary?)

[//]: # (> Link the name of the service &#40;via embedded link&#41; to the service's product service page. Be sure to exclude the localization part of the URL &#40;such as "en-US/"&#41;.)

[//]: # ()
[//]: # (- Examples: )

[//]: # (  - [Azure App Service]&#40;https://azure.microsoft.com/services/app-service&#41;)

[//]: # (  - [Azure Bot Service]&#40;https://azure.microsoft.com/services/bot-service&#41;)

[//]: # (  - [Azure Cognitive Services Language Understanding]&#40;https://azure.microsoft.com/services/cognitive-services/language-understanding-intelligent-service&#41;)

[//]: # (  - [Azure Cognitive Services Speech Services]&#40;https://azure.microsoft.com/services/cognitive-services/speech-services&#41;)

[//]: # (  - [Azure SQL Database]&#40;https://azure.microsoft.com/services/sql-database&#41;)

[//]: # (  - [Azure Monitor]&#40;https://azure.microsoft.com/services/monitor&#41;: Application Insights is a feature of Azure Monitor.)

[//]: # (  - [Resource Groups][resource-groups] is a logical container for Azure resources.  We use resource groups to organize everything related to this project in the Azure console.)

[//]: # ()
[//]: # (### Alternatives)

[//]: # ()
[//]: # (> Use this section to talk about alternative Azure services or architectures that you might consider for this solution. Include the reasons why you might choose these alternatives.)

[//]: # ()
[//]: # (> What alternative technologies were considered and why didn't we use them?)

[//]: # ()
[//]: # (## Scenario details)

[//]: # ()
[//]: # (> This should be an explanation of the business problem and why this scenario was built to solve it.)

[//]: # (>   What prompted them to solve the problem?)

[//]: # (>   What services were used in building out this solution?)

[//]: # (>   What does this example scenario show? What are the customer's goals?)

[//]: # (> What were the benefits of implementing the solution?)

[//]: # ()
[//]: # (### Potential use cases)

[//]: # ()
[//]: # (> What industry is the customer in? Use the following industry keywords, when possible, to get the article into the proper search and filter results: retail, finance, manufacturing, healthcare, government, energy, telecommunications, education, automotive, nonprofit, game, media &#40;media and entertainment&#41;, travel &#40;includes hospitality, like restaurants&#41;, facilities &#40;includes real estate&#41;, aircraft &#40;includes aerospace and satellites&#41;, agriculture, and sports. )

[//]: # (>   Are there any other use cases or industries where this would be a fit?)

[//]: # (>   How similar or different are they to what's in this article?)

[//]: # ()
[//]: # (## Considerations)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: Include the following statement to introduce this section:)

[//]: # ()
[//]: # (These considerations implement the pillars of the Azure Well-Architected Framework, which is a set of guiding tenets that can be used to improve the quality of a workload. For more information, see [Microsoft Azure Well-Architected Framework]&#40;/azure/architecture/framework&#41;.)

[//]: # ()
[//]: # (> Are there any lessons learned from running this that would be helpful for new customers?  What went wrong when building it out?  What went right?)

[//]: # (> How do I need to think about managing, maintaining, and monitoring this long term?)

[//]: # ()
[//]: # (> REQUIREMENTS: )

[//]: # (>   You must include the "Cost optimization" section. )

[//]: # (>   You must include at least two of the other H3 sub-sections/pillars: Reliability, Security, Operational excellence, and Performance efficiency.)

[//]: # ()
[//]: # (### Reliability)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: If using this section, include the following statement to introduce the section:)

[//]: # ()
[//]: # (Reliability ensures your application can meet the commitments you make to your customers. For more information, see [Overview of the reliability pillar]&#40;/azure/architecture/framework/resiliency/overview&#41;.")

[//]: # ()
[//]: # (> This section includes resiliency and availability considerations. They can also be H4 headers in this section, if you think they should be separated.)

[//]: # (> Are there any key resiliency and reliability considerations &#40;past the typical&#41;?)

[//]: # ()
[//]: # (### Security)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: If using this section, include the following statement to introduce the section:)

[//]: # ()
[//]: # (Security provides assurances against deliberate attacks and the abuse of your valuable data and systems. For more information, see [Overview of the security pillar]&#40;/azure/architecture/framework/security/overview&#41;.)

[//]: # ()
[//]: # (> This section includes identity and data sovereignty considerations.)

[//]: # (> Are there any security considerations &#40;past the typical&#41; that I should know about this?)

[//]: # ()
[//]: # (### Cost optimization)

[//]: # ()
[//]: # (> REQUIRED: This section is required.)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: Include the following statement to introduce the section:)

[//]: # ()
[//]: # (Cost optimization is about looking at ways to reduce unnecessary expenses and improve operational efficiencies. For more information, see [Overview of the cost optimization pillar]&#40;/azure/architecture/framework/cost/overview&#41;.)

[//]: # ()
[//]: # (> How much will this cost to run? See if you can answer this without dollar amounts.)

[//]: # (> Are there ways I could save cost?)

[//]: # (> If it scales linearly, than we should break it down by cost/unit. If it does not, why?)

[//]: # (> What are the components that make up the cost?)

[//]: # (> How does scale affect the cost?)

[//]: # ()
[//]: # (> Link to the pricing calculator &#40;https://azure.microsoft.com/pricing/calculator&#41; with all of the components in the architecture included.)

[//]: # (> If it makes sense, include small/medium/large configurations. Describe what needs to be changed as you move to larger sizes.)

[//]: # ()
[//]: # (### Operational excellence)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: If using this section, include the following statement to introduce the section:)

[//]: # ()
[//]: # (Operational excellence covers the operations processes that deploy an application and keep it running in production. For more information, see [Overview of the operational excellence pillar]&#40;/azure/architecture/framework/devops/overview&#41;.)

[//]: # ()
[//]: # (> This includes DevOps, monitoring, and diagnostics considerations.)

[//]: # (> How do I need to think about operating this solution?)

[//]: # ()
[//]: # (### Performance efficiency)

[//]: # ()
[//]: # (> REQUIRED STATEMENT: If using this section, include the following statement to introduce the section:)

[//]: # ()
[//]: # (Performance efficiency is the ability of your workload to scale to meet the demands placed on it by users in an efficient manner. For more information, see [Performance efficiency pillar overview]&#40;/azure/architecture/framework/scalability/overview&#41;.)

[//]: # ()
[//]: # (> This includes scalability considerations.)

[//]: # (> Are there any key performance considerations &#40;past the typical&#41;?)

[//]: # (> Are there any size considerations around this specific solution? What scale does this work at? At what point do things break or not make sense for this architecture?)

[//]: # ()
[//]: # (## Deploy this scenario)

[//]: # ()
[//]: # (> &#40;Optional, but greatly encouraged&#41;)

[//]: # ()
[//]: # (> Is there an example deployment that can show me this in action?  What would I need to change to run this in production?)

[//]: # ()
[//]: # (## Contributors)

[//]: # ()
[//]: # (> Start with the explanation text &#40;same for every section&#41;, in italics. Then include the "Principal authors" list and the "Other contributors" list, if there are additional contributors &#40;all in plain text, not italics or bold&#41;. We include all the contributors in these lists, regardless of what company they work for. Link each contributor's name to the person's LinkedIn profile. After the name, place a pipe symbol &#40;"|"&#41; with spaces, and then enter the person's title. We don't include the person's company, MVP status, or links to additional profiles. Implement this format:)

[//]: # ()
[//]: # (*This article is maintained by Microsoft. It was originally written by the following contributors.* )

[//]: # ()
[//]: # (Principal authors: > Only the primary authors. Listed alphabetically by last name. Use this format: Fname Lname. If the article gets rewritten, keep the original authors and add in the new one&#40;s&#41;.)

[//]: # ()
[//]: # ( - [Author 1 Name]&#40;http://linkedin.com/ProfileURL&#41; | &#40;Title, such as "Cloud Solution Architect"&#41;)

[//]: # ( - [Author 2 Name]&#40;http://linkedin.com/ProfileURL&#41; | &#40;Title, such as "Cloud Solution Architect"&#41;)

[//]: # ( - > Continue for each primary author &#40;even if there are 10 of them&#41;.)

[//]: # ()
[//]: # (Other contributors: > Include contributing &#40;but not primary&#41; authors, major editors &#40;not minor edits&#41;, and technical reviewers. Listed alphabetically by last name. Use this format: Fname Lname. It's okay to add in newer contributors.)

[//]: # ()
[//]: # ( - [Contributor 1 Name]&#40;http://linkedin.com/ProfileURL&#41; | &#40;Title, such as "Cloud Solution Architect"&#41;)

[//]: # ( - [Contributor 2 Name]&#40;http://linkedin.com/ProfileURL&#41; | &#40;Title, such as "Cloud Solution Architect"&#41;)

[//]: # ( - > Continue for each additional contributor &#40;even if there are 10 of them&#41;.)

[//]: # ( )
[//]: # (*To see non-public LinkedIn profiles, sign in to LinkedIn.*)

[//]: # ()
[//]: # (## Next steps)

[//]: # ()
[//]: # (> Link to Microsoft Learn documentation and training content, along with any third-party documentation.)

[//]: # (> Where should I go next if I want to start building this?)

[//]: # (> Are there any relevant case studies or customers doing something similar?)

[//]: # (> Is there any other documentation that might be useful? Are there product documents that go into more detail on specific technologies that are not already linked?)

[//]: # ()
[//]: # (Examples:)

[//]: # (* [Azure Kubernetes Service &#40;AKS&#41; documentation]&#40;/azure/aks&#41;)

[//]: # (* [Azure Machine Learning documentation]&#40;/azure/machine-learning&#41;)

[//]: # (* [What are Azure Cognitive Services?]&#40;/azure/cognitive-services/what-are-cognitive-services&#41;)

[//]: # (* [What is Language Understanding &#40;LUIS&#41;?]&#40;/azure/cognitive-services/luis/what-is-luis&#41;)

[//]: # (* [What is the Speech service?]&#40;/azure/cognitive-services/speech-service/overview&#41;)

[//]: # (* [What is Azure Active Directory B2C?]&#40;/azure/active-directory-b2c/overview&#41;)

[//]: # (* [Introduction to Bot Framework Composer]&#40;/composer/introduction&#41;)

[//]: # (* [What is Application Insights]&#40;/azure/azure-monitor/app/app-insights-overview&#41;)

[//]: # ( )
[//]: # (## Related resources)

[//]: # ()
[//]: # (> Link to articles in the AAC repo. The links should be relative, such as &#40;../../solution-ideas/articles/<article-name>.yml&#41;.)

[//]: # ()
[//]: # (Examples:)

[//]: # (  - [Artificial intelligence &#40;AI&#41; - Architectural overview]&#40;/azure/architecture/data-guide/big-data/ai-overview&#41;)

[//]: # (  - [Choosing a Microsoft cognitive services technology]&#40;/azure/architecture/data-guide/technology-choices/cognitive-services&#41;)

[//]: # (  - [Chatbot for hotel reservations]&#40;/azure/architecture/example-scenario/ai/commerce-chatbot&#41;)

[//]: # (  - [Build an enterprise-grade conversational bot]&#40;/azure/architecture/reference-architectures/ai/conversational-bot&#41;)

[//]: # (  - [Speech-to-text conversion]&#40;/azure/architecture/reference-architectures/ai/speech-ai-ingestion&#41;)