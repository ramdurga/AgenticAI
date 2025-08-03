"""
Agentic AI Agent - A simple implementation for beginners
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
import anthropic

# Load environment variables
load_dotenv()

@dataclass
class Task:
    """Represents a task for the agent to complete"""
    id: str
    description: str
    priority: str = "medium"
    status: str = "pending"
    created_at: str = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().isoformat()

@dataclass
class Plan:
    """Represents a plan with steps to complete a task"""
    task_id: str
    steps: List[Dict[str, Any]]
    estimated_time: str = "unknown"
    confidence: float = 0.8

@dataclass
class Result:
    """Represents the result of a task execution"""
    task_id: str
    success: bool
    output: str
    tools_used: List[str]
    execution_time: float
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []

class Memory:
    """Memory system for the agent"""
    
    def __init__(self):
        self.short_term = []  # Recent interactions
        self.long_term = {}   # Important facts and patterns
        self.episodic = []    # Past experiences
    
    def add_to_short_term(self, interaction: Dict[str, Any]):
        """Add recent interaction to short-term memory"""
        self.short_term.append({
            'timestamp': datetime.now().isoformat(),
            'interaction': interaction
        })
        # Keep only last 10 interactions
        if len(self.short_term) > 10:
            self.short_term.pop(0)
    
    def add_to_long_term(self, key: str, value: Any):
        """Add important information to long-term memory"""
        self.long_term[key] = {
            'value': value,
            'timestamp': datetime.now().isoformat(),
            'access_count': 0
        }
    
    def get_from_long_term(self, key: str) -> Optional[Any]:
        """Retrieve information from long-term memory"""
        if key in self.long_term:
            self.long_term[key]['access_count'] += 1
            return self.long_term[key]['value']
        return None
    
    def add_episode(self, episode: Dict[str, Any]):
        """Add a complete episode to episodic memory"""
        self.episodic.append({
            'timestamp': datetime.now().isoformat(),
            'episode': episode
        })
    
    def get_relevant_memories(self, context: str) -> List[Dict[str, Any]]:
        """Get memories relevant to current context"""
        relevant = []
        
        # Check short-term memory
        for memory in self.short_term[-5:]:  # Last 5 interactions
            relevant.append(memory)
        
        # Check long-term memory for relevant keys
        for key, value in self.long_term.items():
            if context.lower() in key.lower():
                relevant.append(value)
        
        return relevant

class Agent:
    """Main agent class with autonomous capabilities"""
    
    def __init__(self, name: str = "AgenticAI", personality: str = "helpful"):
        self.name = name
        self.personality = personality
        self.memory = Memory()
        self.tools = {}
        self.learning_rate = 0.1
        
        # Initialize Claude client
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if api_key:
            self.claude_client = anthropic.Anthropic(api_key=api_key)
        else:
            self.claude_client = None
            print("⚠️  Warning: No ANTHROPIC_API_KEY found. Some features will be limited.")
    
    def analyze_task(self, task_description: str) -> Task:
        """Analyze and create a task from description"""
        task_id = f"task_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Use Claude to analyze task if available
        if self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": f"Analyze this task and provide a structured response:\n{task_description}\n\nProvide: 1) Priority (high/medium/low), 2) Key requirements, 3) Estimated complexity"
                    }]
                )
                analysis = response.content[0].text
                # Extract priority from analysis
                if "high" in analysis.lower():
                    priority = "high"
                elif "low" in analysis.lower():
                    priority = "low"
                else:
                    priority = "medium"
            except Exception as e:
                print(f"⚠️  Claude analysis failed: {e}")
                priority = "medium"
        else:
            priority = "medium"
        
        task = Task(
            id=task_id,
            description=task_description,
            priority=priority
        )
        
        # Store in memory
        self.memory.add_to_short_term({
            'type': 'task_analysis',
            'task_id': task_id,
            'description': task_description,
            'priority': priority
        })
        
        return task
    
    def create_plan(self, task: Task) -> Plan:
        """Create a plan to complete the task"""
        steps = []
        
        if self.claude_client:
            try:
                response = self.claude_client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=1000,
                    messages=[{
                        "role": "user",
                        "content": f"Create a step-by-step plan for this task:\n{task.description}\n\nProvide 3-5 clear steps with tool requirements."
                    }]
                )
                plan_text = response.content[0].text
                
                # Parse plan into steps (simplified)
                lines = plan_text.split('\n')
                for line in lines:
                    if line.strip() and any(keyword in line.lower() for keyword in ['step', '1.', '2.', '3.', '4.', '5.']):
                        steps.append({
                            'description': line.strip(),
                            'tool_required': self._identify_tool(line),
                            'status': 'pending'
                        })
            except Exception as e:
                print(f"⚠️  Claude planning failed: {e}")
                steps = self._create_default_plan(task)
        else:
            steps = self._create_default_plan(task)
        
        plan = Plan(
            task_id=task.id,
            steps=steps
        )
        
        return plan
    
    def _create_default_plan(self, task: Task) -> List[Dict[str, Any]]:
        """Create a default plan when Claude is not available"""
        return [
            {
                'description': f"Analyze task: {task.description}",
                'tool_required': 'text_processor',
                'status': 'pending'
            },
            {
                'description': "Gather relevant information",
                'tool_required': 'web_search',
                'status': 'pending'
            },
            {
                'description': "Process and synthesize results",
                'tool_required': 'data_analyzer',
                'status': 'pending'
            }
        ]
    
    def _identify_tool(self, step_description: str) -> str:
        """Identify which tool is needed for a step"""
        step_lower = step_description.lower()
        
        if any(word in step_lower for word in ['search', 'find', 'look up']):
            return 'web_search'
        elif any(word in step_lower for word in ['calculate', 'math', 'compute']):
            return 'calculator'
        elif any(word in step_lower for word in ['analyze', 'process', 'synthesize']):
            return 'data_analyzer'
        elif any(word in step_lower for word in ['file', 'read', 'write']):
            return 'file_operations'
        elif any(word in step_lower for word in ['code', 'program', 'execute']):
            return 'code_executor'
        else:
            return 'text_processor'
    
    def execute_plan(self, task: Task, plan: Plan) -> Result:
        """Execute the plan and return results"""
        start_time = datetime.now()
        tools_used = []
        errors = []
        output_parts = []
        
        print(f"🤖 {self.name} executing plan for task: {task.description}")
        
        for i, step in enumerate(plan.steps, 1):
            print(f"  📋 Step {i}: {step['description']}")
            
            try:
                if step['tool_required'] in self.tools:
                    tool_result = self.tools[step['tool_required']](step['description'])
                    output_parts.append(f"Step {i}: {tool_result}")
                    tools_used.append(step['tool_required'])
                    step['status'] = 'completed'
                else:
                    # Simulate tool execution
                    simulated_result = self._simulate_tool_execution(step['tool_required'], step['description'])
                    output_parts.append(f"Step {i}: {simulated_result}")
                    tools_used.append(step['tool_required'])
                    step['status'] = 'completed'
                    
            except Exception as e:
                error_msg = f"Step {i} failed: {str(e)}"
                errors.append(error_msg)
                step['status'] = 'failed'
                print(f"    ❌ {error_msg}")
        
        execution_time = (datetime.now() - start_time).total_seconds()
        
        # Determine success based on completed steps
        success = len([s for s in plan.steps if s['status'] == 'completed']) > 0
        
        result = Result(
            task_id=task.id,
            success=success,
            output="\n".join(output_parts),
            tools_used=tools_used,
            execution_time=execution_time,
            errors=errors
        )
        
        # Learn from this execution
        self._learn_from_execution(task, plan, result)
        
        return result
    
    def _simulate_tool_execution(self, tool_name: str, description: str) -> str:
        """Simulate tool execution when actual tools aren't available"""
        simulations = {
            'web_search': f"Simulated web search for: {description}",
            'calculator': f"Simulated calculation for: {description}",
            'data_analyzer': f"Simulated data analysis for: {description}",
            'file_operations': f"Simulated file operation for: {description}",
            'code_executor': f"Simulated code execution for: {description}",
            'text_processor': f"Simulated text processing for: {description}"
        }
        return simulations.get(tool_name, f"Simulated {tool_name} for: {description}")
    
    def _learn_from_execution(self, task: Task, plan: Plan, result: Result):
        """Learn from task execution to improve future performance"""
        # Store episode in memory
        episode = {
            'task': asdict(task),
            'plan': asdict(plan),
            'result': asdict(result),
            'success_rate': 1.0 if result.success else 0.0
        }
        self.memory.add_episode(episode)
        
        # Update long-term memory with patterns
        if result.success:
            self.memory.add_to_long_term(
                f"successful_pattern_{task.description[:50]}",
                {
                    'tools_used': result.tools_used,
                    'execution_time': result.execution_time,
                    'success': True
                }
            )
        
        # Adjust learning rate based on success
        if result.success:
            self.learning_rate = min(self.learning_rate + 0.01, 0.2)
        else:
            self.learning_rate = max(self.learning_rate - 0.01, 0.05)
    
    def register_tool(self, name: str, tool_function):
        """Register a tool that the agent can use"""
        self.tools[name] = tool_function
        print(f"🔧 Tool registered: {name}")
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            'name': self.name,
            'personality': self.personality,
            'learning_rate': self.learning_rate,
            'tools_available': list(self.tools.keys()),
            'memory_stats': {
                'short_term_count': len(self.memory.short_term),
                'long_term_count': len(self.memory.long_term),
                'episodic_count': len(self.memory.episodic)
            }
        } 