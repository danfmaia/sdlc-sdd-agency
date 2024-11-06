import os
from autogen import GroupChat, GroupChatManager
from agents import user_proxy, project_manager, coder_agent, tester_agent
from tools import register_tools

# Register tools for execution
register_tools(user_proxy, project_manager, coder_agent, tester_agent)

##################
# Set up the chat #
##################
groupchat = GroupChat(
    agents=[user_proxy, project_manager, coder_agent, tester_agent],
    messages=[],
    max_round=100,
    send_introductions=True,
    enable_clear_history=True,
)

manager = GroupChatManager(
    groupchat=groupchat,
    llm_config={
        "model": "gpt-4o",
        "api_key": os.environ["OPENAI_API_KEY"],
        "temperature": 0,
    },
    is_termination_msg=lambda msg: "terminate" in msg["content"].lower()
)

##################
# Start the chat #
##################
chat_result = user_proxy.initiate_chat(
    manager,
    message="Explore the project docs and write a README file."
)

# Save the chat result to a file in the current directory
OUTPUT_FILE_PATH = "chat_results.txt"

with open(OUTPUT_FILE_PATH, "w", encoding="utf-8") as file:
    file.write("Chat Summary:\n")
    file.write(chat_result.summary + "\n\n")
    file.write("Chat History:\n")
    for message in chat_result.chat_history:
        file.write(f"{message['role']}: {message['content']}\n")
