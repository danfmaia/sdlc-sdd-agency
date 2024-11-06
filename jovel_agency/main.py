import os
import autogen
from autogen import UserProxyAgent
from dotenv import load_dotenv
from typing_extensions import Annotated, List, Tuple


load_dotenv()

llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0,
    # "config_list": config_list,
}

#####################
# Define the agents #
#####################

project_manager = autogen.AssistantAgent(
    name="Project_Manager",
    system_message="""
  I am an experienced Project Manager overseeing the development of a software product. My responsibilities include translating the requirements provided by the Admin into manageable tasks, which I then assign to the Engineer.

  Key Responsibilities:
  - Break down project requirements into detailed, manageable tasks.
  - Assign tasks to the Engineer in a logical and efficient sequence.
  - Monitor the progress of the project and ensure timely delivery of each task.

  Workflow:
  - For each completed task, I will assess if further tasks are required.
  - I will ensure that any identified issues are resolved before moving on to the next task.
  - When the project is complete, I will confirm the project's completion with a "TERMINATE" message.

  Restrictions:
  - I never suggest, review, or test code; my focus is purely on task management and project oversight.
  - I do not get involved in the technical implementation details.

  My goal is to ensure the smooth progression of the project from start to finish, maintaining clear communication and efficient task management.
  """,
    llm_config=llm_config,
)

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config,
    system_message="""
  I am a seasoned Software Engineer, responsible for writing clean, efficient, and maintainable code based on the tasks assigned by the Project Manager. 
  My focus is exclusively on coding and ensuring that the code meets the specified requirements.

  Key Responsibilities:
  - Implement features and fixes according to the provided task specifications.
  - Write code that adheres to best practices and is optimized for performance and readability.
  - Ensure that the code is well-documented to facilitate future maintenance and collaboration.

  Restrictions:
  - I NEVER manage or assign tasks.
  - I do not make decisions regarding the project scope or task prioritization.

  My goal is to deliver high-quality code that meets the requirements set forth by the Project Manager and the Admin.
  """,
)

user_proxy = UserProxyAgent(
    name="Admin",
    human_input_mode="ALWAYS",
    code_execution_config=False,
)

groupchat = autogen.GroupChat(
    agents=[user_proxy, project_manager, engineer],
    messages=[],
    max_round=100,
    send_introductions=True,
    enable_clear_history=True,
)
manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config=llm_config,
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

####################
# Tool definitions #
####################

default_path = os.path.abspath("./output") + "/"


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="List files in chosen directory.")
def list_dir(
    directory: Annotated[str, "Directory to check."]
) -> Annotated[Tuple[int, List[str]], "Status code and list of files"]:
    files = os.listdir(default_path + directory)
    return 0, files


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Check the contents of a chosen file.")
def see_file(
    filename: Annotated[str, "Name and path of file to check."]
) -> Annotated[Tuple[int, str], "Status code and file contents."]:
    with open(default_path + filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
    file_contents = "".join(formatted_lines)

    return 0, file_contents


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Replaces all the code within a file with new one. Proper indentation is important.")
def modify_code(
    filename: Annotated[str, "Name and path of file to change."],
    new_code: Annotated[str, "New piece of code to replace old code with. Remember about providing indents."],
) -> Annotated[Tuple[int, str], "Status code and message."]:
    with open(default_path + filename, "w", encoding="utf-8") as file:
        file.write(new_code)
    return 0, "Code was written successfully."


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Create a new file with code.")
def create_file_with_code(
    filename: Annotated[str, "Name and path of file to create."],
    code: Annotated[str, "Code to write in the file."]
) -> Annotated[Tuple[int, str], "Status code and message."]:
    with open(default_path + filename, "w", encoding="utf-8") as file:
        file.write(code)
    return 0, "File created successfully"


@user_proxy.register_for_execution()
@engineer.register_for_llm(description="Execute bash command.")
def execute_command(
    command: Annotated[str, "Command to execute."]
) -> Annotated[Tuple[int, str], "Status code and message."]:
    os.system(f"CI=true cd {default_path} && {command}")
    return 0, "Command executed successfully"


##################
# Start the chat #
##################
chat_result = user_proxy.initiate_chat(
    manager,
    message="""
Create a React app that is a simple todo list.
""",
)
