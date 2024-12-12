pip install nltk
import nltk
import random
from nltk.chat.util import Chat, reflections

# Download necessary NLTK datasets (run this once)
nltk.download('punkt')

# Define a set of conversation patterns
patterns = [
    (r'Hi|Hello|Hey', ['Hello!', 'Hi there!', 'Hey! How can I help you today?']),
    (r'How are you?', ['I am doing great, thank you!', 'I am fine, how about you?']),
    (r'I am (.*)', ['Oh, you are feeling {0}. Interesting!', 'Tell me more about being {0}.']),
    (r'What is your name?', ['I am a chatbot, but you can call me ChatBot!']),
    (r'How old are you?', ['I am ageless! I exist to chat and help you!']),
    (r'What can you do?', ['I can chat with you, answer questions, and help you with simple tasks.']),
    (r'Bye|Goodbye', ['Goodbye!', 'See you later!', 'Take care!']),
    (r'(.*)', ['I am not sure I understand what you mean. Could you rephrase?'])
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

def chat():
    print("ChatBot: Hello! How can I assist you today? (Type 'exit' to end the conversation.)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("ChatBot: Goodbye!")
            break
        
        # Get the chatbot's response
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
