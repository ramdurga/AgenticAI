"""
Working Demo of Agentic AI Concepts
This demo shows how agentic AI works without requiring complex LangChain setup
"""

from tools import get_tools

def simulate_agentic_ai():
    """Simulate how an agentic AI would work"""
    print("🤖 Agentic AI Simulation")
    print("=" * 50)
    print("This simulates how an agentic AI would think and use tools.")
    print()
    
    # Get the tools
    tools = get_tools()
    
    # Example questions
    questions = [
        "What is Python programming?",
        "What's 15 * 23?",
        "What's the weather in London?",
        "What's the capital of France and what's its population?"
    ]
    
    print("�� Simulating Agentic AI Responses:")
    print("-" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 Agent Thinking Process:")
        
        # Simulate agent reasoning
        if "python" in question.lower():
            print("  1. I need to search for information about Python")
            print("  2. I'll use the web_search tool")
            result = tools[0].run("python programming")
            print(f"  3. Tool result: {result}")
            print("  4. I'll provide a comprehensive answer based on this information")
            
        elif any(op in question for op in ['*', '+', '-', '/', 'calculate']):
            print("  1. I need to perform a mathematical calculation")
            print("  2. I'll use the calculator tool")
            # Extract the math expression
            import re
            numbers = re.findall(r'\d+', question)
            if len(numbers) >= 2:
                expression = f"{numbers[0]} * {numbers[1]}"
                result = tools[1].run(expression)
                print(f"  3. Tool result: {result}")
                print("  4. I'll provide the calculated answer")
            
        elif "weather" in question.lower():
            print("  1. I need to get weather information")
            print("  2. I'll use the weather tool")
            # Extract city name
            if "london" in question.lower():
                result = tools[2].run("London")
                print(f"  3. Tool result: {result}")
                print("  4. I'll provide the weather information")
                
        elif "capital" in question.lower() or "population" in question.lower():
            print("  1. I need to search for information about capitals and populations")
            print("  2. I'll use the web_search tool")
            result = tools[0].run("capital of France population")
            print(f"  3. Tool result: {result}")
            print("  4. I'll combine this information to provide a comprehensive answer")
        
        print("  5. Final Answer: Based on my analysis and tool usage, here's what I found...")
        print()
    
    print("✅ Agentic AI simulation completed!")
    print("\n💡 Key Concepts Demonstrated:")
    print("  - Tool Selection: Agent chooses appropriate tools")
    print("  - Reasoning: Step-by-step thinking process")
    print("  - Execution: Using tools to get information")
    print("  - Synthesis: Combining results into answers")

def demo_tools_directly():
    """Demo the tools working directly"""
    print("\n🛠️ Direct Tool Testing:")
    print("-" * 30)
    
    tools = get_tools()
    
    # Test each tool
    test_cases = [
        ("Web Search", tools[0], "machine learning"),
        ("Calculator", tools[1], "2 + 3 * 4"),
        ("Weather", tools[2], "Tokyo")
    ]
    
    for name, tool, input_data in test_cases:
        print(f"\n🔧 Testing {name}:")
        print(f"  Input: {input_data}")
        result = tool.run(input_data)
        print(f"  Result: {result}")

if __name__ == "__main__":
    simulate_agentic_ai()
    demo_tools_directly()
    print("\n🎉 Demo completed! The agentic AI concepts are working!")
