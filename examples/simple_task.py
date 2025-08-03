"""
Simple Task Example - Agentic AI for Dummies
Demonstrates basic usage of the agentic AI system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import Agent, run_agent_task


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
    
    if result.learnings:
        print(f"  🧠 Learnings: {result.learnings}")
        
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
    
    if result.learnings:
        print(f"  🧠 Learnings: {result.learnings}")
        
    print()


def interactive_agent_demo():
    """Interactive demo where user can input their own tasks"""
    print("🎮 Interactive Agent Demo")
    print("=" * 50)
    print("Enter your own tasks and watch the agent work!")
    print("Type 'quit' to exit")
    print()
    
    agent = Agent("InteractiveAgent")
    
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
                
            if result.learnings:
                print(f"  🧠 Learnings: {result.learnings}")
                
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
    print(f"  Confidence: {status['confidence_level']:.2f}")
    print(f"  Success Rate: {status['success_rate']:.2f}")
    print(f"  Tasks Completed: {status['tasks_completed']}")
    print(f"  Memory Size:")
    print(f"    - Short-term: {status['memory_size']['short_term']}")
    print(f"    - Long-term: {status['memory_size']['long_term']}")
    print(f"    - Episodic: {status['memory_size']['episodic']}")
    
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