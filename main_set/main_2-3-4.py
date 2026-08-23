from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

load_dotenv()

default_tone = "дружелюбный"

base_template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("../prompts/system.txt", input_variables=["lang"]),
    SystemMessagePromptTemplate.from_template("твой тон общения: {tone}"),
    HumanMessagePromptTemplate.from_template("Скажи '{text}' на трех языках")
])

template = base_template.partial(lang="славянский", tone=default_tone)

text = input("Введите текст: ")
prompt = template.format_messages(text=text)

print(template.format(text=text))

# model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
# response = model.invoke(prompt)
#
# print(response.content)
