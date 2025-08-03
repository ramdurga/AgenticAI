"""
Simple Task Example - Agentic AI for Dummies
Demonstrates basic usage of the agentic AI system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import Agent
from tools import web_search, calculator, data_analyzer, file_operations, code_executor, text_processor


def run_agent_task(task_description: str, agent_name: str = "Agent") -> object:
    """
    Convenience function to create an agent and run a task
    """
    agent = Agent(name=agent_name)
    
    # Register tools
    agent.register_tool("web_search", web_search)
    agent.register_tool("calculator", calculator)
    agent.register_tool("data_analyzer", data_analyzer)
    agent.register_tool("file_operations", file_operations)
    agent.register_tool("code_executor", code_executor)
    agent.register_tool("text_processor", text_processor)
    
    # Analyze the task
    task = agent.analyze_task(task_description)
    
    # Create a plan
    plan = agent.create_plan(task)
    
    # Execute the plan
    result = agent.execute_plan(task, plan)
    
    return result


def simple_research_example():
    """Example 1: Simple research task"""
    print("🔍 Example 1: Simple Research Task")
    print("=" * 50)
    
    task = "Find information about Python programming for beginners"
    
    print(f"Task: {task}")
    print()
    
    # Run the task
    result = run_agent_task(task, "ResearchAgent")
    
    # Display results
    print("📊 Results:")
    print(f"  ✅ Success: {result.success}")
    print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
    print(f"  📝 Output: {result.output}")
    
    if result.errors:
        print(f"  ❌ Errors: {result.errors}")
        
    print()


def coding_task_example():
    """Example 2: Coding task"""
    print("💻 Example 2: Coding Task")
    print("=" * 50)
    
    task = "Create a simple Python function to calculate the factorial of a number"
    
    print(f"Task: {task}")
    print()
    
    # Run the task
    result = run_agent_task(task, "CodeAgent")
    
    # Display results
    print("📊 Results:")
    print(f"  ✅ Success: {result.success}")
    print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
    print(f"  📝 Output: {result.output}")
    
    if result.errors:
        print(f"  ❌ Errors: {result.errors}")
        
    print()


def data_analysis_example():
    """Example 3: Data analysis task"""
    print("📊 Example 3: Data Analysis Task")
    print("=" * 50)
    
    task = "Analyze a dataset of student grades and provide insights"
    
    print(f"Task: {task}")
    print()
    
    # Run the task
    result = run_agent_task(task, "DataAgent")
    
    # Display results
    print("📊 Results:")
    print(f"  ✅ Success: {result.success}")
    print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
    print(f"  📝 Output: {result.output}")
    
    if result.errors:
        print(f"  ❌ Errors: {result.errors}")
        
    print()


def interactive_agent_demo():
    """Interactive demo where user can input their own tasks"""
    print("🎮 Interactive Agent Demo")
    print("=" * 50)
    print("Enter your own tasks and watch the agent work!")
    print("Type 'quit' to exit")
    print()
    
    agent = Agent("InteractiveAgent")
    
    # Register tools
    agent.register_tool("web_search", web_search)
    agent.register_tool("calculator", calculator)
    agent.register_tool("data_analyzer", data_analyzer)
    agent.register_tool("file_operations", file_operations)
    agent.register_tool("code_executor", code_executor)
    agent.register_tool("text_processor", text_processor)
    
    while True:
        try:
            # Get user input
            user_task = input("🤖 Enter a task for the agent: ").strip()
            
            if user_task.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not user_task:
                print("⚠️ Please enter a task!")
                continue
                
            print(f"\n🚀 Agent is working on: {user_task}")
            print("-" * 40)
            
            # Run the task
            result = run_agent_task(user_task, "InteractiveAgent")
            
            # Display results
            print("\n📊 Results:")
            print(f"  ✅ Success: {result.success}")
            print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
            print(f"  📝 Output: {result.output}")
            
            if result.errors:
                print(f"  ❌ Errors: {result.errors}")
                
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print()


def agent_status_demo():
    """Demo showing agent status and memory"""
    print("📊 Agent Status Demo")
    print("=" * 50)
    
    agent = Agent("StatusDemoAgent")
    
    # Register tools
    agent.register_tool("web_search", web_search)
    agent.register_tool("calculator", calculator)
    agent.register_tool("data_analyzer", data_analyzer)
    agent.register_tool("file_operations", file_operations)
    agent.register_tool("code_executor", code_executor)
    agent.register_tool("text_processor", text_processor)
    
    # Run a few tasks to build up memory
    tasks = [
        "Research machine learning basics",
        "Find information about data science",
        "Analyze programming trends"
    ]
    
    for i, task in enumerate(tasks, 1):
        print(f"\n🔄 Task {i}: {task}")
        result = run_agent_task(task, "StatusDemoAgent")
        print(f"  ✅ Success: {result.success}")
        
    # Show agent status
    status = agent.get_status()
    print(f"\n📊 Agent Status:")
    print(f"  Name: {status['name']}")
    print(f"  Personality: {status['personality']}")
    print(f"  Learning Rate: {status['learning_rate']:.2f}")
    print(f"  Tools Available: {status['tools_available']}")
    print(f"  Memory Stats:")
    print(f"    - Short-term: {status['memory_stats']['short_term_count']}")
    print(f"    - Long-term: {status['memory_stats']['long_term_count']}")
    print(f"    - Episodic: {status['memory_stats']['episodic_count']}")
    
    print()


def main():
    """Main function to run all examples"""
    print("🤖 Agentic AI for Dummies - Examples")
    print("=" * 60)
    print()
    
    # Run the examples
    simple_research_example()
    coding_task_example()
    data_analysis_example()
    agent_status_demo()
    
    # Ask if user wants interactive demo
    print("🎮 Would you like to try the interactive demo? (y/n): ", end="")
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            print()
            interactive_agent_demo()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    
    print("\n🎉 All examples completed!")
    print("💡 Try modifying the tasks or creating your own agent!")


if __name__ == "__main__":
    main() 