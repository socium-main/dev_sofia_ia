# from crewai import Agent

# chatbot_agent = Agent(
#     role="Friendly Chatbot",
#     goal="Engage in friendly conversation and provide helpful responses",
#     backstory="You are a cheerful and knowledgeable AI assistant, always eager to help and chat.",
#     verbose=True
# )

# from crewai import Task

# chat_task = Task(
#     description="Engage in a conversation with the user, responding to their messages in a friendly and helpful manner.",
#     agent=chatbot_agent,
#     expected_output="A friendly and helpful response to the user's message.",
#     verbos=True
# )

# from crewai import Crew

# chatbot_crew = Crew(
#     agents=[chatbot_agent],
#     tasks=[chat_task],
#     verbose=True
# )


# def chat():
#     print("Chatbot: Hello! How can I help you today?")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit', 'bye']:
#             print("Chatbot: Goodbye! Have a great day!")
#             break
        
#         response = chatbot_crew.kickoff(inputs={'user_message': user_input})
#         print(f"Chatbot: {response}")

# if __name__ == "__main__":
#     chat()



from crewai import Crew, Agent, Task
# Import other necessary CrewAI components

def initialize_crew():
    # Set up your agents, tasks, and crew here
    # Return the initialized crew
    pass

def chat_interface():
    print("Welcome to CrewAI Chat!")
    
    crew = initialize_crew()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        # Process the user input with CrewAI
        response = crew.kickoff(user_input)
        
        print(f"CrewAI: {response}")

if __name__ == "__main__":
    chat_interface()