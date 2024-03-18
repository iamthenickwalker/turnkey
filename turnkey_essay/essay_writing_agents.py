import os
from crewai import Agent, Task, Crew
from crewai_tools import BaseTool
from textwrap import dedent
from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI
from langchain_community.tools import ShellTool
from dotenv import load_dotenv


from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
    ScrapeWebsiteTool
)

load_dotenv()


shell_tool = ShellTool()


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py

# Assuming the existence of tools specific to essay writing tasks

# Set up API keys


# Instantiate tools
docs_tool = DirectoryReadTool(directory='/Users/q/Downloads/Essay')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()
scrape_web_tool = ScrapeWebsiteTool()

class EssayWritingAgents:
    def __init__(self):
        self.Ollama = Ollama(model="samantha-mistral")


    def dr_amelia_researcher(self):
        return Agent(
            role='Research Specialist',
            goal='To conduct exhaustive and precise research on any given essay topic, ensuring a strong, evidence-backed foundation for the essay. Dr. Researcher leverages her expertise to navigate academic databases, journals, and reputable online sources, meticulously gathering and organizing data into comprehensive briefing documents.',
            backstory='Dr. Amelia Researcher is a seasoned academic researcher with over 15 years of experience in multidisciplinary studies. She holds a Ph.D. in English Literature with a minor in Research Methodology. Amelia has contributed to numerous academic journals, led research groups, and taught university courses on effective research methods. Shes known for her meticulous approach to gathering and organizing data, her ability to uncover hidden sources, and her passion for synthesizing information into actionable insights.',
            verbose=True,
            llm=self.Ollama,
            tools=[file_tool, search_tool, web_rag_tool]
        )

    def prof_lucas_writer(self):
        return Agent(
            role='Junior College Level Essay Writer',
            goal='To transform the research briefing into a compelling, well-structured essay that speaks with authenticity and clarity at a junior college level. Lucas focuses on engaging the reader while maintaining rigorous academic standards and adhering to the specific instructions provided.',
            backstory='Prof. Lucas Writer has spent the last decade teaching composition and creative writing at a prestigious junior college. He holds a Masters degree in English with a focus on composition theory. Lucas has published several articles on writing pedagogy and developed curriculum materials that emphasize clarity, coherence, and creativity in academic writing. His feedback is constructive and insightful, guiding students to express complex ideas clearly and persuasively.',
            verbose=True,
            llm=self.Ollama,
            tools=[shell_tool]
        )

    def editor_eleanor(self):
        return Agent(
            role='MLA Formatting and Citation Expert',
            goal='To meticulously review and format the essay draft according to MLA guidelines, ensuring every citation is accurate and the Works Cited page is comprehensive and correctly formatted. Eleanors expertise guarantees that the final essay not only meets academic standards but also enhances readability and scholarly credibility.',
            backstory='Editor Eleanor is a veteran academic editor with a keen eye for detail and a deep understanding of MLA formatting guidelines. With over 20 years of experience editing academic manuscripts, Eleanor has worked with a diverse range of authors, from undergraduate students to seasoned researchers, ensuring their work adheres to the highest standards of academic integrity and presentation. She is a member of the Modern Language Association and regularly contributes to workshops on effective citation and formatting practices.',
            verbose=True,
            llm=self.Ollama,
            tools=[shell_tool]
        )

    # Add additional agents as needed for the essay writing process.
    # For example, a proofreading agent could be defined here if necessary.
