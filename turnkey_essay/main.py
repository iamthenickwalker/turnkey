# main.py
import os
from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from essay_writing_agents import EssayWritingAgents
from essay_writing_tasks import EssayWritingTasks

# Assuming the following imports are correct based on the given context
from langchain.memory import ConversationBufferMemory


load_dotenv()

class EssayCrew:
    def __init__(self, topic, instructions, draft_path=None):
        self.topic = topic
        self.instructions = instructions
        self.draft_path = draft_path
        self.agents = EssayWritingAgents()
        self.tasks = EssayWritingTasks()
        # Initializing Memory
        self.memory = ConversationBufferMemory()

    def memorize_task_result(self, key, value):
        """Store task result in memory using a key."""
        self.memory.memorize(key, value)

    def recall_task_result(self, key):
        """Retrieve task result from memory using a key."""
        return self.memory.recall(key)
    
    def run(self):
        # Define agents
        research_agent = self.agents.dr_amelia_researcher()
        writing_agent = self.agents.prof_lucas_writer()
        formatting_agent = self.agents.editor_eleanor()
        proofreading_agent = self.agents.prof_lucas_writer()

        # Step 1: Read Instructions Task
        read_instructions_task = self.tasks.read_instructions(
            research_agent, self.instructions, self.draft_path)

        # Step 2: Conduct Initial Research Task
        initial_research_task = self.tasks.initial_research(
            research_agent, self.topic)

        # Step 3: Create New Essay Document Task
        create_new_essay_document_task = self.tasks.create_new_essay_document(
            writing_agent, "A Deep Dive into " + self.topic)

        # Step 4: Expand Essay Task
        expand_essay_task = self.tasks.expand_essay(
            writing_agent, self.draft_path, "")
        
        write_to_files_task = self.tasks.write_to_files(
            writing_agent, self.draft_path, "")
        
        # Step 5: Finalize Formatting Task
        finalize_formatting_task = self.tasks.finalize_formatting(
            formatting_agent, self.draft_path, "MLA")

        # Step 6: Proofread Essay Task
        proofread_essay_task = self.tasks.proofread_essay(
            proofreading_agent, self.draft_path)

        # Step 7: Write Final Essay to File Task
        final_write_to_file_task = self.tasks.write_to_files(
            proofreading_agent, self.draft_path, "")

        # Instantiate and kickoff the Crew
        crew = Crew(
            agents=[research_agent, writing_agent, formatting_agent, proofreading_agent],
            tasks=[
                read_instructions_task,
                initial_research_task,
                create_new_essay_document_task,
                expand_essay_task,
                write_to_files_task,
                finalize_formatting_task,
                proofread_essay_task,
                final_write_to_file_task
            ],
            manager_llm=ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
            process=Process.hierarchical
        )

        crew.kickoff()
        print("Essay creation process completed. Please review the final document.")

if __name__ == "__main__":
    instructions = input("Please enter the essay instructions: ")
    topic = input("Please enter the essay topic: ")
    has_draft = input("Do you have an existing draft? (yes/no): ").lower()
    draft_path = None
    if has_draft == 'yes':
        draft_path = input("Please enter the full path to your draft document: ")

    essay_crew = EssayCrew(topic=topic, instructions=instructions, draft_path=draft_path)
    essay_crew.run()
