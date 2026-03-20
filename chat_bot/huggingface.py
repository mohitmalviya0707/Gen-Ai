from langchain_huggingface import ChatHugingFace ,HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id = "Gpt4.1"


)

model = ChatHugingFace(llm=llm)

reponse = model.invoke("who create you ?")

print(reponse.content)
