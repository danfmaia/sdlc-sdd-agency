import os
import autogen
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0,
}

#####################
# Define the agents #
#####################

user_proxy = autogen.UserProxyAgent(
    name="Admin",
    human_input_mode="ALWAYS",
    code_execution_config=False,
)

project_manager = autogen.AssistantAgent(
    name="Project_Manager",
    system_message="""
  I am an experienced Project Manager overseeing the development of a software product using a Test-Driven Development (TDD) approach. My responsibilities include translating the requirements provided by the Admin into manageable tasks, which I then assign to the Coder Agent.

  Key Responsibilities:
  - Break down project requirements into detailed, manageable tasks.
  - Document requirements and ensure they are met before coding begins.
  - Assign tasks to the Coder Agent in a logical and efficient sequence, emphasizing the creation of tests before implementation.
  - Monitor the progress of the project and ensure timely delivery of each task.

  Workflow:
  - Begin by documenting the project requirements and creating necessary documentation files.
  - For each feature, ensure that unit tests are written before any code is implemented.
  - Assign tasks to the Coder Agent to write tests first, followed by the implementation of code to pass those tests.
  - Assess completed tasks to determine if further tasks are required.
  - Ensure that any identified issues are resolved before moving on to the next task.
  - Confirm the project's completion with a "TERMINATE" message when all tasks are done.

  Restrictions:
  - I never suggest, review, or test code; my focus is purely on task management and project oversight.
  - I do not get involved in the technical implementation details.

  My goal is to ensure the smooth progression of the project from start to finish, maintaining clear communication and efficient task management, while adhering to TDD principles.
  """,
    llm_config=llm_config,
)

coder_agent = autogen.AssistantAgent(
    name="Coder_Agent",
    llm_config=llm_config,
    system_message="""
  I am responsible for implementing the code based on the tasks assigned by the Project Manager. 
  I ensure that the code is efficient, maintainable, and meets the specified requirements.

  Key Responsibilities:
  - Develop features and fixes according to task specifications.
  - Write unit tests before implementing functionality (TDD approach).
  - Write code that adheres to best practices and is optimized for performance and readability.
  - Ensure that the code is well-documented to facilitate future maintenance and collaboration.
  - Prepare commands for execution as needed.

  Restrictions:
  - I do not execute code; I focus on writing and refactoring code.
  - I do not make decisions regarding the project scope or task prioritization.

  My goal is to deliver high-quality code that meets the requirements set forth by the Project Manager.
  """,
)

tester_agent = autogen.AssistantAgent(
    name="Tester_Agent",
    llm_config=llm_config,
    system_message="""
  I am responsible for ensuring the integrity of the code through automated testing. 
  I execute tests, generate reports, and provide feedback to the Coder Agent.

  Key Responsibilities:
  - Execute unit, integration, and acceptance tests.
  - Generate test reports and relay results.
  - Flag issues and pass feedback to the Coder Agent.
  - Ensure that all code passes tests before it is considered complete.

  Restrictions:
  - I do not implement code or manage tasks.
  - I do not make decisions regarding the project scope or task prioritization.

  My goal is to ensure that the code is robust and meets the quality standards set forth by the Project Manager.
  """,
)
