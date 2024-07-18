# Multi-Agent Development Team

## Introduction

This repository contains the code referenced in the article "Building your own software development team with ChatGPT and AutoGen." The article explores how to build a software development team using AI agents, specifically leveraging ChatGPT and the AutoGen framework.

## Installation

To set up the project, follow these steps:

- `pip install -r requirements.txt`
- Rename `OAI_CONFIG_LIST.json.sample` to `OAI_CONFIG_LIST.json`.
- Add your OpenAI API key to the configuration file.

## Usage

To start the multi-agent chat, run the following command:

```bash
python main.py
```

## Agent Configuration

### Admin

The human in the loop, providing feedback and manually running the code.

### Project Manager

Responsible for breaking down requirements into tasks and managing the project flow.

### Engineer

Responsible for writing and modifying the code based on the tasks assigned by the Project Manager.

## Tools

The following tools are registered to assist the Engineer in coding tasks:

- `list_dir`: Lists the contents of a directory.
- `see_file`: Views the content of a file.
- `modify_code`: Modifies existing code in a file.
- `create_file_with_code`: Creates a new file with the provided code.
- `execute_command`: Runs bash commands.

## Example

To create a React.js todo list app, initiate the chat with the following message:

```bash
chat_result = user_proxy.initiate_chat(
    manager,
    message="""
Create a React app that is a simple todo list.
""",
```

## Contact

For any questions or feedback, please open an issue.
