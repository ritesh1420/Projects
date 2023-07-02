from speak import say
import openai
import wikipedia

def generate_chat_response(input_text):
    # Set up OpenAI API credentials
    openai.api_key = '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'
    
    # Generate a response using ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    
    # Extract and return the generated response
    return response.choices[0].text.strip()
def search_and_speak(query):
    # Your code to generate a response using ChatGPT
    response = generate_chat_response(query)

    # Speak the response
    say(response)

# Example usage
search_query = "What is the capital of France?"
search_and_speak(search_query)
