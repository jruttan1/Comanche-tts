from TTS.api import TTS

model_path = "/Users/jack/Desktop/text_to_audio/model/modified_model_file.pth"
config_path = "/Users/jack/Desktop/text_to_audio/model/config.json"

try:
    tts = TTS(model_path=model_path, config_path=config_path)
    print("✅ Model initialized successfully!")
    
    # Test synthesis
    tts.tts_to_file(
        text="Nʉmʉnʉʉ haitʉ haniikuhu.",
        language="comanche",
        file_path="output.wav"
    )
except Exception as e:
    print(f"❌ Error: {e}")
