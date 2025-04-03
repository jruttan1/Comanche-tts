import torch

# Paths (case-sensitive!)
pretrained_path = "/Users/jack/Library/Application Support/tts/tts_models--multilingual--multi-dataset--your_tts/model_file.pth"
modified_path = "/Users/jack/Desktop/text_to_audio/modified_model_file.pth"

# Load checkpoint
checkpoint = torch.load(pretrained_path, map_location="cpu")

# Expand language embeddings from 3 (en/es/fr) to 4 (including Comanche)
old_emb = checkpoint["model"]["emb_l.weight"]  # Shape [3, 4]
new_emb = torch.cat([old_emb, torch.randn(1, 4)], dim=0)  # Add Comanche embedding
checkpoint["model"]["emb_l.weight"] = new_emb  # New shape [4, 4]

# Save modified checkpoint
torch.save(checkpoint, modified_path)
print(f"Modified model saved to {modified_path}")
