from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

load_dotenv()

default_tone = "дружелюбный"

values = {
    "lang": "славянский",
    "text": input("Введите текст: "),
    "tone": input(f"Введите тон ({default_tone}): ").strip() or default_tone,
}

template = ChatPromptTemplate([
    SystemMessagePromptTemplate.from_template_file("../prompts/system.txt", input_variables=["lang"]),
    SystemMessagePromptTemplate.from_template("твой тон общения: {tone}"),
    HumanMessagePromptTemplate.from_template("Скажи '{text}' на трех языках")
])

prompt = template.format_messages(**values)

model = ChatOpenAI(model="gpt-4.1-mini", temperature=1, timeout=(10, 120), max_retries=0)
response = model.invoke(prompt)


print(prompt)

print(response.content)