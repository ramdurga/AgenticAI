"""
Simple tools for the LangChain agentic AI example
"""

import requests
import json
from typing import Optional, Type, List, Dict, Any
from langchain.tools import BaseTool
from pydantic import BaseModel, Field


class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for current information"
    
    def _run(self, query: str) -> str:
        """Search the web for information"""
        try:
            # Simulate web search (in real use, you'd use a search API)
            mock_results = {
                "python": "Python is a high-level programming language known for its simplicity and readability.",
                "weather": "Weather information can be found through various online services and APIs.",
                "capital": "Capitals are the primary cities of countries, often housing government buildings.",
                "population": "Population data is collected by governments and international organizations."
            }
            
            # Simple keyword matching
            for keyword, info in mock_results.items():
                if keyword.lower() in query.lower():
                    return f"Search results for '{query}': {info}"
            
            return f"Search results for '{query}': Found relevant information about this topic."
            
        except Exception as e:
            return f"Error searching for '{query}': {str(e)}"


class CalculatorTool(BaseTool):
    name: str = "calculator"
    description: str = "Calculate mathematical expressions"
    
    def _run(self, expression: str) -> str:
        """Calculate a mathematical expression"""
        try:
            # Safe evaluation (in production, use a proper math parser)
            allowed_chars = set('0123456789+-*/(). ')
            if not all(c in allowed_chars for c in expression):
                return "Error: Invalid characters in expression"
            
            result = eval(expression)
            return f"Calculation: {expression} = {result}"
            
        except Exception as e:
            return f"Error calculating '{expression}': {str(e)}"


class WeatherTool(BaseTool):
    name: str = "weather"
    description: str = "Get current weather information for a city"
    
    def _run(self, city: str) -> str:
        """Get weather for a city"""
        try:
            # Mock weather data (in real use, you'd call a weather API)
            mock_weather = {
                "new york": "New York: 72°F, Partly Cloudy",
                "london": "London: 15°C, Rainy",
                "tokyo": "Tokyo: 25°C, Sunny",
                "paris": "Paris: 18°C, Cloudy"
            }
            
            city_lower = city.lower()
            if city_lower in mock_weather:
                return mock_weather[city_lower]
            else:
                return f"Weather for {city}: 20°C, Partly Cloudy (mock data)"
                
        except Exception as e:
            return f"Error getting weather for '{city}': {str(e)}"


def get_tools():
    """Get all available tools"""
    return [
        WebSearchTool(),
        CalculatorTool(),
        WeatherTool()
    ]


# Simple function tools for the custom agent
def web_search(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """
    Simulate web search functionality
    In a real implementation, this would use actual search APIs
    """
    mock_results = {
        "python": "Python is a high-level programming language known for its simplicity and readability.",
        "machine learning": "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
        "data science": "Data science combines statistics, programming, and domain expertise to extract insights from data.",
        "programming": "Programming is the process of creating instructions for computers to execute.",
        "algorithm": "An algorithm is a step-by-step procedure for solving problems or performing tasks."
    }
    
    results = []
    for keyword, info in mock_results.items():
        if keyword.lower() in query.lower():
            results.append({
                "title": f"Results for {keyword}",
                "snippet": info,
                "url": f"https://example.com/{keyword.replace(' ', '-')}"
            })
    
    if not results:
        results.append({
            "title": f"Results for {query}",
            "snippet": f"Found relevant information about {query}",
            "url": f"https://example.com/{query.replace(' ', '-')}"
        })
    
    return results[:max_results]


def calculator(expression: str) -> str:
    """
    Calculate mathematical expressions
    """
    try:
        # Safe evaluation (in production, use a proper math parser)
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters in expression"
        
        result = eval(expression)
        return f"Calculation: {expression} = {result}"
        
    except Exception as e:
        return f"Error calculating '{expression}': {str(e)}"


def data_analyzer(data_description: str) -> str:
    """
    Simulate data analysis functionality
    """
    analysis_results = {
        "student grades": "Analysis shows average grade of 85%, with 70% of students scoring above 80%",
        "sales data": "Sales analysis reveals 15% growth compared to last quarter, with strongest performance in Q3",
        "survey results": "Survey analysis indicates 78% satisfaction rate, with highest scores in customer service",
        "performance metrics": "Performance analysis shows 92% uptime, with response times averaging 200ms"
    }
    
    for keyword, result in analysis_results.items():
        if keyword.lower() in data_description.lower():
            return f"Data Analysis for '{data_description}': {result}"
    
    return f"Data Analysis for '{data_description}': Comprehensive analysis completed with insights and recommendations"


def file_operations(operation: str, filename: str = "output.txt", content: str = "") -> str:
    """
    Simulate file operations
    """
    if "read" in operation.lower():
        return f"File read operation: Successfully read content from {filename}"
    elif "write" in operation.lower():
        return f"File write operation: Successfully wrote content to {filename}"
    elif "save" in operation.lower():
        return f"File save operation: Successfully saved data to {filename}"
    else:
        return f"File operation '{operation}' completed successfully"


def code_executor(code: str) -> str:
    """
    Simulate code execution
    """
    if "print" in code.lower():
        return f"Code execution: Successfully executed print statement"
    elif "function" in code.lower():
        return f"Code execution: Function defined and ready for use"
    elif "loop" in code.lower():
        return f"Code execution: Loop executed successfully"
    else:
        return f"Code execution: Successfully executed code snippet"


def text_processor(text: str) -> str:
    """
    Simulate text processing
    """
    word_count = len(text.split())
    char_count = len(text)
    
    return f"Text processing completed: {word_count} words, {char_count} characters processed" 