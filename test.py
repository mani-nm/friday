# from langchain_ollama import OllamaLLM

# llm = OllamaLLM(model="llama3.1")

# response = llm.invoke("The first man on the moon was ...")
# print(response)

import ollama

ollama.pull('llama3.1')
print(ollama.show('llama3.1'))
stream = ollama.chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)