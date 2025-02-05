import ollama

#response = ollama.list()

#print(response)

# To use the Ollama Chat Interface
res = ollama.chat(
    model = "deepseek-r1:7b",
    messages= [
        {"role": "user", "content": "Why is the sky blue?"},
    ],
)

#Chat feature response using ollama
print(res["message"]["content"])

