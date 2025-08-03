"""
Agentic AI Agent - A simple implementation for beginners
"""

import json
import logging
import time
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from datetime import datetime
import os
from pathlib import Path

# Import our tools
from tools import ToolRegistry, web_search, file_operations, code_executor, data_analyzer

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Task:
    """Represents a task for the agent to complete"""
    goal: str
    constraints: List[str] = None
    success_criteria: List[str] = None
    priority: str = "medium"
    created_at: datetime = None
    
    def __post_init__(self):
        if self.constraints is None:
            self.constraints = []
        if self.success_criteria is None:
            self.success_criteria = []
        if self.created_at is None:
            self.created_at = datetime.now()


@dataclass
class Plan:
    """Represents a plan with steps to achieve a goal"""
    steps: List[str]
    estimated_time: str
    resources_needed: List[str]
    risk_level: str = "medium"


@dataclass
class Result:
    """Represents the result of a task execution"""
    success: bool
    output: Any
    execution_time: float
    errors: List[str] = None
    learnings: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.learnings is None:
            self.learnings = []


class Memory:
    """Simple memory system for the agent"""
    
    def __init__(self):
        self.short_term = {}  # Current task context
        self.long_term = {}   # Learned patterns
        self.episodic = []    # Task memories
        
    def store_short_term(self, key: str, value: Any):
        """Store information for current task"""
        self.short_term[key] = value
        
    def get_short_term(self, key: str) -> Any:
        """Retrieve short-term memory"""
        return self.short_term.get(key)
        
    def store_long_term(self, pattern: str, outcome: str):
        """Store learned patterns"""
        self.long_term[pattern] = outcome
        
    def get_long_term(self, pattern: str) -> Optional[str]:
        """Retrieve long-term memory"""
        return self.long_term.get(pattern)
        
    def store_episode(self, task: Task, result: Result):
        """Store a completed task episode"""
        episode = {
            "task": task,
            "result": result,
            "timestamp": datetime.now()
        }
        self.episodic.append(episode)
        
    def get_similar_episodes(self, task_goal: str) -> List[Dict]:
        """Find similar past episodes"""
        # Simple keyword matching for now
        similar = []
        for episode in self.episodic:
            if any(word in episode["task"].goal.lower() 
                   for word in task_goal.lower().split()):
                similar.append(episode)
        return similar


