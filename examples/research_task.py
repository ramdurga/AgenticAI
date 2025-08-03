"""
Research Task Example - Agentic AI for Dummies
Demonstrates advanced research capabilities of the agentic AI system
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agent import Agent, Task, Plan, Result
from tools import web_search, file_operations


def comprehensive_research_example():
    """Example of comprehensive research with multiple steps"""
    print("🔬 Comprehensive Research Example")
    print("=" * 60)
    
    # Create a more complex research task
    task_description = """
    Research the impact of artificial intelligence on job markets:
    1. Find current statistics on AI adoption in different industries
    2. Identify jobs most at risk from automation
    3. Discover new job opportunities created by AI
    4. Analyze the skills needed for the future workforce
    5. Provide recommendations for career planning
    """
    
    print(f"Task: {task_description.strip()}")
    print()
    
    # Create agent
    agent = Agent("ResearchAgent", personality="thorough")
    
    # Analyze the task
    task = agent.analyze_task(task_description)
    print(f"📋 Task Analysis:")
    print(f"  Goal: {task.goal}")
    print(f"  Constraints: {task.constraints}")
    print(f"  Success Criteria: {task.success_criteria}")
    print()
    
    # Create detailed plan
    plan = agent.create_plan()
    print(f"📋 Research Plan:")
    for i, step in enumerate(plan.steps, 1):
        print(f"  {i}. {step}")
    print(f"  Estimated Time: {plan.estimated_time}")
    print(f"  Risk Level: {plan.risk_level}")
    print()
    
    # Execute the plan
    print("🚀 Executing Research Plan...")
    result = agent.execute_plan(plan)
    
    # Display detailed results
    print("\n📊 Research Results:")
    print(f"  ✅ Success: {result.success}")
    print(f"  ⏱️  Execution Time: {result.execution_time:.2f} seconds")
    
    print("\n📝 Detailed Output:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n🧠 Key Learnings:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    if result.errors:
        print(f"\n❌ Errors Encountered:")
        for error in result.errors:
            print(f"  • {error}")
    
    # Learn from results
    agent.learn_from_results(result)
    
    print()


def multi_source_research_example():
    """Example of research using multiple sources and tools"""
    print("📚 Multi-Source Research Example")
    print("=" * 60)
    
    # Define research topics
    research_topics = [
        "machine learning applications in healthcare",
        "renewable energy trends 2024",
        "cybersecurity best practices for small businesses"
    ]
    
    agent = Agent("MultiSourceAgent", personality="analytical")
    
    all_results = []
    
    for i, topic in enumerate(research_topics, 1):
        print(f"\n🔍 Research Topic {i}: {topic}")
        print("-" * 50)
        
        # Create task
        task = agent.analyze_task(f"Research {topic} and provide comprehensive insights")
        
        # Create plan
        plan = agent.create_plan()
        
        # Execute
        result = agent.execute_plan(plan)
        
        # Store results
        all_results.append({
            "topic": topic,
            "result": result
        })
        
        print(f"  ✅ Success: {result.success}")
        print(f"  ⏱️  Time: {result.execution_time:.2f}s")
        
        if result.learnings:
            print(f"  🧠 Key Insight: {result.learnings[0] if result.learnings else 'N/A'}")
    
    # Synthesize all research
    print(f"\n📊 Research Synthesis:")
    print(f"  Total Topics Researched: {len(research_topics)}")
    print(f"  Successful Researches: {sum(1 for r in all_results if r['result'].success)}")
    print(f"  Total Time: {sum(r['result'].execution_time for r in all_results):.2f}s")
    
    # Show agent's learning progress
    status = agent.get_status()
    print(f"\n🤖 Agent Learning Progress:")
    print(f"  Confidence Level: {status['confidence_level']:.2f}")
    print(f"  Success Rate: {status['success_rate']:.2f}")
    print(f"  Memory Episodes: {status['memory_size']['episodic']}")
    
    print()


def comparative_research_example():
    """Example of comparative research between different options"""
    print("⚖️ Comparative Research Example")
    print("=" * 60)
    
    # Define comparison criteria
    comparison_task = """
    Compare different programming languages for web development:
    - JavaScript vs Python vs Ruby
    - Consider: learning curve, job market, community support, performance
    - Provide recommendations for different use cases
    """
    
    print(f"Task: {comparison_task.strip()}")
    print()
    
    agent = Agent("ComparisonAgent", personality="balanced")
    
    # Analyze task
    task = agent.analyze_task(comparison_task)
    
    # Create comparison plan
    plan = agent.create_plan()
    
    # Execute comparison
    result = agent.execute_plan(plan)
    
    # Display comparison results
    print("📊 Comparison Results:")
    print(f"  ✅ Analysis Complete: {result.success}")
    print(f"  ⏱️  Analysis Time: {result.execution_time:.2f} seconds")
    
    print("\n📋 Comparison Output:")
    for step_key, step_output in result.output.items():
        print(f"  {step_key}: {step_output}")
    
    if result.learnings:
        print(f"\n💡 Key Insights:")
        for learning in result.learnings:
            print(f"  • {learning}")
    
    print()


def research_with_documentation():
    """Example of research that creates documentation"""
    print("📝 Research with Documentation Example")
    print("=" * 60)
    
    research_task = "Research the history of artificial intelligence and create a comprehensive report"
    
    print(f"Task: {research_task}")
    print()
    
    agent = Agent("DocumentationAgent", personality="detailed")
    
    # Run the research
    result = run_agent_task(research_task, "DocumentationAgent")
    
    # Create documentation
    if result.success:
        print("📄 Creating Research Report...")
        
        # Simulate creating a report
        report_content = f"""
