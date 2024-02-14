import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

def generate_pet_name(animal_type,pet_color):
    # Assuming OpenAI class takes API key as an argument
    openai_api_key = os.getenv("OPENAI_API_KEY")
    llm = OpenAI(api_key=openai_api_key, temperature=0.6)
    
    prompt_template = PromptTemplate(
        input_variables=["animal_type",'pet_color'],
        template="I have a {animal_type} pet. I have a {pet_color} pet.Generate 5 cool pet names for it and also provide meaning of each name generated."
        
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template,output_key='name_pet')
    response = name_chain({'animal_type': animal_type,'pet_color':pet_color})
    
    return response


