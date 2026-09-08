import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

# print("Vocab Size", encoder.n_vocab)

text = input("Enter your sentence: ")
tokens = encoder.encode(text) # encoder - convert sentence or text into tokens 

print("Tokens",tokens)

my_tokens = tokens
decoded = encoder.decode(my_tokens)

print("Decoded",decoded)