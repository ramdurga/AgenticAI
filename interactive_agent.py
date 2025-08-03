"""
Interactive LangChain Agentic AI Example
Chat with an agentic AI that can use tools to help you
"""

import os
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from tools import WebSearchTool, CalculatorTool, WeatherTool

# Load environment variables
load_dotenv()

def create_interactive_agent():
    """Create an interactive agentic AI agent using Claude"""
    
    # Initialize Claude LLM
    llm = ChatAnthropic(
        model="claude-3-haiku-20240307",
        temperature=0.7,  # Slightly higher for more creative responses
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Create tools
    tools = [
        WebSearchTool(),
        CalculatorTool(),
        WeatherTool()
    ]
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful AI assistant that can use tools to answer questions. 
        You have access to web search, calculator, and weather tools.
        Always think step by step and use tools when needed.
        Be conversational and engaging in your responses."""),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create agent
    agent = create_openai_tools_agent(llm, tools, prompt)
    
    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent_executor

def main():
    """Interactive chat with the agent"""
    
    print("🤖 Interactive LangChain Agentic AI Chat")
    print("=" * 50)
    print("Type 'quit' to exit the chat")
    print("Type 'help' to see available commands")
    print("-" * 50)
    
    # Check if API key is available
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Warning: No ANTHROPIC_API_KEY found in environment variables.")
        print("   Please set your Anthropic API key to use the interactive chat.")
        print("   You can still run the demo.py to see how the tools work.")
        return
    
    # Create agent
    agent = create_interactive_agent()
    
    print("🤖 Hello! I'm your AI assistant. I can help you with:")
    print("   • Web searches for current information")
    print("   • Mathematical calculations")
    print("   • Weather information")
    print("   • General questions and conversations")
    print()
    
    while True:
        try:
            # Get user input
            user_input = input("👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 Goodbye! Thanks for chatting with me!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print("🤖 Available commands:")
                print("   • 'quit', 'exit', 'bye' - Exit the chat")
                print("   • 'help' - Show this help message")
                print("   • Any other text - Ask me a question!")
                print()
                continue
            
            # Skip empty input
            if not user_input:
                continue
            
            # Get response from agent
            print("🤖 Thinking...")
            response = agent.invoke({"input": user_input})
            print(f"🤖 Assistant: {response['output']}")
            print()
            
        except KeyboardInterrupt:
            print("\n🤖 Goodbye! Thanks for chatting with me!")
            break
        except Exception as e:
            print(f"🤖 Sorry, I encountered an error: {str(e)}")
            print("Please try asking your question again.")
            print()

if __name__ == "__main__":
    main() 