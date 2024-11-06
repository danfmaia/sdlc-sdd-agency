import os
import json
from typing_extensions import Annotated, List, Tuple, Dict
from autogen import UserProxyAgent, AssistantAgent
import subprocess

default_path = os.path.abspath("./output") + "/"
docs_path = os.path.abspath("./output/docs") + "/"  # Path for documentation
PROJECT_CONTEXT_PATH = os.path.join(docs_path, "project_context.json")


def ensure_directory_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def load_project_context() -> Dict:
    """Load project context from file if it exists."""
    try:
        if os.path.exists(PROJECT_CONTEXT_PATH):
            with open(PROJECT_CONTEXT_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
    except FileNotFoundError:
        print("Project context file not found")
    except PermissionError:
        print("Permission denied when accessing project context file")
    except json.JSONDecodeError as e:
        print(f"Error decoding project context JSON: {e}")
    except IOError as e:
        print(f"IO Error when reading project context: {e}")

    return {
        "name": "",
        "description": "",
        "tech_stack": [],
        "features": [],
        "current_state": {}
    }


def save_project_context(context: Dict) -> None:
    """Save project context to file."""
    ensure_directory_exists(os.path.dirname(PROJECT_CONTEXT_PATH))
    with open(PROJECT_CONTEXT_PATH, 'w', encoding='utf-8') as f:
        json.dump(context, f, indent=2)


def register_tools(user_proxy: UserProxyAgent, project_manager: AssistantAgent, coder_agent: AssistantAgent, tester_agent: AssistantAgent):
    # Load and inject project context into Project Manager's system message
    context = load_project_context()
    project_manager.update_system_message(f"""
{project_manager.system_message}

Current Project Context:
- Project Name: {context.get('name')}
- Description: {context.get('description')}
- Tech Stack: {', '.join(context.get('tech_stack', []))}
- Implemented Features: {', '.join(context.get('features', []))}
""")

    # Tools for Project Manager
    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Update project context with new information.")
    def update_project_context(
        updates: Annotated[Dict,
                           "Dictionary containing updates to project context"]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            context = load_project_context()
            context.update(updates)
            save_project_context(context)
            return 0, "Project context updated successfully"
        except FileNotFoundError:
            return 1, "Error: Project context file not found"
        except PermissionError:
            return 1, "Error: Permission denied when accessing project context"
        except json.JSONDecodeError as e:
            return 1, f"Error decoding project context JSON: {str(e)}"
        except IOError as e:
            return 1, f"IO Error when updating project context: {str(e)}"
        except TypeError as e:
            return 1, f"Type Error: Invalid update data format: {str(e)}"

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Create a documentation file.")
    def create_doc_file(
        filename: Annotated[str, "Name of the documentation file to create."],
        content: Annotated[str, "Content to write in the documentation file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            full_path = os.path.join(docs_path, filename)
            ensure_directory_exists(os.path.dirname(full_path))
            with open(full_path, "w", encoding="utf-8") as file:
                file.write(content)
            return 0, "Documentation file created successfully"
        except FileNotFoundError:
            return 1, "Error: Directory not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="List documentation files in the docs directory.")
    def list_docs(
        directory: Annotated[str, "Directory to check."]
    ) -> Annotated[Tuple[int, List[str]], "Status code and list of documentation files"]:
        try:
            ensure_directory_exists(docs_path + directory)
            files = os.listdir(docs_path + directory)
            return 0, files
        except FileNotFoundError:
            return 1, "Error: Directory not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Check the contents of a documentation file.")
    def see_doc_file(
        filename: Annotated[str,
                            "Name and path of documentation file to check."]
    ) -> Annotated[Tuple[int, str], "Status code and file contents."]:
        try:
            with open(docs_path + filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
            formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
            file_contents = "".join(formatted_lines)
            return 0, file_contents
        except FileNotFoundError:
            return 1, "Error: File not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @project_manager.register_for_llm(description="Modify the contents of a documentation file.")
    def modify_doc_file(
        filename: Annotated[str, "Name and path of documentation file to modify."],
        new_content: Annotated[str,
                               "New content to replace the old content in the documentation file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            with open(docs_path + filename, "w", encoding="utf-8") as file:
                file.write(new_content)
            return 0, "Documentation file modified successfully"
        except FileNotFoundError:
            return 1, "Error: File not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    # Tools for Coder Agent
    @user_proxy.register_for_execution()
    @coder_agent.register_for_llm(description="List files in chosen directory.")
    def list_dir(
        directory: Annotated[str, "Directory to check."]
    ) -> Annotated[Tuple[int, List[str]], "Status code and list of files"]:
        try:
            ensure_directory_exists(default_path + directory)
            files = os.listdir(default_path + directory)
            return 0, files
        except FileNotFoundError:
            return 1, "Error: Directory not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @coder_agent.register_for_llm(description="Check the contents of a chosen file.")
    def see_file(
        filename: Annotated[str, "Name and path of file to check."]
    ) -> Annotated[Tuple[int, str], "Status code and file contents."]:
        try:
            with open(default_path + filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
            formatted_lines = [f"{i+1}:{line}" for i, line in enumerate(lines)]
            file_contents = "".join(formatted_lines)
            return 0, file_contents
        except FileNotFoundError:
            return 1, "Error: File not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @coder_agent.register_for_llm(description="Replaces all the code within a file with new one. Proper indentation is important.")
    def modify_code(
        filename: Annotated[str, "Name and path of file to change."],
        new_code: Annotated[str, "New piece of code to replace old code with. Remember about providing indents."],
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            with open(default_path + filename, "w", encoding="utf-8") as file:
                file.write(new_code)
            return 0, "Code was written successfully."
        except FileNotFoundError:
            return 1, "Error: File not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    @user_proxy.register_for_execution()
    @coder_agent.register_for_llm(description="Create a new file with code.")
    def create_file_with_code(
        filename: Annotated[str, "Name and path of file to create."],
        code: Annotated[str, "Code to write in the file."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            ensure_directory_exists(os.path.dirname(default_path + filename))
            with open(default_path + filename, "w", encoding="utf-8") as file:
                file.write(code)
            return 0, "File created successfully"
        except FileNotFoundError:
            return 1, "Error: Directory not found."
        except PermissionError:
            return 1, "Error: Permission denied."
        except IOError as e:
            return 1, f"IOError: {str(e)}"

    # Shared tool for Coder and Tester Agents
    @user_proxy.register_for_execution()
    @coder_agent.register_for_llm(description="Prepare bash commands for execution.")
    @tester_agent.register_for_llm(description="Execute test commands.")
    def execute_command(
        command: Annotated[str, "Command to execute."]
    ) -> Annotated[Tuple[int, str], "Status code and message."]:
        try:
            os.system(f"CI=true cd {default_path} && {command}")
            return 0, "Command executed successfully"
        except FileNotFoundError:
            return 1, "Error: Command or directory not found"
        except PermissionError:
            return 1, "Error: Permission denied"
        except subprocess.SubprocessError as e:
            return 1, f"Subprocess Error: {str(e)}"
        except OSError as e:
            return 1, f"OS Error: {str(e)}"
