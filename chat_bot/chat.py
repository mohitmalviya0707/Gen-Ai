from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMIstralAI
from langchain_core.messages import AIMessage , SystemMessage , HumanMessage

model = ChatMIstralAI(model = "mistral-smal-2509" , temperacure=0.9)

print("chose your ai model ")
print("press 1 for Angry model ")
print("press 2  for funny model")
print('fress 3 for san model ')

choise = int(input("tell your response: "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


messages = [
    SystemMessage(content = mode)

]

print ("------- if your plabe to exit click 0 ---------")

while True:
    prompt = input("you:- ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :", response.content)

print(messages)