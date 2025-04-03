from TTS.api import TTS

# Initialize the model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2")

# Option A: Use reference audio (voice cloning)
tts.tts_to_file(
    text="Your Comanche text here",
    speaker_wav="path/to/reference_audio.wav",  # Required for cloning
    language="en",                              # Must match model's supported languages
    file_path="output.wav"
)

# Option B: Use predefined speaker ID (if available)
tts.tts_to_file(
    text="Your Comanche text here",
    speaker="Ana Florence", # Example speaker name from the model
    language="en",
    file_path="output.wav"
)
