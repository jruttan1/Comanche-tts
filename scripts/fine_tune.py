from trainer import Trainer, TrainerArgs
from TTS.config import load_config
from TTS.tts.models import setup_model
from TTS.utils.audio import AudioProcessor
import os

# Paths (case-sensitive!)
config_path = "/Users/jack/Desktop/text_to_audio/model/config.json"
restore_path = "/Users/jack/Desktop/text_to_audio/modified_model_file.pth"
output_path = "/Users/jack/Desktop/text_to_audio/fine_tuned_model/"

# Verify paths
print("Config exists:", os.path.exists(config_path))  # Must return True
print("Model exists:", os.path.exists(restore_path))  # Must return True

# Load config
config = load_config(config_path)

# Initialize components
ap = AudioProcessor.init_from_config(config)
model = setup_model(config)
model.load_checkpoint(config, restore_path, strict=False)  # Allow embedding mismatch

# Initialize trainer
trainer = Trainer(
    TrainerArgs(),
    config,
    output_path,
    model=model,
    train_samples=[],
    eval_samples=[],
    training_assets={"audio_processor": ap}
)

# Start training
trainer.fit()
