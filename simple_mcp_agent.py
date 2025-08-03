"""
Simple MCP (Model Context Protocol) Agent Example
Demonstrates how to create an agentic AI system using MCP with Claude
"""

import os
import json
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
import anthropic

# Import our MCP tools
from tools import CalculatorTool, WebSearchTool, WeatherTool

# Load environment variables
load_dotenv()

class MCPAgent:
    """Simple MCP Agent using Claude"""
    
    def __init__(self, model: str = "claude-3-haiku-20240307", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.tools = {}
        self.conversation_history = []
        
        # Initialize Claude client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            self.claude_client = anthropic.Anthropic(api_key=api_key)
        else:
            self.claude_client = None
            print("⚠️  Warning: No ANTHROPIC_API_KEY found. Using simulated responses.")
    
    def register_tool(self, tool):
        """Register a tool with the agent"""
        self.tools[tool.name] = tool
        print(f"🔧 Tool registered: {tool.name} - {tool.description}")
    
    def get_available_tools(self) -> List[Dict[str, Any]]:
        """Get list of available tools for the LLM"""
        return [tool.get_schema() for tool in self.tools.values()]
    
    def chat(self, message: str) -> str:
        """Chat with the agent"""
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": message})
        
        # Create system prompt with tool information
        system_prompt = self._create_system_prompt()
        
        # Create messages for Claude
        messages = [{"role": "user", "content": system_prompt}] + self.conversation_history
        
        if self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=1000,
                    messages=messages
                )
                
                response_text = response.content[0].text
                
                # Add assistant response to history
                self.conversation_history.append({"role": "assistant", "content": response_text})
                
                return response_text
                
            except Exception as e:
                print(f"⚠️  Claude API error: {e}")
                return self._fallback_response(message)
        else:
            return self._fallback_response(message)
    
    def _create_system_prompt(self) -> str:
        """Create system prompt with tool information"""
        tools_info = []
        for tool in self.tools.values():
            schema = tool.get_schema()
            tools_info.append(f"- {schema['name']}: {schema['description']}")
        
        tools_text = "\n".join(tools_info)
        
        return f"""You are an MCP (Model Context Protocol) agent that can use tools to help users.

Available tools:
{tools_text}

When a user asks a question that requires using tools:
1. Think about which tools you need
2. Explain which tools you would use and why
3. Provide a helpful response

Always be helpful and explain your reasoning. If you don't need tools for a simple question, just answer directly."""
    
    def _fallback_response(self, message: str) -> str:
        """Fallback response when Claude is not available"""
        message_lower = message.lower()
        
        # Check if we need to use tools
        if any(word in message_lower for word in ["calculate", "math", "*", "+", "-", "/"]):
            return """🤖 MCP Agent Response:

I would use the calculator tool to perform this mathematical calculation. The calculator tool can handle basic arithmetic operations and provide accurate results.

Tool Usage: calculator tool for mathematical operations
Response: I would calculate the result using the calculator tool and provide you with the answer."""
        
        elif "weather" in message_lower:
            return """🤖 MCP Agent Response:

I would use the weather tool to get current weather information for the specified location. The weather tool can provide temperature, conditions, and other weather data.

Tool Usage: weather tool for current weather information
Response: I would fetch the weather data using the weather tool and provide you with current conditions."""
        
        elif any(word in message_lower for word in ["search", "find", "information", "what is"]):
            return """🤖 MCP Agent Response:

I would use the web search tool to find relevant information about this topic. The web search tool can search for current information and provide comprehensive results.

Tool Usage: web_search tool for finding information
Response: I would search for relevant information using the web search tool and provide you with the results."""
        
        else:
            return """🤖 MCP Agent Response:

I can help you with various tasks using my available tools. I have access to:
- Calculator tool for mathematical calculations
- Web search tool for finding information
- Weather tool for current weather data

Just let me know what you need help with!"""
    
    def execute_tool(self, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a specific tool"""
        if tool_name in self.tools:
            return self.tools[tool_name].execute(params)
        else:
            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found"
            }
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print("🗑️  Conversation history cleared")

def create_mcp_agent() -> MCPAgent:
    """Create and configure an MCP agent"""
    agent = MCPAgent()
    
    # Register tools
    agent.register_tool(CalculatorTool())
    agent.register_tool(WebSearchTool())
    agent.register_tool(WeatherTool())
    
    return agent

def main():
    """Main function to demonstrate the MCP agent"""
    print("🤖 Simple MCP Agent Example")
    print("=" * 50)
    print()
    
    # Create agent
    agent = create_mcp_agent()
    
    # Example conversations
    examples = [
        "What's 15 * 23?",
        "What's the weather in London?",
        "Tell me about Python programming",
        "What's the capital of France and calculate 2^10?"
    ]
    
    print("🧪 Testing MCP Agent with Different Questions:")
    print("-" * 50)
    
    for i, question in enumerate(examples, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 Agent Response:")
        
        response = agent.chat(question)
        print(response)
        print()
    
    # Interactive mode
    print("🎮 Interactive Mode (type 'quit' to exit):")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = agent.chat(user_input)
            print(f"🤖 Agent: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n✅ MCP Agent demonstration completed!")
    print("\n💡 Key Concepts Demonstrated:")
    print("  - Tool Integration: Agent can use multiple tools")
    print("  - Context Management: Maintains conversation history")
    print("  - Autonomous Decision Making: Chooses appropriate tools")
    print("  - Error Handling: Graceful fallback when API unavailable")

if __name__ == "__main__":
    main() 