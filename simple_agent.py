"""
Simple LangChain Agentic AI Example
A minimal example showing how to build an agentic AI using LangChain
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

def create_agent():
    """Create a simple agentic AI agent using Claude"""
    
    # Initialize Claude LLM
    llm = ChatAnthropic(
        model=os.getenv("ANTHROPIC_MODEL"),
        temperature=0,
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
        ("system", "You are a helpful AI assistant that can use tools to answer questions. Always think step by step and use tools when needed."),
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
    """Main function to demonstrate the agent"""
    
    print("🤖 Simple LangChain Agentic AI Example")
    print("=" * 50)
    
    # Check if API key is available
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⚠️  Warning: No ANTHROPIC_API_KEY found in environment variables.")
        print("   Please set your Anthropic API key to use the full agent features.")
        print("   You can still run the demo.py to see how the tools work.")
        return
    
    # Create agent
    agent = create_agent()
    
    # Example questions
    questions = [
        "What is Python programming?",
        "What's 15 * 23?",
        "What's the weather in London?",
        "What's the capital of France and what's its population?"
    ]
    
    print("\n🧪 Testing Agent with Different Questions:")
    print("-" * 50)
    
    for i, question in enumerate(questions, 1):
        print(f"\n❓ Question {i}: {question}")
        print("🤖 Agent Response:")
        
        try:
            response = agent.invoke({"input": question})
            print(f"   Answer: {response['output']}")
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
    
    print("\n✅ Agent demonstration completed!")

if __name__ == "__main__":
    main() 