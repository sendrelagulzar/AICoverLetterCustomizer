import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY']='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'
llm = OpenAI(temperature=0.6)

def project(description,client_name,my_name):
    prompt_template_1= PromptTemplate(
    input_variables=['description','client_name','my_name'],
    template="Write a project proposal cover letter to secure the project with {client_name}. The project is about {description}.Add Sincerely{my_name}"
    )
    chain= LLMChain(llm=llm, prompt=prompt_template_1)
    response=chain.run({'description':description,'client_name':client_name,'my_name':my_name})
    return response

def job(description,client_name,my_name):
    prompt_template_2= PromptTemplate(
    input_variables=['description','client_name','my_name'],
    template="Write cover letter to get a job from {client_name} company. The job profile is {description}.Add Sincerely{my_name}"
    )
    chain= LLMChain(llm=llm, prompt=prompt_template_2)
    response=chain.run({'description':description,'client_name':client_name,'my_name':my_name})
    return response