class Agent:
    """
    A simple agentic AI agent that can:
    - Analyze tasks
    - Create plans
    - Execute plans
    - Learn from results
    """
    
    def __init__(self, name: str = "Agent", personality: str = "helpful"):
        self.name = name
        self.personality = personality
        self.memory = Memory()
        self.tools = ToolRegistry()
        self.current_task = None
        self.current_plan = None
        
        # Agent state
        self.is_busy = False
        self.confidence_level = 0.5
        self.success_rate = 0.0
        self.tasks_completed = 0
        
        logger.info(f"🤖 {self.name} initialized with {self.personality} personality")
        
    def analyze_task(self, task_input: str) -> Task:
        """
        Analyze a task and create a structured Task object
        """
        logger.info(f"🔍 Analyzing task: {task_input}")
        
        # Simple task analysis (in a real system, this would use NLP)
        task = Task(goal=task_input)
        
        # Extract constraints and success criteria based on keywords
        if "research" in task_input.lower():
            task.constraints.append("Must use reliable sources")
            task.success_criteria.append("Provide comprehensive summary")
            task.success_criteria.append("Include multiple perspectives")
            
        if "code" in task_input.lower() or "program" in task_input.lower():
            task.constraints.append("Code must be functional")
            task.success_criteria.append("Include comments and documentation")
            
        if "analyze" in task_input.lower() or "data" in task_input.lower():
            task.constraints.append("Use appropriate analysis methods")
            task.success_criteria.append("Provide clear insights")
            
        self.current_task = task
        self.memory.store_short_term("current_task", task)
        
        logger.info(f"✅ Task analyzed: {len(task.constraints)} constraints, {len(task.success_criteria)} success criteria")
        return task
        
    def create_plan(self) -> Plan:
        """
        Create a plan to achieve the current task
        """
        if not self.current_task:
            raise ValueError("No current task to plan for")
            
        logger.info(f"📋 Creating plan for: {self.current_task.goal}")
        
        # Check memory for similar tasks
        similar_episodes = self.memory.get_similar_episodes(self.current_task.goal)
        
        steps = []
        if similar_episodes:
            # Use learned patterns
            logger.info(f"📚 Found {len(similar_episodes)} similar past experiences")
            steps = self._create_plan_from_experience(similar_episodes)
        else:
            # Create new plan based on task type
            steps = self._create_plan_from_scratch()
            
        plan = Plan(
            steps=steps,
            estimated_time="5-15 minutes",
            resources_needed=["Internet access", "Basic tools"],
            risk_level="low"
        )
        
        self.current_plan = plan
        self.memory.store_short_term("current_plan", plan)
        
        logger.info(f"✅ Plan created with {len(steps)} steps")
        return plan
        
    def _create_plan_from_experience(self, episodes: List[Dict]) -> List[str]:
        """Create plan based on past successful experiences"""
        # For now, use a simple approach
        return [
            "1. Review past successful approaches",
            "2. Adapt proven strategies to current task",
            "3. Execute with learned optimizations",
            "4. Document new learnings"
        ]
        
    def _create_plan_from_scratch(self) -> List[str]:
        """Create a new plan from scratch"""
        task_goal = self.current_task.goal.lower()
        
        if "research" in task_goal:
            return [
                "1. Define research scope and objectives",
                "2. Search for relevant information sources",
                "3. Gather and evaluate information",
                "4. Synthesize findings into coherent summary",
                "5. Present results with recommendations"
            ]
        elif "code" in task_goal or "program" in task_goal:
            return [
                "1. Understand requirements and constraints",
                "2. Design solution architecture",
                "3. Implement core functionality",
                "4. Test and debug code",
                "5. Document and optimize"
            ]
        elif "analyze" in task_goal or "data" in task_goal:
            return [
                "1. Understand data structure and format",
                "2. Clean and prepare data",
                "3. Apply appropriate analysis methods",
                "4. Generate insights and visualizations",
                "5. Present findings and recommendations"
            ]
        else:
            # Generic plan
            return [
                "1. Understand the problem",
                "2. Break down into manageable steps",
                "3. Execute each step systematically",
                "4. Verify results meet requirements",
                "5. Document process and outcomes"
            ]
            
    def execute_plan(self, plan: Optional[Plan] = None) -> Result:
        """
        Execute the current plan step by step
        """
        if plan is None:
            plan = self.current_plan
            
        if not plan:
            raise ValueError("No plan to execute")
            
        logger.info(f"🚀 Executing plan with {len(plan.steps)} steps")
        
        start_time = time.time()
        errors = []
        learnings = []
        output = {}
        
        self.is_busy = True
        
        try:
            for i, step in enumerate(plan.steps, 1):
                logger.info(f"📝 Step {i}: {step}")
                
                # Execute the step (simplified for demo)
                step_result = self._execute_step(step)
                
                if step_result.get("success"):
                    output[f"step_{i}"] = step_result["output"]
                    if step_result.get("learning"):
                        learnings.append(step_result["learning"])
                else:
                    errors.append(f"Step {i} failed: {step_result.get('error', 'Unknown error')}")
                    
                # Small delay to simulate processing
                time.sleep(0.5)
                
        except Exception as e:
            errors.append(f"Execution failed: {str(e)}")
            
        finally:
            self.is_busy = False
            
        execution_time = time.time() - start_time
        success = len(errors) == 0
        
        result = Result(
            success=success,
            output=output,
            execution_time=execution_time,
            errors=errors,
            learnings=learnings
        )
        
        # Update agent statistics
        self.tasks_completed += 1
        if success:
            self.success_rate = (self.success_rate * (self.tasks_completed - 1) + 1) / self.tasks_completed
        else:
            self.success_rate = (self.success_rate * (self.tasks_completed - 1)) / self.tasks_completed
            
        logger.info(f"✅ Plan execution completed. Success: {success}, Time: {execution_time:.2f}s")
        return result
        
    def _execute_step(self, step: str) -> Dict[str, Any]:
        """
        Execute a single step of the plan
        """
        step_lower = step.lower()
        
        # Simple step execution logic
        if "search" in step_lower or "find" in step_lower:
            return self._execute_search_step(step)
        elif "analyze" in step_lower or "process" in step_lower:
            return self._execute_analysis_step(step)
        elif "code" in step_lower or "implement" in step_lower:
            return self._execute_code_step(step)
        elif "document" in step_lower or "present" in step_lower:
            return self._execute_documentation_step(step)
        else:
            return self._execute_generic_step(step)
            
    def _execute_search_step(self, step: str) -> Dict[str, Any]:
        """Execute a search-related step"""
        try:
            # Simulate web search
            search_query = self._extract_search_query(step)
            results = web_search(search_query)
            return {
                "success": True,
                "output": f"Found {len(results)} relevant results for '{search_query}'",
                "learning": "Web search is effective for gathering information"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def _execute_analysis_step(self, step: str) -> Dict[str, Any]:
        """Execute an analysis-related step"""
        try:
            # Simulate data analysis
            analysis_result = data_analyzer("sample_data")
            return {
                "success": True,
                "output": f"Analysis completed: {analysis_result}",
                "learning": "Systematic analysis reveals important patterns"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def _execute_code_step(self, step: str) -> Dict[str, Any]:
        """Execute a coding-related step"""
        try:
            # Simulate code execution
            code_result = code_executor("print('Hello, World!')")
            return {
                "success": True,
                "output": f"Code executed successfully: {code_result}",
                "learning": "Incremental development helps catch errors early"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def _execute_documentation_step(self, step: str) -> Dict[str, Any]:
        """Execute a documentation-related step"""
        try:
            # Simulate documentation
            doc_result = file_operations.write_file("output.txt", "Task completed successfully")
            return {
                "success": True,
                "output": f"Documentation created: {doc_result}",
                "learning": "Good documentation helps future tasks"
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
            
    def _execute_generic_step(self, step: str) -> Dict[str, Any]:
        """Execute a generic step"""
        return {
            "success": True,
            "output": f"Completed: {step}",
            "learning": "Systematic approach leads to better results"
        }
        
    def _extract_search_query(self, step: str) -> str:
        """Extract search query from step description"""
        # Simple extraction - in reality, this would use NLP
        words = step.split()
        if "for" in words:
            for_idx = words.index("for")
            return " ".join(words[for_idx + 1:])
        return "relevant information"
        
    def learn_from_results(self, result: Result):
        """
        Learn from the execution results and update memory
        """
        logger.info(f"🧠 Learning from results (success: {result.success})")
        
        if self.current_task:
            # Store the episode in memory
            self.memory.store_episode(self.current_task, result)
            
            # Extract patterns for long-term memory
            if result.success:
                pattern = f"Task type: {self._classify_task(self.current_task.goal)}"
                outcome = "successful"
                self.memory.store_long_term(pattern, outcome)
                
                # Update confidence based on success
                self.confidence_level = min(1.0, self.confidence_level + 0.1)
            else:
                # Learn from failures
                for error in result.errors:
                    pattern = f"Error: {error}"
                    outcome = "avoid"
                    self.memory.store_long_term(pattern, outcome)
                    
                # Decrease confidence slightly
                self.confidence_level = max(0.0, self.confidence_level - 0.05)
                
        # Store learnings
        for learning in result.learnings:
            self.memory.store_long_term(f"Learning: {learning}", "apply")
            
        logger.info(f"📚 Learning complete. Confidence: {self.confidence_level:.2f}")
        
    def _classify_task(self, task_goal: str) -> str:
        """Classify the type of task"""
        goal_lower = task_goal.lower()
        
        if "research" in goal_lower or "find" in goal_lower:
            return "research"
        elif "code" in goal_lower or "program" in goal_lower:
            return "programming"
        elif "analyze" in goal_lower or "data" in goal_lower:
            return "analysis"
        else:
            return "general"
            
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "name": self.name,
            "personality": self.personality,
            "is_busy": self.is_busy,
            "confidence_level": self.confidence_level,
            "success_rate": self.success_rate,
            "tasks_completed": self.tasks_completed,
            "current_task": self.current_task.goal if self.current_task else None,
            "memory_size": {
                "short_term": len(self.memory.short_term),
                "long_term": len(self.memory.long_term),
                "episodic": len(self.memory.episodic)
            }
        }
        
    def reset(self):
        """Reset the agent to initial state"""
        self.current_task = None
        self.current_plan = None
        self.is_busy = False
        self.memory.short_term.clear()
        logger.info("🔄 Agent reset to initial state")


# Convenience function to create and run an agent
def run_agent_task(task_description: str, agent_name: str = "Agent") -> Result:
    """
    Convenience function to create an agent and run a task
    """
    agent = Agent(name=agent_name)
    
    # Analyze the task
    task = agent.analyze_task(task_description)
    
    # Create a plan
    plan = agent.create_plan()
    
    # Execute the plan
    result = agent.execute_plan(plan)
    
    # Learn from results
    agent.learn_from_results(result)
    
    return result


if __name__ == "__main__":
    # Example usage
    print("🤖 Agentic AI Agent Demo")
    print("=" * 40)
    
    agent = Agent("DemoAgent")
    
    # Example task
    task_description = "Research the best programming languages for beginners"
    
    print(f"Task: {task_description}")
    print()
    
    # Run the task
    result = run_agent_task(task_description, "DemoAgent")
    
    print(f"Result: {'✅ Success' if result.success else '❌ Failed'}")
    print(f"Execution time: {result.execution_time:.2f} seconds")
    print(f"Output: {result.output}")
    
    if result.errors:
        print(f"Errors: {result.errors}")
        
    if result.learnings:
        print(f"Learnings: {result.learnings}") 