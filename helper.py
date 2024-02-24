from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI()

#Dummy function
def generate_pet_name(n: int = 5, animal: str="cat", pet_color: str = "brown"):

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        ("user", '''I have a {animal} pet and I want a cool name for it. Suggest me {num} cool names for my pet. My pet is {pet_color} in color.
         Answer only names seperated by newline character. Do not output anything else''')
    ])

    chain = prompt | llm

    res = chain.invoke({"num": str(n), "animal": animal, "pet_color": pet_color})

    return res.content