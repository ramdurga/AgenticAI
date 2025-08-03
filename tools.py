"""
Tools for the Agentic AI Agent
Provides various capabilities that the agent can use to accomplish tasks
"""

import json
import logging
import time
import random
from typing import List, Dict, Any, Optional
from pathlib import Path
import os

logger = logging.getLogger(__name__)


class ToolRegistry:
    """Registry for all available tools"""
    
    def __init__(self):
        self.tools = {}
        self._register_default_tools()
        
    def _register_default_tools(self):
        """Register the default set of tools"""
        self.register_tool("web_search", web_search)
        self.register_tool("file_operations", file_operations)
        self.register_tool("code_executor", code_executor)
        self.register_tool("data_analyzer", data_analyzer)
        self.register_tool("text_processor", text_processor)
        self.register_tool("calculator", calculator)
        
    def register_tool(self, name: str, tool_func):
        """Register a new tool"""
        self.tools[name] = tool_func
        logger.info(f"🔧 Registered tool: {name}")
        
    def get_tool(self, name: str):
        """Get a tool by name"""
        return self.tools.get(name)
        
    def list_tools(self) -> List[str]:
        """List all available tools"""
        return list(self.tools.keys())
        
    def execute_tool(self, tool_name: str, *args, **kwargs):
        """Execute a tool with given arguments"""
        tool = self.get_tool(tool_name)
        if tool:
            return tool(*args, **kwargs)
        else:
            raise ValueError(f"Tool '{tool_name}' not found")


