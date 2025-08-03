"""
Weather Tool for MCP Agent
Provides weather information capabilities
"""

from typing import Dict, Any

class WeatherTool:
    """MCP Weather Tool"""
    
    def __init__(self):
        self.name = "weather"
        self.description = "Get current weather information for a city"
        self.parameters = {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get weather for"
                }
            },
            "required": ["city"]
        }
    
    def execute(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the weather tool"""
        city = params.get("city", "")
        
        try:
            # Simulate weather data (in real implementation, use weather API)
            weather_data = self._get_weather_data(city)
            
            return {
                "success": True,
                "weather": weather_data,
                "city": city,
                "formatted_result": f"Weather for {city}: {weather_data['temperature']}, {weather_data['condition']}"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Weather error: {str(e)}"
            }
    
    def _get_weather_data(self, city: str) -> Dict[str, Any]:
        """Get weather data for a city"""
        # Mock weather data
        mock_weather = {
            "new york": {
                "temperature": "72°F",
                "condition": "Partly Cloudy",
                "humidity": "65%",
                "wind": "8 mph"
            },
            "london": {
                "temperature": "15°C",
                "condition": "Rainy",
                "humidity": "80%",
                "wind": "12 km/h"
            },
            "tokyo": {
                "temperature": "25°C",
                "condition": "Sunny",
                "humidity": "55%",
                "wind": "5 km/h"
            },
            "paris": {
                "temperature": "18°C",
                "condition": "Cloudy",
                "humidity": "70%",
                "wind": "10 km/h"
            },
            "sydney": {
                "temperature": "22°C",
                "condition": "Partly Cloudy",
                "humidity": "60%",
                "wind": "15 km/h"
            }
        }
        
        city_lower = city.lower()
        if city_lower in mock_weather:
            return mock_weather[city_lower]
        else:
            # Default weather for unknown cities
            return {
                "temperature": "20°C",
                "condition": "Partly Cloudy",
                "humidity": "65%",
                "wind": "10 km/h"
            }
    
    def get_schema(self) -> Dict[str, Any]:
        """Get the tool schema for MCP"""
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        } 