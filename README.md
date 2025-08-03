# 🤖 MCP (Model Context Protocol) Example

A simple example demonstrating how to use the Model Context Protocol (MCP) with an LLM to create an agentic AI system.

## 🎯 What is MCP?

Model Context Protocol (MCP) is a standard for connecting AI models to external tools and data sources. It enables:
- **Tool Integration**: Connect LLMs to external APIs and services
- **Context Management**: Maintain conversation history and context
- **Autonomous Agents**: Create AI agents that can use tools independently

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key (get one from https://console.anthropic.com/)

### Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up your API key
cp env_example.txt .env
# Edit .env and add your ANTHROPIC_API_KEY

# 3. Run the example
python simple_mcp_agent.py
```

## 📁 Project Structure

```
mcp_example/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── simple_mcp_agent.py      # Main MCP agent example
├── tools/                   # MCP tools
│   ├── __init__.py
│   ├── calculator.py        # Calculator tool
│   ├── web_search.py        # Web search tool
│   └── weather.py           # Weather tool
├── config/
│   └── mcp_config.json      # MCP configuration
└── env_example.txt          # Environment variables template
```

## 🧠 How It Works

### 1. **MCP Agent Creation**
```python
from simple_mcp_agent import create_mcp_agent

agent = create_mcp_agent()
```

### 2. **Tool Integration**
```python
# Tools are automatically registered with the agent
agent.register_tool(calculator_tool)
agent.register_tool(web_search_tool)
agent.register_tool(weather_tool)
```

### 3. **Context Management**
```python
# Agent maintains conversation context
response = agent.chat("What's 15 * 23?")
# Agent remembers previous interactions
```

### 4. **Autonomous Tool Usage**
```python
# Agent decides which tools to use
response = agent.chat("What's the weather in London and calculate 2^10?")
# Agent uses weather tool and calculator tool automatically
```

## 🛠️ Available Tools

| Tool | Purpose | Example |
|------|---------|---------|
| `calculator` | Mathematical calculations | `2 + 3 * 4` |
| `web_search` | Search for information | `Python programming` |
| `weather` | Get weather information | `London weather` |

## 🎮 Examples

### Basic Usage
```python
from simple_mcp_agent import create_mcp_agent

# Create agent
agent = create_mcp_agent()

# Chat with agent
response = agent.chat("What's 25 * 4?")
print(response)
```

### Tool Usage
```python
# Agent uses tools automatically
response = agent.chat("What's the weather in Tokyo and calculate 15^2?")
# Agent will use weather tool and calculator tool
```

## 🔧 Key Concepts

### MCP Principles
1. **Tool Integration**: Connect LLMs to external capabilities
2. **Context Management**: Maintain conversation state
3. **Autonomous Decision Making**: Agent chooses which tools to use
4. **Standardized Interface**: Consistent tool communication

### Agent Capabilities
- **Tool Selection**: Automatically chooses appropriate tools
- **Context Awareness**: Remembers conversation history
- **Error Handling**: Graceful tool failure handling
- **Response Generation**: Combines tool results into coherent answers

## 🎯 Learning Objectives

### Technical Skills
1. **MCP Implementation**: Understanding the protocol
2. **Tool Development**: Creating custom tools
3. **Context Management**: Maintaining conversation state
4. **Error Handling**: Robust tool integration

### Agentic AI Concepts
1. **Autonomy**: Agent makes independent decisions
2. **Tool Use**: Leveraging external capabilities
3. **Planning**: Multi-step task execution
4. **Learning**: Improving from interactions

## 🚀 Next Steps

1. **Explore the code**: Understand MCP implementation
2. **Add custom tools**: Create your own MCP tools
3. **Extend the agent**: Add more sophisticated capabilities
4. **Build applications**: Create real-world MCP agents

## 📚 Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Anthropic Claude API](https://console.anthropic.com/)
- [MCP Tools](https://github.com/modelcontextprotocol/tools)

---

**🎉 Ready to explore MCP-powered agentic AI!** 🚀 