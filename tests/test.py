import mlflow
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Path to the MLflow model artifact
artifact_uri = "/content/model/model_state_dict.pth"  # Direct path to the artifact / Model

# Download the artifact locally from mlflow using artifact URI
local_path = mlflow.artifacts.download_artifacts(artifact_uri=artifact_uri)

# Check if CUDA (GPU) is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the tokenizer and base model
base_model_name = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(base_model_name)
model = AutoModelForCausalLM.from_pretrained(base_model_name).to(device)

# Load the fine-tuned state dictionary onto the GPU
state_dict = torch.load(local_path, map_location=device)

# Update the base model with the fine-tuned weights
model.load_state_dict(state_dict)

# Set the model to evaluation mode
model.eval()

# Test the model with an example input
test_input = "generate a simple python documentation"
inputs = tokenizer(test_input, return_tensors="pt").to(device)  # Move inputs to GPU

# Generate predictions
with torch.no_grad():
    outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)

# Decode the output
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Generated Text:")
print(generated_text)