def web_search(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Simulate web search functionality
    In a real implementation, this would use actual search APIs
    """
    logger.info(f"🔍 Searching for: {query}")
    
    # Simulate search delay
    time.sleep(0.5)
    
    # Mock search results based on query
    mock_results = []
    
    if "programming" in query.lower() or "language" in query.lower():
        mock_results = [
            {
                "title": "Top Programming Languages for Beginners in 2024",
                "url": "https://example.com/programming-languages",
                "snippet": "Python, JavaScript, and Scratch are among the best programming languages for beginners due to their simple syntax and extensive learning resources.",
                "relevance": 0.95
            },
            {
                "title": "Why Python is Perfect for Beginners",
                "url": "https://example.com/python-beginners",
                "snippet": "Python's readable syntax and large community make it an excellent choice for new programmers.",
                "relevance": 0.92
            },
            {
                "title": "JavaScript: The Language of the Web",
                "url": "https://example.com/javascript-web",
                "snippet": "JavaScript is essential for web development and offers immediate visual feedback for beginners.",
                "relevance": 0.88
            }
        ]
    elif "data" in query.lower() or "analysis" in query.lower():
        mock_results = [
            {
                "title": "Data Analysis Techniques for Beginners",
                "url": "https://example.com/data-analysis",
                "snippet": "Learn the fundamentals of data analysis including cleaning, visualization, and interpretation.",
                "relevance": 0.94
            },
            {
                "title": "Python for Data Science",
                "url": "https://example.com/python-data-science",
                "snippet": "Python's pandas and numpy libraries make data analysis accessible to beginners.",
                "relevance": 0.91
            }
        ]
    else:
        # Generic results
        mock_results = [
            {
                "title": f"Search Results for: {query}",
                "url": f"https://example.com/search?q={query}",
                "snippet": f"Comprehensive information about {query} with detailed explanations and examples.",
                "relevance": 0.85
            },
            {
                "title": f"Understanding {query}",
                "url": f"https://example.com/understanding-{query}",
                "snippet": f"Learn the basics and advanced concepts of {query} through practical examples.",
                "relevance": 0.82
            }
        ]
    
    # Limit results
    results = mock_results[:max_results]
    
    logger.info(f"✅ Found {len(results)} search results")
    return results


def file_operations():
    """File operations tool - returns a namespace with file operation methods"""
    
    class FileOps:
        @staticmethod
        def read_file(filepath: str) -> str:
            """Read content from a file"""
            try:
                path = Path(filepath)
                if path.exists():
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    logger.info(f"📖 Read file: {filepath}")
                    return content
                else:
                    logger.warning(f"⚠️ File not found: {filepath}")
                    return f"File not found: {filepath}"
            except Exception as e:
                logger.error(f"❌ Error reading file {filepath}: {e}")
                return f"Error reading file: {str(e)}"
        
        @staticmethod
        def write_file(filepath: str, content: str) -> str:
            """Write content to a file"""
            try:
                path = Path(filepath)
                path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
                logger.info(f"📝 Wrote file: {filepath}")
                return f"Successfully wrote {len(content)} characters to {filepath}"
            except Exception as e:
                logger.error(f"❌ Error writing file {filepath}: {e}")
                return f"Error writing file: {str(e)}"
        
        @staticmethod
        def append_file(filepath: str, content: str) -> str:
            """Append content to a file"""
            try:
                path = Path(filepath)
                path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(path, 'a', encoding='utf-8') as f:
                    f.write(content + '\n')
                    
                logger.info(f"📝 Appended to file: {filepath}")
                return f"Successfully appended content to {filepath}"
            except Exception as e:
                logger.error(f"❌ Error appending to file {filepath}: {e}")
                return f"Error appending to file: {str(e)}"
        
        @staticmethod
        def list_files(directory: str = ".") -> List[str]:
            """List files in a directory"""
            try:
                path = Path(directory)
                if path.exists():
                    files = [f.name for f in path.iterdir() if f.is_file()]
                    logger.info(f"📁 Listed {len(files)} files in {directory}")
                    return files
                else:
                    logger.warning(f"⚠️ Directory not found: {directory}")
                    return []
            except Exception as e:
                logger.error(f"❌ Error listing files in {directory}: {e}")
                return []
        
        @staticmethod
        def create_directory(dirpath: str) -> str:
            """Create a directory"""
            try:
                path = Path(dirpath)
                path.mkdir(parents=True, exist_ok=True)
                logger.info(f"📁 Created directory: {dirpath}")
                return f"Successfully created directory: {dirpath}"
            except Exception as e:
                logger.error(f"❌ Error creating directory {dirpath}: {e}")
                return f"Error creating directory: {str(e)}"
    
    return FileOps()


def code_executor(code: str, language: str = "python") -> Dict[str, Any]:
    """
    Simulate code execution
    In a real implementation, this would use a sandboxed environment
    """
    logger.info(f"💻 Executing {language} code")
    
    # Simulate execution time
    time.sleep(0.3)
    
    # Mock execution results
    if "print" in code.lower():
        return {
            "success": True,
            "output": "Hello, World!",
            "execution_time": 0.1,
            "language": language
        }
    elif "hello" in code.lower():
        return {
            "success": True,
            "output": "Hello from the code executor!",
            "execution_time": 0.05,
            "language": language
        }
    elif "error" in code.lower():
        return {
            "success": False,
            "output": "",
            "error": "SyntaxError: invalid syntax",
            "execution_time": 0.02,
            "language": language
        }
    else:
        return {
            "success": True,
            "output": f"Code executed successfully: {code[:50]}...",
            "execution_time": 0.15,
            "language": language
        }


def data_analyzer(data_source: str) -> Dict[str, Any]:
    """
    Simulate data analysis functionality
    """
    logger.info(f"📊 Analyzing data from: {data_source}")
    
    # Simulate analysis time
    time.sleep(0.4)
    
    # Mock analysis results
    analysis_results = {
        "data_points": random.randint(100, 1000),
        "columns": random.randint(3, 8),
        "missing_values": random.randint(0, 50),
        "outliers": random.randint(0, 10),
        "correlations": {
            "feature1_feature2": round(random.uniform(-0.8, 0.8), 3),
            "feature2_feature3": round(random.uniform(-0.8, 0.8), 3)
        },
        "summary_stats": {
            "mean": round(random.uniform(10, 100), 2),
            "median": round(random.uniform(10, 100), 2),
            "std": round(random.uniform(5, 20), 2)
        },
        "insights": [
            "Data shows a clear trend in the target variable",
            "Several features have strong correlations",
            "Missing values are minimal and can be handled",
            "No significant outliers detected"
        ]
    }
    
    logger.info(f"✅ Analysis completed with {analysis_results['data_points']} data points")
    return analysis_results


def text_processor(text: str, operation: str = "summarize") -> str:
    """
    Process text with various operations
    """
    logger.info(f"📝 Processing text with operation: {operation}")
    
    # Simulate processing time
    time.sleep(0.2)
    
    if operation == "summarize":
        # Simple summarization (in reality, this would use NLP)
        sentences = text.split('.')
        summary = '. '.join(sentences[:2]) + '.'
        return f"Summary: {summary}"
    
    elif operation == "extract_keywords":
        # Simple keyword extraction
        words = text.lower().split()
        keywords = [word for word in words if len(word) > 4]
        return f"Keywords: {', '.join(keywords[:5])}"
    
    elif operation == "sentiment":
        # Simple sentiment analysis
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            sentiment = "positive"
        elif negative_count > positive_count:
            sentiment = "negative"
        else:
            sentiment = "neutral"
            
        return f"Sentiment: {sentiment} (positive: {positive_count}, negative: {negative_count})"
    
    else:
        return f"Processed text with operation '{operation}': {text[:100]}..."


def calculator(expression: str) -> Dict[str, Any]:
    """
    Simple calculator for basic mathematical operations
    """
    logger.info(f"🧮 Calculating: {expression}")
    
    try:
        # Safe evaluation (in production, use a proper math parser)
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Invalid characters in expression")
        
        result = eval(expression)
        
        return {
            "success": True,
            "expression": expression,
            "result": result,
            "type": "calculation"
        }
        
    except Exception as e:
        return {
            "success": False,
            "expression": expression,
            "error": str(e),
            "type": "calculation"
        }


# Convenience functions for direct access
def search_web(query: str) -> List[Dict[str, Any]]:
    """Convenience function for web search"""
    return web_search(query)


def read_file_content(filepath: str) -> str:
    """Convenience function for reading files"""
    return file_operations().read_file(filepath)


def write_file_content(filepath: str, content: str) -> str:
    """Convenience function for writing files"""
    return file_operations().write_file(filepath, content)


def run_code(code: str) -> Dict[str, Any]:
    """Convenience function for code execution"""
    return code_executor(code)


def analyze_data(data_source: str) -> Dict[str, Any]:
    """Convenience function for data analysis"""
    return data_analyzer(data_source)


if __name__ == "__main__":
    # Test the tools
    print("🔧 Testing Tools")
    print("=" * 30)
    
    # Test web search
    print("\n1. Testing web search:")
    results = web_search("programming languages for beginners")
    print(f"Found {len(results)} results")
    
    # Test file operations
    print("\n2. Testing file operations:")
    file_ops = file_operations()
    result = file_ops.write_file("test.txt", "Hello, this is a test file!")
    print(result)
    
    # Test code execution
    print("\n3. Testing code execution:")
    result = code_executor("print('Hello, World!')")
    print(f"Code result: {result}")
    
    # Test data analysis
    print("\n4. Testing data analysis:")
    result = data_analyzer("sample_data.csv")
    print(f"Analysis completed: {result['data_points']} data points")
    
    # Test text processing
    print("\n5. Testing text processing:")
    result = text_processor("This is a great example of text processing. It works very well.", "sentiment")
    print(result)
    
    # Test calculator
    print("\n6. Testing calculator:")
    result = calculator("2 + 3 * 4")
    print(f"Calculation result: {result}")
    
    print("\n✅ All tools tested successfully!") 