# AI History Research Report

## Executive Summary
This report provides a comprehensive overview of artificial intelligence history.

## Key Findings
- AI has evolved significantly since the 1950s
- Multiple AI winters and springs have occurred
- Current AI renaissance is driven by big data and computing power

## Methodology
Research conducted using multiple sources and analysis tools.

## Recommendations
- Continue monitoring AI developments
- Invest in AI education and training
- Consider ethical implications of AI

## Research Details
Execution Time: {result.execution_time:.2f} seconds
Success Rate: {result.success}
Learnings: {len(result.learnings)} key insights gained

Generated by: Agentic AI System
Date: {result.execution_time}
        """
        
        # Write report to file
        file_ops = file_operations()
        report_path = "ai_history_research_report.md"
        write_result = file_ops.write_file(report_path, report_content)
        
        print(f"✅ Report created: {report_path}")
        print(f"📄 File operation: {write_result}")
        
        # Show report preview
        print("\n📋 Report Preview:")
        lines = report_content.split('\n')[:10]
        for line in lines:
            print(f"  {line}")
        print("  ...")
    
    print()


def interactive_research_demo():
    """Interactive research demo"""
    print("🎮 Interactive Research Demo")
    print("=" * 60)
    print("Enter research topics and watch the agent investigate!")
    print("Type 'quit' to exit")
    print()
    
    agent = Agent("InteractiveResearchAgent")
    
    while True:
        try:
            # Get research topic
            topic = input("🔍 Enter a research topic: ").strip()
            
            if topic.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not topic:
                print("⚠️ Please enter a research topic!")
                continue
            
            print(f"\n🚀 Researching: {topic}")
            print("-" * 40)
            
            # Create research task
            research_task = f"Research {topic} and provide detailed insights with sources"
            
            # Run research
            result = run_agent_task(research_task, "InteractiveResearchAgent")
            
            # Display results
            print("\n📊 Research Results:")
            print(f"  ✅ Success: {result.success}")
            print(f"  ⏱️  Time: {result.execution_time:.2f} seconds")
            print(f"  📝 Output: {result.output}")
            
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
    """Main function to run research examples"""
    print("🔬 Agentic AI Research Examples")
    print("=" * 70)
    print()
    
    # Run research examples
    comprehensive_research_example()
    multi_source_research_example()
    comparative_research_example()
    research_with_documentation()
    
    # Ask for interactive demo
    print("🎮 Would you like to try the interactive research demo? (y/n): ", end="")
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            print()
            interactive_research_demo()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    
    print("\n🎉 Research examples completed!")
    print("💡 The agent can now handle complex research tasks!")


if __name__ == "__main__":
    main() 