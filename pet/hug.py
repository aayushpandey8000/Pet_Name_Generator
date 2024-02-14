import os
from transformers import pipeline
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    # Assuming Hugging Face API key is stored in the environment variable HUGGING_FACE_API_KEY
    hugging_face_api_key = os.getenv("HUGGING_FACE_API_KEY")
    
    # Set up the Hugging Face pipeline for text generation
    generator = pipeline('text-generation', model='openai/whisper-large', api_key=hugging_face_api_key)

    # Define the prompt
    prompt = f"I have a {animal_type} pet. I have a {pet_color} pet. Generate 5 cool pet names for it and also provide meaning of each name generated."

    # Generate pet names using Hugging Face
    generated_names = generator(prompt, max_length=100, num_return_sequences=5)

    # Extract the generated names from the response
    pet_names = [item['generated_text'] for item in generated_names]

    # Return the response
    return {'name_pet': pet_names}

if __name__ == "__main__":
    response = generate_pet_name("Cat", "White")
    print(response)
