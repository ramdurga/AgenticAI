"""
Calculator Tool for MCP Agent
Provides mathematical calculation capabilities
"""

import re
from typing import Dict, Any

class CalculatorTool:
    """MCP Calculator Tool"""
    
    def __init__(self):
        self.name = "calculator"
        self.description = "Perform mathematical calculations"
        self.parameters = {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to calculate"
                }
            },
            "required": ["expression"]
        }
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the calculator tool"""
        expression = params.get("expression", "")
        
        try:
            # Validate expression for safety
            if not self._is_safe_expression(expression):
                return {
                    "success": False,
                    "error": "Invalid characters in expression. Only numbers, operators, and parentheses allowed."
                }
            
            # Evaluate the expression
            result = eval(expression)
            
            return {
                "success": True,
                "result": result,
                "expression": expression,
                "formatted_result": f"Calculation: {expression} = {result}"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Calculation error: {str(e)}"
            }
    
    def _is_safe_expression(self, expression: str) -> bool:
        """Check if expression contains only safe characters"""
        # Allow numbers, basic operators, parentheses, and spaces
        safe_pattern = r'^[0-9+\-*/().\s]+$'
        return bool(re.match(safe_pattern, expression))
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool schema for MCP"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        } 