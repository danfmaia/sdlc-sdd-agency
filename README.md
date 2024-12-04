# SDLC Agency with Test-Driven Development

A sophisticated AutoGen-based agency that implements a complete Software Development Life Cycle (SDLC) workflow with Test-Driven Development (TDD) principles. This agency orchestrates multiple AI agents to collaborate on software development projects, from requirements gathering to deployment.

## Overview

The SDLC Agency provides an automated, self-improving approach to software development by coordinating specialized AI agents, each with distinct roles and responsibilities. The workflow follows TDD principles, ensuring high-quality, well-tested code through continuous collaboration between agents.

## Architecture

### Core Components

1. **Group Chat System**

   - Manages communication between agents
   - Handles message routing and termination conditions
   - Maintains chat history and generates summaries

2. **Agent System**

   - User Proxy (Admin) Agent: Human interface for project oversight
   - Project Manager Agent: Orchestrates workflow and task management
   - Coder Agent: Implements features following TDD principles
   - Tester Agent: Manages test execution and quality assurance

3. **Tools System**
   - File management utilities
   - Documentation tools
   - Code execution capabilities
   - Project context management

### Directory Structure

```
sdlc_agency/
├── main.py              # Main entry point
├── agency.md           # Agency definition and guidelines
├── src/
│   ├── agents.py       # Agent definitions and configurations
│   └── tools.py        # Utility functions and tool registrations
└── output/
    └── docs/           # Generated documentation
```

## Features

- **Automated Workflow Management**

  - Task breakdown and assignment
  - Progress tracking
  - Conflict resolution

- **Test-Driven Development**

  - Automated test creation
  - Test execution and reporting
  - Code quality assurance

- **Documentation Management**

  - Automated documentation generation
  - Version control
  - Project context tracking

- **Continuous Improvement**
  - Memory management through Mem0
  - Learning from previous interactions
  - Workflow optimization

## Usage

1. **Environment Setup**

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key
```

2. **Running the Agency**

```python
python main.py
```

3. **Interacting with the Agency**
   The agency can be initiated with specific tasks through the UserProxyAgent:

```python
chat_result = user_proxy.initiate_chat(
    manager,
    message="Your task description here"
)
```

## Configuration

### LLM Configuration

```python
llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0,
}
```

### Agent Configuration

Agents can be customized through their system messages and tool registrations. See `src/agents.py` for examples.

## Tools and Utilities

The agency provides various tools for:

- File management
- Documentation creation and modification
- Code execution
- Project context management
- Test execution

## Output

The agency generates:

- Chat summaries and history (`chat_results.txt`)
- Project documentation
- Code files
- Test reports

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## Next Steps

The SDLC Agency is evolving to provide a comprehensive software development solution. Our roadmap focuses on three key areas: expanding the agent team, enhancing multi-agent system capabilities, and improving user interaction.

### 1. Agent Team Expansion

Currently, the agency operates with four core agents: User Proxy (Admin), Project Manager, Coder, and Tester. To create a complete SDLC workflow, we plan to introduce five additional specialized agents:

1. **Requirement Analyst Agent**

   - **Role:** Gather and refine business requirements.
   - **Responsibilities:** Collect user stories, acceptance criteria, and functional requirements.

2. **Design Architect Agent**

   - **Role:** Develop system architecture and design.
   - **Responsibilities:** Create architecture diagrams and design specifications.

3. **Documentation Agent**

   - **Role:** Manage detailed and ongoing documentation.
   - **Responsibilities:** Document system design, user manuals, and test documentation.

4. **Reviewer Agent**

   - **Role:** Conduct code reviews to ensure quality and adherence to standards.
   - **Responsibilities:** Review code, identify improvements, and ensure compliance.

5. **Deployment Agent**
   - **Role:** Automate the deployment process and ensure smooth integration.
   - **Responsibilities:** Implement CI/CD pipelines and manage rollbacks.

### 2. Multi-Agent System Enhancements

To support the expanded agent team and improve overall functionality, we plan to implement:

- **Enhanced Collaboration:** Improved communication protocols and coordination between agents
- **Memory Management:** Advanced implementation of Mem0 for better learning and adaptation
- **Workflow Optimization:** Streamlined processes for handling complex projects
- **Scalability Improvements:** Enhanced capability to handle larger projects and teams

### 3. User Interface Development

To make the system more accessible and user-friendly, we're evaluating several interface options, each with distinct advantages:

1. **Streamlit**

   - **Description:** Python-based framework for rapid development of clean, simple interfaces
   - **Best for:** Quick prototyping and straightforward chat interactions
   - **Advantage:** Minimal setup time and easy deployment

2. **Gradio**

   - **Description:** AI-focused interface framework with built-in chat components
   - **Best for:** ML/AI application demonstrations
   - **Advantage:** Specialized for AI model interactions

3. **Dash**

   - **Description:** Framework combining Flask, Plotly, and React
   - **Best for:** Data-rich applications requiring sophisticated visualizations
   - **Advantage:** Balance of customization and development speed

4. **TS/React**
   - **Description:** Full-featured web application framework
   - **Best for:** Complex, scalable applications
   - **Advantage:** Maximum customization and scalability potential

The interface choice will be based on user feedback and specific requirements as the project evolves.

### Implementation Strategy

We'll follow a phased approach:

1. Integrate new agents one at a time, ensuring stable operation
2. Implement multi-agent system enhancements incrementally
3. Develop and test the chosen interface solution
4. Gather user feedback and iterate on improvements

This structured expansion will ensure that each addition contributes to a more robust and efficient software development workflow.

## License

[MIT License](LICENSE)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [AutoGen](https://github.com/microsoft/autogen)
- Inspired by modern software development practices and TDD principles
