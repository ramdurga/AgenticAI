"""
Simple MCP Demo
Demonstrates the Model Context Protocol concept with a basic implementation
"""

import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

def create_simple_mcp_agent():
    """Create a simple MCP-style agent"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️  No ANTHROPIC_API_KEY found. Using simulated responses.")
        return None
    
    return anthropic.Anthropic(api_key=api_key)

def simulate_tool_usage(tool_name: str, params: dict) -> str:
    """Simulate tool usage for the MCP agent"""
    
    if tool_name == "calculator":
        expression = params.get("expression", "")
        try:
            result = eval(expression)
            return f"Calculator result: {expression} = {result}"
        except:
            return f"Calculator error: Invalid expression '{expression}'"
    
    elif tool_name == "web_search":
        query = params.get("query", "")
        return f"Web search results for '{query}': Found relevant information about this topic."
    
    elif tool_name == "weather":
        city = params.get("city", "")
        return f"Weather for {city}: 20°C, Partly Cloudy (mock data)"
    
    else:
        return f"Tool '{tool_name}' executed with parameters: {params}"

def mcp_agent_response(question: str, claude_client=None):
    """Generate an MCP agent response"""
    
    if claude_client:
        try:
            # Create a comprehensive prompt for MCP behavior
            prompt = f"""You are an MCP (Model Context Protocol) agent that can use tools to help users.

Available tools:
- calculator: Perform mathematical calculations
- web_search: Search the web for current information
- weather: Get current weather information for a city

Question: {question}

Please provide:
1. Which tools you would use to answer this question
2. Your step-by-step reasoning process
3. A comprehensive answer based on your analysis

Think like an autonomous agent that can plan, use tools, and reason step by step."""

            response = claude_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"⚠️  Claude API error: {e}")
            return fallback_mcp_response(question)
    else:
        return fallback_mcp_response(question)

def fallback_mcp_response(question: str):
    """Fallback response when Claude is not available"""
    
    question_lower = question.lower()
    
    if any(word in question_lower for word in ["calculate", "math", "*", "+", "-", "/"]):
        return """🤖 MCP Agent Response:

I would use the calculator tool to perform this mathematical calculation.

Tool Usage: calculator tool
Parameters: {"expression": "mathematical expression"}
Response: I would calculate the result using the calculator tool and provide you with the answer.

This demonstrates the MCP principle of tool integration and autonomous decision making."""
    
    elif "weather" in question_lower:
        return """🤖 MCP Agent Response:

I would use the weather tool to get current weather information.

Tool Usage: weather tool
Parameters: {"city": "location name"}
Response: I would fetch the weather data using the weather tool and provide you with current conditions.

This demonstrates the MCP principle of context-aware tool selection."""
    
    elif any(word in question_lower for word in ["search", "find", "information", "what is"]):
        return """🤖 MCP Agent Response:

I would use the web search tool to find relevant information.

Tool Usage: web_search tool
Parameters: {"query": "search term"}
Response: I would search for relevant information using the web search tool and provide you with the results.

This demonstrates the MCP principle of autonomous tool usage."""
    
    else:
        return """🤖 MCP Agent Response:

I can help you with various tasks using my available tools. I have access to:
- Calculator tool for mathematical calculations
- Web search tool for finding information
- Weather tool for current weather data

This demonstrates the MCP principle of standardized tool communication."""

def main():
    """Main function to demonstrate MCP concepts"""
    print("🤖 Simple MCP (Model Context Protocol) Demo")
    print("=" * 50)
    print()
    
    # Create agent
    agent = create_simple_mcp_agent()
    
    # Example questions
    questions = [
        "What's 15 * 23?",
        "What's the weather in London?",
        "Tell me about Python programming",
        "What's the capital of France and calculate 2^10?"
    ]
    
    print("🧪 Testing MCP Agent with Different Questions:")
    print("-" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 MCP Agent Response:")
        
        response = mcp_agent_response(question, agent)
        print(response)
        print()
    
    print("✅ MCP Demo completed!")
    print("\n💡 MCP Key Concepts Demonstrated:")
    print("  - Tool Integration: Connect LLMs to external capabilities")
    print("  - Context Management: Maintain conversation state")
    print("  - Autonomous Decision Making: Agent chooses which tools to use")
    print("  - Standardized Interface: Consistent tool communication")
    print("\n🎯 This demonstrates the Model Context Protocol principles!")

if __name__ == "__main__":
    main() 