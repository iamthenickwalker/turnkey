from crewai import Task
from textwrap import dedent
# Assuming the tools are correctly defined and available in the tools module.


class EssayWritingTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"


    def read_instructions(self, agent, instructions, draft_path=None):
        """Task for reading and understanding user instructions and any existing draft."""
        return Task(
            description=dedent(f"""

                SOP for Reading Instructions and Draft:
                1. Use the FileReadTool to read the essay instructions from: "{instructions}". This file contains the user's expectations for the essay, including the topic, specific points to cover, and formatting guidelines.
                2. Use the FileReadTool to read the draft from: "{draft_path}". The draft contains initial thoughts and content on the essay topic.
                3. Analyze the instructions first and then the draft to identify the key themes, thesis statement, main arguments, and any specific user requirements.
                4. Prepare a summary that includes:
                   - An outline of how the instructions guide the essay's development.
                   - Key themes and requirements specified by the user.
                   - Suggestions on how to incorporate or address the draft content in the expanded essay.
                5. This summary will guide the subsequent tasks in the essay writing process, ensuring that the final product aligns with the user's expectations.

                Tools used:
                - FileReadTool for reading instruction and draft documents.
                {self.__tip_section()}
            """),
            agent=agent,
            expected_output="A detailed summary document that outlines the essay structure based on the instructions and draft, highlighting key points and suggesting areas for research or clarification."
        )

    def initial_research(self, agent, topic):
        """Task for conducting initial research on the essay topic."""
        return Task(
            description=dedent(f"""
                SOP for Conducting Initial Research:
                1. Begin by defining key subtopics related to the main essay topic: "{topic}". Identify 3-5 key areas that require in-depth exploration to support the essay's thesis and main arguments.
                2. Use the SerperDevTool to conduct a broad search on each subtopic. Aim to gather a diverse range of sources, including academic journals, reputable news articles, and authoritative websites.
                3. For each subtopic, collect at least 5 sources that provide valuable insights, evidence, or perspectives. Ensure that the sources are current, credible, and relevant to the essay's focus.
                4. Summarize the key findings from each source, noting any significant facts, statistics, or expert opinions that could strengthen the essay. Pay special attention to any conflicting viewpoints or emerging trends.
                5. Organize the summarized information by subtopic, creating a structured document that clearly outlines the research findings. This document should serve as a comprehensive briefing for writing the essay, highlighting how the research supports the main arguments.
                6. Identify any gaps in the information gathered and list additional questions or subtopics that may require further research.

                Tools used:
                - SerperDevTool for conducting online searches.
                - Optionally, use the ScrapeWebsiteTool for extracting specific information from web pages if detailed analysis is needed.

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent(f"""
            A well-organized research document that compiles key findings from various sources, categorized by subtopic, with summaries that highlight their relevance to the essay topic. The document should also list any areas needing further research, guiding the next steps in the essay writing process.
        """)
        )
    def create_new_essay_document(self, agent, essay_title):
        """Task for creating a new essay document."""
        # Format the title to a valid filename (e.g., replace spaces with underscores and remove special characters)
        filename = essay_title.replace(" ", "_") + ".txt"
        filepath = f"/Users/q/Downloads/Essay/{filename}"
        
        return Task(
            description=dedent(f"""
                SOP for Creating a New Essay Document:
                1. Use the ShellTool to execute a command that creates a new text file for the essay at the specified path.
                2. The new file will be named based on the essay title provided, with spaces replaced by underscores and appended with '.txt'.
                3. Ensure the file is created in the directory '/Users/q/Downloads/Essay/'.
                
                Command to execute:
                touch "{filepath}"
                
                Expected Output:
                A new text file named '{filename}' located in '/Users/q/Downloads/Essay/'. This file will be used to write and save the essay content.
            """),
            agent=agent,
            expected_output=f"A new document created at {filepath}"
        )
    
    def expand_essay(self, agent, draft_path, research_summary):
        """Task for expanding the essay based on initial research and any provided draft."""
        return Task(
            description=dedent(f"""
                Use the initial research summary and any provided draft to expand the essay. Ensure the expansion 
                incorporates the research findings effectively and fills in any identified gaps. Follow the structure 
                outlined in the user instructions and improve upon the draft where applicable.
                
                The expanded essay MUST:
                               
                SOP for Expanding the Essay:
                               
                1. Start by reviewing the initial draft located at "{draft_path}". Identify the thesis statement, main arguments, and the overall structure of the essay to understand the foundation upon which you'll build.
                2. Read through the research summary document provided in the "{research_summary}". This document contains key findings from the initial research task, including facts, statistics, expert opinions, and potentially useful quotes.
                3. Based on the research summary, identify areas within the draft that can be strengthened or expanded. Look for opportunities to incorporate new evidence, support existing arguments, or introduce new subtopics that align with the essay's main theme.
                4. Draft additional paragraphs or sections that seamlessly integrate with the existing content. Ensure each new addition enhances the essay's coherence, supports the thesis, and adheres to the user's instructions and formatting guidelines.
                5. Revise the draft to improve transitions between sections, ensuring the essay flows logically from introduction to conclusion. Pay special attention to maintaining a consistent tone and voice throughout.
                6. Throughout the expansion process, use the FileReadTool to reference the original draft and research summary as needed. Additionally, consider using the ShellTool for text manipulation tasks that can automate parts of the editing process.
                
                Tools used:
                - FileReadTool for accessing the draft and research summary documents.
                - ShellTool for automated text manipulation and formatting tasks (optional).

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent(f"""
            An expanded essay draft that incorporates research findings to strengthen arguments and enhance content. The revised draft should be coherent, logically structured, and aligned with the user's instructions and formatting preferences. Include a brief report outlining the major additions and revisions made to the draft.
        """)
        )

    def finalize_formatting(self, agent, expanded_draft, formatting_style):
        """Task for applying final formatting and compiling the Works Cited page."""
        return Task(
            description=dedent(f"""
                SOP for Finalizing Essay Formatting:
                
                1. Start by reviewing the expanded draft located at "{expanded_draft}". This draft contains the content of the essay post-expansion and requires formatting adjustments.
                2. Apply the "{formatting_style}" formatting style to the document. This includes setting the correct font type and size, margin sizes, spacing, paragraph indentation, and heading styles as per the style guide.
                3. Ensure that all citations within the text are formatted correctly according to the "{formatting_style}" guidelines. Pay special attention to in-text citations and the formatting of the reference list or bibliography at the end of the document.
                4. Add page numbers, a running head (if required by the style guide), and ensure that any figures, tables, or appendices are appropriately labeled and formatted.
                5. Use the ShellTool to automate any part of the formatting process that can be standardized, such as replacing tabs with spaces for indentation or adding headers and footers.
                
                Tools used:
                - ShellTool for automated formatting adjustments (ensure your implementation supports the required operations).
                
                {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent(f"""
            A finalized essay document that:
            - Strictly adheres to the formatting guidelines of the specified style guide, with all citations correctly formatted.
            - Includes a detailed Works Cited or References page that accurately reflects all sources cited within the essay.
            - Has been thoroughly proofread to ensure grammatical correctness, punctuation accuracy, and overall coherence.
            - Is ready for submission, meeting all specified requirements and quality standards.
        """)
        )

    def proofread_essay(self, agent, expanded_draft):
        """Task for proofreading the essay to correct grammatical errors and improve coherence."""
        return Task(
            description=dedent(f"""
                SOP for Proofreading the Essay:
                1. Begin by using the FileReadTool to open the expanded essay document located at "{expanded_draft}". This document contains the essay's latest draft, which has already incorporated research findings and addressed initial feedback.
                2. Carefully read through the entire document, focusing first on identifying and correcting any grammatical errors, spelling mistakes, and punctuation issues. Use tools like Grammarly or similar if available and integrated into your workflow.
                3. Next, assess the essay for coherence and logical flow. Ensure that each paragraph transitions smoothly to the next and that the essay as a whole supports the thesis statement effectively. Reorganize content if necessary to improve the essay's clarity and readability.
                4. Verify adherence to the specified formatting guidelines (e.g., MLA, APA). Check for correct citation formatting, proper use of headings and subheadings, and consistency in font and spacing. Use the ShellTool or a dedicated formatting tool if available to automate parts of this process.
                5. Conclude by preparing a brief report summarizing the changes made during the proofreading process. Highlight any major grammatical corrections, structural adjustments, or formatting improvements. If further revisions are needed, outline these recommendations for the next steps.
                
                Tools used:
                - FileReadTool for accessing the expanded essay document.
                - Grammarly or similar for grammatical corrections (if integrated).
                - ShellTool for automated formatting tasks (optional).

                {self.__tip_section()}
            """),
            agent=agent,
            expected_output=dedent(f"""
            A thoroughly proofread essay that is free from grammatical and spelling errors, exhibits a clear and logical structure, and adheres to the specified formatting guidelines. Include a proofreading report detailing the revisions made and any further recommendations.
        """)
        )
    
    def write_to_files(self, agent, file_path, content):
        """Task for writing content to a file using ShellTool."""
    # This presumes a secure implementation of ShellTool capable of safely handling file writes.
        return Task(
            description=dedent(f"""
                SOP for Writing Content to a File:
                1. Prepare the content to be written to the file located at "{file_path}".
                2. Use the ShellTool to safely execute the command to write the content to the specified file.
                3. Verify the content has been correctly written to the file and handle any errors encountered during the process.
            
            Command to execute:
            echo "{content}" > {file_path}
            
            Note: Ensure ShellTool sanitizes input to prevent command injection.
            
            Expected Output:
            Content successfully written to "{file_path}", ready for further processing or review.

            {self.__tip_section()}
        """),
        agent=agent,
        expected_output=f"Content written to {file_path}"
    )



    # Include any other tasks as necessary for ensuring the essay's quality and completeness.
