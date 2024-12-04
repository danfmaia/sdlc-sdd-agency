# Software Development Life Cycle Agency with Test-Driven Development – Shorthand: SDLC/TDD Agency

An experimental AutoGen-based project exploring how multiple AI agents could potentially collaborate in a software development workflow. This prototype implements a Test-Driven Development (TDD) approach through agent orchestration.

## Overview

The SDLC/TDD Agency investigates the possibilities of automating software development workflows using specialized AI agents. By implementing a basic Software Development Life Cycle (SDLC) with Test-Driven Development (TDD) principles, we explore how different agents might collaborate, learn, and potentially improve the development process.

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
sdlc-tdd-agency/
├── main.py              # Main entry point
├── agency.md           # Agency definition and guidelines
├── src/
│   ├── agents.py       # Agent definitions and configurations
│   └── tools.py        # Utility functions and tool registrations
└── output/
    └── docs/           # Generated documentation
```

## Current Capabilities

- **Basic Workflow Automation (Experimental)**

  - Task breakdown and assignment between agents
  - Initial progress tracking implementation
  - Basic conflict resolution patterns

- **Test-Driven Development Exploration**

  - Proof-of-concept test creation
  - Basic test execution and reporting
  - Initial code quality checks

- **Documentation Management**

  - Basic documentation generation
  - Simple version tracking
  - Project context experiments

- **Learning Mechanisms (In Development)**
  - Early-stage memory management through Mem0
  - Basic pattern recognition from interactions
  - Experimental workflow adaptations

## Research Goals

This project aims to explore several key questions:

1. How effectively can AI agents collaborate in a software development context?
2. What are the limitations and challenges of current LLM-based agents in SDLC?
3. How might TDD principles be automated through multi-agent systems?

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

## Current Limitations

- Agents may sometimes produce inconsistent or incorrect outputs
- Complex decision-making still requires human oversight
- Limited understanding of broader project context
- Experimental nature means workflows may need frequent adjustment

## Next Steps

This experimental project is continuously evolving as we explore different approaches to AI-assisted software development. Current areas of investigation include:

### 1. Agent Team Expansion (Experimental)

Currently, the agency operates with four core agents: User Proxy (Admin), Project Manager, Coder, and Tester. We're exploring the addition of specialized agents to study how they might enhance the SDLC workflow:

1. **Requirement Analyst Agent**

   - **Role:** Gather and refine business requirements
   - **Research Focus:** Testing automated requirement analysis and user story generation
   - **Current State:** Early prototype stage

2. **Design Architect Agent**

   - **Role:** Develop system architecture and design
   - **Research Focus:** Exploring automated architecture decisions and trade-offs
   - **Current State:** Concept development

3. **Documentation Agent**

   - **Role:** Manage detailed and ongoing documentation
   - **Research Focus:** Testing automated documentation generation and maintenance
   - **Current State:** Basic implementation

4. **Reviewer Agent**

   - **Role:** Conduct code reviews to ensure quality
   - **Research Focus:** Studying automated code analysis patterns
   - **Current State:** Prototype testing

5. **Deployment Agent**
   - **Role:** Automate the deployment process
   - **Research Focus:** Investigating CI/CD automation patterns
   - **Current State:** Initial planning

### 2. Multi-Agent System Enhancements

To support the expanded agent team and improve overall functionality, we plan to investigate:

- **Enhanced Collaboration:** Improved communication protocols between agents
- **Memory Management:** Advanced implementation of Mem0 for better learning
- **Workflow Optimization:** Testing different process patterns
- **Scalability Improvements:** Exploring methods to handle larger projects

### 3. User Interface Development

We're evaluating several interface options for research purposes:

1. **Streamlit**

   - **Description:** Python-based framework for rapid prototyping
   - **Research Value:** Quick iteration on interaction patterns
   - **Current Status:** Initial testing

2. **Gradio**

   - **Description:** AI-focused interface framework
   - **Research Value:** Specialized AI model interactions
   - **Current Status:** Under evaluation

3. **Dash**

   - **Description:** Framework combining Flask, Plotly, and React
   - **Research Value:** Data visualization experiments
   - **Current Status:** Concept phase

4. **TS/React**
   - **Description:** Full-featured web application framework
   - **Research Value:** Complex interaction patterns
   - **Current Status:** Future consideration

### Implementation Strategy

We'll follow an experimental approach:

1. Test new agents individually in controlled environments
2. Study multi-agent interactions through incremental integration
3. Prototype and evaluate interface solutions
4. Gather data on agent behaviors and effectiveness

## License

[MIT License](LICENSE)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [AutoGen](https://github.com/microsoft/autogen)
- Inspired by modern software development practices and TDD principles
