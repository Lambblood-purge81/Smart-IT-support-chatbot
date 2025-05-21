from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Use TinyLlama model
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set up the text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)  # -1 = CPU

# Define the AI assistant function
def get_ai_response(prompt):
    full_prompt = f"You are an expert IT support assistant. Help the user step by step:\n\nUser: {prompt}\nAssistant:"
    response = generator(full_prompt, max_length=500, temperature=0.7, do_sample=True)[0]["generated_text"]
    return response.replace(full_prompt, "").strip()
