import ollama

#response = ollama.list()

#print(response)

# To use the Ollama Chat Interface
res = ollama.chat(
    model = "deepseek-r1:7b",
    messages= [
        {"role": "user", "content": "Why is the sky blue?"},
    ],
    #Stream is on
    stream=True
)

#Chat feature response using ollama and stream it
for chunk in res:
    print(chunk["message"]["content"],end="", flush=True)

