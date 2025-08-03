"""
Simple Claude Agentic AI Demo
Demonstrates agentic AI concepts using Claude directly
"""

import os
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

def create_claude_agent():
    """Create a simple agent using Claude directly"""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️  No ANTHROPIC_API_KEY found. Using simulated responses.")
        return None
    
    return anthropic.Anthropic(api_key=api_key)

def simulate_agent_response(question: str, claude_client=None):
    """Simulate an agentic AI response"""
    
    if claude_client:
        try:
            # Create a prompt that simulates agentic thinking
            prompt = f"""You are an agentic AI assistant. For the following question, think step by step:

Question: {question}

Please provide:
1. What tools you would use to answer this
2. Your step-by-step reasoning
3. A comprehensive answer

Think like an agentic AI that can use tools and reason autonomously."""

            response = claude_client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            print(f"⚠️  Claude API error: {e}")
            return simulate_fallback_response(question)
    else:
        return simulate_fallback_response(question)

def simulate_fallback_response(question: str):
    """Simulate agentic AI response without Claude"""
    
    # Simple keyword-based responses
    question_lower = question.lower()
    
    if "python" in question_lower:
        return """🤖 Agentic AI Response:

1. Tools I would use: Web search tool to find current information about Python
2. Reasoning: I need to search for comprehensive information about Python programming
3. Answer: Python is a high-level programming language known for its simplicity and readability. It's widely used for web development, data science, AI, and automation. Python's clean syntax makes it excellent for beginners while being powerful enough for complex applications."""

    elif any(word in question_lower for word in ["calculate", "math", "*", "+", "-", "/"]):
        return """🤖 Agentic AI Response:

1. Tools I would use: Calculator tool to perform mathematical calculations
2. Reasoning: This is a mathematical calculation that requires precise computation
3. Answer: I would use my calculator tool to compute the result accurately and provide the mathematical solution."""

    elif "weather" in question_lower:
        return """🤖 Agentic AI Response:

1. Tools I would use: Weather API tool to get current weather information
2. Reasoning: I need to access real-time weather data for the specified location
3. Answer: I would use my weather tool to fetch current conditions, temperature, and forecast for the requested city."""

    else:
        return """🤖 Agentic AI Response:

1. Tools I would use: Web search tool to gather information
2. Reasoning: I need to search for relevant information to provide a comprehensive answer
3. Answer: I would use my search tools to find current, accurate information and synthesize it into a helpful response."""

def main():
    """Main demo function"""
    print("🤖 Simple Claude Agentic AI Demo")
    print("=" * 50)
    print()
    
    # Create Claude client
    claude_client = create_claude_agent()
    
    # Example questions
    questions = [
        "What is Python programming?",
        "What's 15 * 23?",
        "What's the weather in London?",
        "What's the capital of France and what's its population?"
    ]
    
    print("🧪 Testing Agentic AI with Different Questions:")
    print("-" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 Agent Response:")
        
        response = simulate_agent_response(question, claude_client)
        print(response)
        print()
    
    print("✅ Demo completed!")
    print("\n💡 Key Concepts Demonstrated:")
    print("  - Tool Selection: Agent chooses appropriate tools")
    print("  - Reasoning: Step-by-step thinking process")
    print("  - Execution: Using tools to get information")
    print("  - Synthesis: Combining results into answers")

if __name__ == "__main__":
    main() 