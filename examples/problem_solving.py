"""
Problem Solving Example - Agentic AI for Dummies
Demonstrates how the agentic AI system can solve complex problems
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import Agent, Task, Plan, Result
from tools import calculator, file_operations


def mathematical_problem_solving():
    """Example of solving mathematical problems"""
    print("🧮 Mathematical Problem Solving")
    print("=" * 60)
    
    # Define mathematical problems
    problems = [
        "Calculate the compound interest for $1000 invested at 5% for 10 years",
        "Find the area of a circle with radius 7 units",
        "Solve the equation: 2x + 5 = 13",
        "Calculate the factorial of 8"
    ]
    
    agent = Agent("MathAgent", personality="precise")
    
    for i, problem in enumerate(problems, 1):
        print(f"\n🔢 Problem {i}: {problem}")
        print("-" * 50)
        
        # Analyze the problem
        task = agent.analyze_task(problem)
        
        # Create solution plan
        plan = agent.create_plan()
        
        # Execute solution
        result = agent.execute_plan(plan)
        
        print(f"  ✅ Solved: {result.success}")
        print(f"  ⏱️  Time: {result.execution_time:.2f}s")
        print(f"  📝 Solution: {result.output}")
        
        if result.learnings:
            print(f"  🧠 Learning: {result.learnings[0]}")
    
    print()


def optimization_problem():
    """Example of solving optimization problems"""
    print("⚡ Optimization Problem Solving")
    print("=" * 60)
    
    optimization_task = """
    Optimize a delivery route for a delivery company:
    - 5 delivery locations with different distances
    - Each location has different time windows
    - Minimize total travel time
    - Consider fuel costs and vehicle capacity
    - Provide the optimal route sequence
    """
    
    print(f"Task: {optimization_task.strip()}")
    print()
    
    agent = Agent("OptimizationAgent", personality="analytical")
    
    # Analyze the optimization problem
    task = agent.analyze_task(optimization_task)
    
    # Create optimization plan
    plan = agent.create_plan()
    
    print("📋 Optimization Plan:")
    for i, step in enumerate(plan.steps, 1):
        print(f"  {i}. {step}")
    print()
    
    # Execute optimization
    result = agent.execute_plan(plan)
    
    print("📊 Optimization Results:")
    print(f"  ✅ Optimization Complete: {result.success}")
    print(f"  ⏱️  Computation Time: {result.execution_time:.2f} seconds")
    
    print("\n📋 Solution Details:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n💡 Optimization Insights:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def debugging_problem():
    """Example of debugging and problem diagnosis"""
    print("🐛 Debugging Problem Example")
    print("=" * 60)
    
    # Simulate a buggy scenario
    buggy_code = """
    def calculate_average(numbers):
        total = 0
        for num in numbers:
            total += num
        return total / len(numbers)  # Potential division by zero
    
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],  # Should work
        [],                 # Will cause error
        [10],              # Should work
        None               # Will cause error
    ]
    """
    
    debugging_task = f"""
    Debug the following code and identify potential issues:
    {buggy_code}
    
    Identify:
    1. Potential runtime errors
    2. Edge cases that might fail
    3. Improvements for robustness
    4. Test cases to verify fixes
    """
    
    print(f"Task: Debug and improve the code")
    print()
    
    agent = Agent("DebugAgent", personality="thorough")
    
    # Analyze the debugging task
    task = agent.analyze_task(debugging_task)
    
    # Create debugging plan
    plan = agent.create_plan()
    
    # Execute debugging
    result = agent.execute_plan(plan)
    
    print("📊 Debugging Results:")
    print(f"  ✅ Analysis Complete: {result.success}")
    print(f"  ⏱️  Analysis Time: {result.execution_time:.2f} seconds")
    
    print("\n🐛 Issues Found:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n🔧 Suggested Fixes:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def system_design_problem():
    """Example of system design problem solving"""
    print("🏗️ System Design Problem")
    print("=" * 60)
    
    design_task = """
    Design a scalable web application architecture:
    - Handle 1 million daily users
    - Support real-time messaging
    - Ensure 99.9% uptime
    - Consider cost optimization
    - Plan for future scaling
    
    Provide:
    1. High-level architecture diagram
    2. Technology stack recommendations
    3. Database design considerations
    4. Security considerations
    5. Monitoring and logging strategy
    """
    
    print(f"Task: {design_task.strip()}")
    print()
    
    agent = Agent("DesignAgent", personality="creative")
    
    # Analyze the design problem
    task = agent.analyze_task(design_task)
    
    # Create design plan
    plan = agent.create_plan()
    
    print("📋 Design Process:")
    for i, step in enumerate(plan.steps, 1):
        print(f"  {i}. {step}")
    print()
    
    # Execute design process
    result = agent.execute_plan(plan)
    
    print("📊 Design Results:")
    print(f"  ✅ Design Complete: {result.success}")
    print(f"  ⏱️  Design Time: {result.execution_time:.2f} seconds")
    
    print("\n🏗️ Architecture Components:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n💡 Design Insights:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def data_analysis_problem():
    """Example of data analysis problem solving"""
    print("📊 Data Analysis Problem")
    print("=" * 60)
    
    analysis_task = """
    Analyze customer behavior data to improve business decisions:
    
    Dataset includes:
    - Customer purchase history
    - Website browsing patterns
    - Customer demographics
    - Product preferences
    - Seasonal trends
    
    Goals:
    1. Identify customer segments
    2. Predict customer lifetime value
    3. Recommend product improvements
    4. Optimize marketing strategies
    5. Forecast sales trends
    """
    
    print(f"Task: {analysis_task.strip()}")
    print()
    
    agent = Agent("DataAgent", personality="analytical")
    
    # Analyze the data problem
    task = agent.analyze_task(analysis_task)
    
    # Create analysis plan
    plan = agent.create_plan()
    
    # Execute analysis
    result = agent.execute_plan(plan)
    
    print("📊 Analysis Results:")
    print(f"  ✅ Analysis Complete: {result.success}")
    print(f"  ⏱️  Analysis Time: {result.execution_time:.2f} seconds")
    
    print("\n📈 Key Findings:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n💡 Business Insights:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def creative_problem_solving():
    """Example of creative problem solving"""
    print("🎨 Creative Problem Solving")
    print("=" * 60)
    
    creative_task = """
    Design an innovative solution for reducing food waste:
    
    Constraints:
    - Must be cost-effective
    - Should work in urban environments
    - Consider different user groups
    - Address multiple aspects of food waste
    
    Deliverables:
    1. Problem analysis and root causes
    2. Innovative solution concept
    3. Implementation strategy
    4. Success metrics
    5. Potential challenges and solutions
    """
    
    print(f"Task: {creative_task.strip()}")
    print()
    
    agent = Agent("CreativeAgent", personality="innovative")
    
    # Analyze the creative problem
    task = agent.analyze_task(creative_task)
    
    # Create creative solution plan
    plan = agent.create_plan()
    
    # Execute creative process
    result = agent.execute_plan(plan)
    
    print("📊 Creative Solution Results:")
    print(f"  ✅ Solution Designed: {result.success}")
    print(f"  ⏱️  Design Time: {result.execution_time:.2f} seconds")
    
    print("\n💡 Solution Components:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n🎯 Innovation Insights:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def interactive_problem_solver():
    """Interactive problem solver demo"""
    print("🎮 Interactive Problem Solver")
    print("=" * 60)
    print("Describe a problem and watch the agent solve it!")
    print("Type 'quit' to exit")
    print()
    
    agent = Agent("InteractiveSolverAgent")
    
    while True:
        try:
            # Get problem description
            problem = input("🤔 Describe a problem to solve: ").strip()
            
            if problem.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not problem:
                print("⚠️ Please describe a problem!")
                continue
            
            print(f"\n🚀 Agent is solving: {problem}")
            print("-" * 40)
            
            # Create problem-solving task
            solving_task = f"Solve the following problem: {problem}. Provide a step-by-step solution with explanations."
            
            # Run problem solving
            result = run_agent_task(solving_task, "InteractiveSolverAgent")
            
            # Display results
            print("\n📊 Solution Results:")
            print(f"  ✅ Solved: {result.success}")
            print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
            print(f"  📝 Solution: {result.output}")
            
            if result.learnings:
                print(f"  🧠 Key Insights:")
                for learning in result.learnings:
                    print(f"    • {learning}")
            
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print()


def main():
    """Main function to run problem-solving examples"""
    print("🧩 Agentic AI Problem Solving Examples")
    print("=" * 70)
    print()
    
    # Run problem-solving examples
    mathematical_problem_solving()
    optimization_problem()
    debugging_problem()
    system_design_problem()
    data_analysis_problem()
    creative_problem_solving()
    
    # Ask for interactive demo
    print("🎮 Would you like to try the interactive problem solver? (y/n): ", end="")
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            print()
            interactive_problem_solver()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    
    print("\n🎉 Problem-solving examples completed!")
    print("💡 The agent can now tackle complex problems systematically!")


if __name__ == "__main__":
    main() 