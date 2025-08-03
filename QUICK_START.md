# 🚀 Quick Start Guide - LangChain Agentic AI

This guide will help you get started with the minimal LangChain agentic AI solution.

## 📋 Prerequisites

- Python 3.8 or higher
- Anthropic API key (get one from https://console.anthropic.com/)

## 🛠️ Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your API key:**
   ```bash
   cp env_example.txt .env
   # Edit .env and add your Anthropic API key
   ```

3. **Test the setup:**
   ```bash
   python demo.py
   ```

## 🎮 Running Examples

### Basic Agent Demo
```bash
python simple_agent.py
```
Shows how the agent answers predefined questions using tools.

### Interactive Chat
```bash
python interactive_agent.py
```
Start a conversation with the agent. Type 'quit' to exit.

### Tool Demo (No API Key Required)
```bash
python demo.py
```
See how the individual tools work without needing an API key.

## 🧠 Key Concepts

### Agentic AI Principles
- **Autonomy**: Agents work independently
- **Tool Use**: Agents can use external tools
- **Planning**: Agents create step-by-step plans
- **Memory**: Agents remember conversations
- **Learning**: Agents improve over time

### LangChain Components
- **LLM**: Claude language model for reasoning
- **Tools**: Web search, calculator, weather
- **Memory**: Conversation history
- **Agent**: Orchestrates everything together

## 🔧 Available Tools

1. **Web Search**: Find current information
2. **Calculator**: Perform mathematical calculations
3. **Weather**: Get weather information for cities

## 💡 Tips

- Start with `demo.py` to understand the tools
- Use `simple_agent.py` to see the full agent in action
- Try `interactive_agent.py` for conversations
- Check the `tools.py` file to see how tools are implemented

## 🆘 Troubleshooting

**No API Key Error:**
- Make sure you have an Anthropic API key
- Check that your `.env` file is set up correctly
- Run `demo.py` to test without an API key

**Import Errors:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check your Python version (3.8+ required)

**Tool Errors:**
- The tools are simulated for demo purposes
- In a real application, you'd connect to actual APIs

## 🎯 Next Steps

1. Explore the `tools.py` file to understand tool implementation
2. Try modifying the agent prompts in the Python files
3. Add your own custom tools
4. Experiment with different Claude models

Happy coding! 🚀 