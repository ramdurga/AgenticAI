"""
Fixed Simple Agentic AI Example
Bypasses LangChain compatibility issues by using direct Claude integration
"""

import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

def create_simple_agent():
    """Create a simple agentic AI using Claude directly"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️  No ANTHROPIC_API_KEY found. Using simulated responses.")
        return None
    
    return anthropic.Anthropic(api_key=api_key)

def simulate_tool_usage(tool_name: str, input_data: str) -> str:
    """Simulate tool usage for the agent"""
    
    if tool_name == "web_search":
        # Simulate web search
        mock_results = {
            "python": "Python is a high-level programming language known for its simplicity and readability.",
            "weather": "Weather information can be found through various online services and APIs.",
            "capital": "Capitals are the primary cities of countries, often housing government buildings.",
            "population": "Population data is collected by governments and international organizations."
        }
        
        for keyword, info in mock_results.items():
            if keyword.lower() in input_data.lower():
                return f"Search results for '{input_data}': {info}"
        
        return f"Search results for '{input_data}': Found relevant information about this topic."
    
    elif tool_name == "calculator":
        # Simulate calculator
        try:
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in input_data):
                return "Error: Invalid characters in expression"
            
            result = eval(input_data)
            return f"Calculation: {input_data} = {result}"
        except Exception as e:
            return f"Error calculating '{input_data}': {str(e)}"
    
    elif tool_name == "weather":
        # Simulate weather tool
        mock_weather = {
            "new york": "New York: 72°F, Partly Cloudy",
            "london": "London: 15°C, Rainy",
            "tokyo": "Tokyo: 25°C, Sunny",
            "paris": "Paris: 18°C, Cloudy"
        }
        
        city_lower = input_data.lower()
        if city_lower in mock_weather:
            return mock_weather[city_lower]
        else:
            return f"Weather for {input_data}: 20°C, Partly Cloudy (mock data)"
    
    else:
        return f"Tool '{tool_name}' executed with input: {input_data}"

def agentic_response(question: str, claude_client=None):
    """Generate an agentic AI response"""
    
    if claude_client:
        try:
            # Create a comprehensive prompt for agentic behavior
            prompt = f"""You are an agentic AI assistant that can use tools to answer questions.

Question: {question}

Available tools:
- web_search: Search for information on the web
- calculator: Perform mathematical calculations
- weather: Get weather information for cities

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
            return fallback_response(question)
    else:
        return fallback_response(question)

def fallback_response(question: str):
    """Fallback response when Claude is not available"""
    
    question_lower = question.lower()
    
    if "python" in question_lower:
        return """🤖 Agentic AI Response:

1. Tools I would use: web_search tool
2. Reasoning: I need to search for comprehensive information about Python programming
3. Answer: Python is a high-level programming language known for its simplicity and readability. It's widely used for web development, data science, AI, and automation. Python's clean syntax makes it excellent for beginners while being powerful enough for complex applications.

Tool Usage: web_search("Python programming") → Found comprehensive information about Python's features and applications."""

    elif any(word in question_lower for word in ["calculate", "math", "*", "+", "-", "/"]):
        return """🤖 Agentic AI Response:

1. Tools I would use: calculator tool
2. Reasoning: This is a mathematical calculation that requires precise computation
3. Answer: I would use my calculator tool to compute the result accurately.

Tool Usage: calculator("15 * 23") → Calculation: 15 * 23 = 345"""

    elif "weather" in question_lower:
        return """🤖 Agentic AI Response:

1. Tools I would use: weather tool
2. Reasoning: I need to access real-time weather data for the specified location
3. Answer: I would use my weather tool to fetch current conditions and forecast.

Tool Usage: weather("London") → London: 15°C, Rainy"""

    else:
        return """🤖 Agentic AI Response:

1. Tools I would use: web_search tool
2. Reasoning: I need to search for relevant information to provide a comprehensive answer
3. Answer: I would use my search tools to find current, accurate information and synthesize it into a helpful response.

Tool Usage: web_search("relevant information") → Found comprehensive data to answer the question."""

def main():
    """Main function to demonstrate the fixed agent"""
    
    print("🤖 Fixed Simple Agentic AI Example")
    print("=" * 50)
    
    # Create agent
    agent = create_simple_agent()
    
    # Example questions
    questions = [
        "What is Python programming?",
        "What's 15 * 23?",
        "What's the weather in London?",
        "What's the capital of France and what's its population?"
    ]
    
    print("\n🧪 Testing Agentic AI with Different Questions:")
    print("-" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 Agent Response:")
        
        response = agentic_response(question, agent)
        print(response)
        print()
    
    print("✅ Agent demonstration completed!")
    print("\n💡 Key Concepts Demonstrated:")
    print("  - Tool Selection: Agent chooses appropriate tools")
    print("  - Reasoning: Step-by-step thinking process")
    print("  - Execution: Using tools to get information")
    print("  - Synthesis: Combining results into answers")

if __name__ == "__main__":
    main() 