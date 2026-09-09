from openai import OpenAI

# Connect to local Ollama instance (running on port 11434)
client = OpenAI(
    base_url="http://127.0.0.1:11434/v1",
    api_key="ollama"  # API key is required by the SDK but ignored by Ollama
)

text = "Effiel tower is in Paris and is a famous landmarks, it is 324 meters tall"

response = client.embeddings.create(
    input=text,
    model="nomic-embed-text"
)

print("Vector Dimensions:", len(response.data[0].embedding))
print("Vector Embeddings (first 10 values):", response.data[0].embedding[:10])
print("\nFull Vector:", response.data[0].embedding)

