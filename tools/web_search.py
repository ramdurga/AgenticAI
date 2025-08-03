"""
Web Search Tool for MCP Agent
Provides web search capabilities
"""

from typing import Dict, Any, List

class WebSearchTool:
    """MCP Web Search Tool"""
    
    def __init__(self):
        self.name = "web_search"
        self.description = "Search the web for current information"
        self.parameters = {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to look up"
                },
                "max_results": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the web search tool"""
        query = params.get("query", "")
        max_results = params.get("max_results", 5)
        
        try:
            # Simulate web search (in real implementation, use actual search API)
            results = self._simulate_search(query, max_results)
            
            return {
                "success": True,
                "results": results,
                "query": query,
                "formatted_result": f"Found {len(results)} results for '{query}'"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Search error: {str(e)}"
            }
    
    def _simulate_search(self, query: str, max_results: int) -> List[Dict[str, Any]]:
        """Simulate web search results"""
        # Mock search results
        mock_results = {
            "python": [
                {
                    "title": "Python Programming Language",
                    "snippet": "Python is a high-level programming language known for its simplicity and readability.",
                    "url": "https://python.org"
                },
                {
                    "title": "Python Tutorial",
                    "snippet": "Learn Python programming with comprehensive tutorials and examples.",
                    "url": "https://docs.python.org/tutorial"
                }
            ],
            "machine learning": [
                {
                    "title": "Machine Learning Basics",
                    "snippet": "Machine learning is a subset of artificial intelligence that enables systems to learn from data.",
                    "url": "https://example.com/ml-basics"
                }
            ],
            "weather": [
                {
                    "title": "Weather Information",
                    "snippet": "Weather information can be found through various online services and APIs.",
                    "url": "https://example.com/weather"
                }
            ],
            "capital": [
                {
                    "title": "World Capitals",
                    "snippet": "Capitals are the primary cities of countries, often housing government buildings.",
                    "url": "https://example.com/capitals"
                }
            ]
        }
        
        # Find matching results
        results = []
        query_lower = query.lower()
        
        for keyword, keyword_results in mock_results.items():
            if keyword.lower() in query_lower:
                results.extend(keyword_results)
        
        # If no specific matches, provide generic results
        if not results:
            results = [
                {
                    "title": f"Search Results for '{query}'",
                    "snippet": f"Found relevant information about {query}",
                    "url": f"https://example.com/search?q={query}"
                }
            ]
        
        return results[:max_results]
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool schema for MCP"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        } 