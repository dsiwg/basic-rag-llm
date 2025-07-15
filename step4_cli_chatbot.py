"""
step4_cli_chatbot.py

Allows someone to interact with a RAG-LLM via command line.

Loads vector db, embedding model, and text generation model. Specifies 
similarity function and chunk count. Creates prompt using user input,
similar chunks, and additional instructions. Passes text generation model
response back to user.

Author: David Sluder
Date: 2025-07-11
"""

print("Loading libraries.")
from pathlib import Path
from llama_cpp import Llama
from sentence_transformers import SentenceTransformer
import pickle 

# Import vector database
print("Loading vector database.")
VECTOR_DB_PATH = Path("./vector_db.pkl")
with open(VECTOR_DB_PATH, 'rb') as file:
    VECTOR_DB = pickle.load(file)

# Define similarity function
def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)

# Define function to calculate similarity and pull back most similar chunks
def retrieve(query, top_n=3):
  # Create embedding for user prompt
  query_embedding = embedding_model.encode(query)
  # Temporary list to store (chunk, similarity) pairs
  similarities = []
  # Iterate over embeddings in vector database and calc similarity
  for chunk, embedding in VECTOR_DB:
    similarity = cosine_similarity(query_embedding, embedding)
    similarities.append((chunk, similarity))
  # Sort by similarity in descending order
  similarities.sort(key=lambda x: x[1], reverse=True)
  # Return the top N most relevant chunks
  return similarities[:top_n]

# Load the models
print("Loading embedding model.")
embedding_model = SentenceTransformer("./models/embed/" + "all-MiniLM-L6-v2")
print("Loading text generation model.")
text_gen_model = Llama(
    model_path="./models/text_gen/Llama-3.2-1B-Instruct-Q4_K_L.gguf",
    n_ctx=2048,
    n_threads=8,
    verbose=False
)

def main():
    print("Local LLM Chat (type 'exit' to quit)")
    while True:
        user_input = input("\nEnter Prompt: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        retrieved_knowledge = retrieve(user_input)
        instruction_prompt = f'''You are a helpful chatbot.
        Use only the following pieces of context to answer the question. Don't make up any new information:
        {'\n'.join([f' - {chunk}' for chunk, similarity in retrieved_knowledge])}
        '''
        print("\nInstruction Prompt: " + instruction_prompt)
        print("Assistant Answer: ", end="", flush=True)
        for chunk in text_gen_model.create_chat_completion(
            messages = [
                {'role': 'system', 'content': instruction_prompt},
                {'role': 'user', 'content': user_input},
            ],
            stream=True
        ):
            print(chunk["choices"][0]["delta"].get("content", ""), end="", flush=True)

if __name__ == "__main__":
    main()
