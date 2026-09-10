# GEN-AI

A collection of small Python scripts exploring core Generative AI / LLM concepts — starting with tokenization and embeddings.

## 📂 Contents

| File | Description |
|------|-------------|
| [`tokenization.py`](./tokenization.py) | Takes user input text, encodes it into tokens using OpenAI's `gpt-4o` tokenizer (via `tiktoken`), then decodes the tokens back to verify the round-trip. |
| [`embeddings.py`](./embeddings.py) | Connects to a local [Ollama](https://ollama.com/) instance and generates text embeddings using the `nomic-embed-text` model, printing the vector dimensions and sample values. |

## 🛠️ Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running locally (for `embeddings.py`)
- The `nomic-embed-text` model pulled in Ollama:
  ```bash
  ollama pull nomic-embed-text
  ```

## 📦 Installation

```bash
git clone https://github.com/Omrawat11/GEN-AI.git
cd GEN-AI
pip install openai tiktoken
```

## 🚀 Usage

### Tokenization

Run the script and enter any sentence to see it tokenized and decoded:

```bash
python tokenization.py
```

Example:
```
Enter your sentence: Hello world!
Tokens [13225, 2375, 0]
Decoded Hello world!
```

### Embeddings

Make sure Ollama is running on `127.0.0.1:11434`, then run:

```bash
python embeddings.py
```

This will print the embedding vector's dimensions and a preview of its values for a sample sentence about the Eiffel Tower.

## 🎯 Purpose

This repo is a learning space for understanding the building blocks of Generative AI — how raw text becomes tokens, and how text becomes numerical embeddings that models can reason over.

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome via issues or pull requests.

## 📄 License

No license specified yet — consider adding one (e.g. MIT) if you'd like others to freely use this code.
