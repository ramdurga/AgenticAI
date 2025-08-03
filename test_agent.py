#!/usr/bin/env python3
"""
Simple test script for the Agentic AI system
"""

import sys
import os

# Add the current directory to the path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agent import Agent, run_agent_task
from tools import web_search, file_operations, calculator


def test_basic_agent():
    """Test basic agent functionality"""
    print("🧪 Testing Basic Agent Functionality")
    print("=" * 50)
    
    # Create an agent
    agent = Agent("TestAgent")
    
    # Test agent status
    status = agent.get_status()
    print(f"✅ Agent created: {status['name']}")
    print(f"   Personality: {status['personality']}")
    print(f"   Confidence: {status['confidence_level']:.2f}")
    
    return True


def test_simple_task():
    """Test a simple task execution"""
    print("\n🧪 Testing Simple Task Execution")
    print("=" * 50)
    
    task = "Find information about Python programming"
    
    print(f"Task: {task}")
    
    # Run the task
    result = run_agent_task(task, "TestAgent")
    
    print(f"✅ Success: {result.success}")
    print(f"⏱️  Time: {result.execution_time:.2f}s")
    print(f"📝 Output: {result.output}")
    
    return result.success


def test_tools():
    """Test individual tools"""
    print("\n🧪 Testing Tools")
    print("=" * 50)
    
    # Test web search
    print("🔍 Testing web search...")
    search_results = web_search("Python programming")
    print(f"   Found {len(search_results)} results")
    
    # Test calculator
    print("🧮 Testing calculator...")
    calc_result = calculator("2 + 3 * 4")
    print(f"   Result: {calc_result}")
    
    # Test file operations
    print("📁 Testing file operations...")
    file_ops = file_operations()
    test_content = "This is a test file created by the agentic AI system."
    write_result = file_ops.write_file("test_output.txt", test_content)
    print(f"   Write result: {write_result}")
    
    return True


def test_agent_learning():
    """Test agent learning capabilities"""
    print("\n🧪 Testing Agent Learning")
    print("=" * 50)
    
    agent = Agent("LearningAgent")
    
    # Run multiple tasks to test learning
    tasks = [
        "Research machine learning basics",
        "Find information about data science",
        "Analyze programming trends"
    ]
    
    for i, task in enumerate(tasks, 1):
        print(f"Task {i}: {task}")
        result = run_agent_task(task, "LearningAgent")
        print(f"  Success: {result.success}")
    
    # Check learning progress
    status = agent.get_status()
    print(f"\n📊 Learning Progress:")
    print(f"  Tasks completed: {status['tasks_completed']}")
    print(f"  Success rate: {status['success_rate']:.2f}")
    print(f"  Confidence: {status['confidence_level']:.2f}")
    print(f"  Memory episodes: {status['memory_size']['episodic']}")
    
    return True


def test_different_personalities():
    """Test different agent personalities"""
    print("\n🧪 Testing Different Personalities")
    print("=" * 50)
    
    personalities = ["helpful", "analytical", "creative", "thorough"]
    
    for personality in personalities:
        print(f"\nTesting {personality} personality:")
        agent = Agent(f"{personality.capitalize()}Agent", personality=personality)
        
        task = "Research artificial intelligence trends"
        result = run_agent_task(task, f"{personality.capitalize()}Agent")
        
        print(f"  Success: {result.success}")
        print(f"  Time: {result.execution_time:.2f}s")
        print(f"  Learnings: {len(result.learnings)}")
    
    return True


def run_all_tests():
    """Run all tests"""
    print("🚀 Agentic AI System Tests")
    print("=" * 60)
    print()
    
    tests = [
        ("Basic Agent", test_basic_agent),
        ("Simple Task", test_simple_task),
        ("Tools", test_tools),
        ("Agent Learning", test_agent_learning),
        ("Different Personalities", test_different_personalities)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            print(f"🧪 Running {test_name} test...")
            result = test_func()
            if result:
                print(f"✅ {test_name} test passed!")
                passed += 1
            else:
                print(f"❌ {test_name} test failed!")
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
    
    print(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The agentic AI system is working correctly.")
    else:
        print("⚠️ Some tests failed. Please check the implementation.")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1) 