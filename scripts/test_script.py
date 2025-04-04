from TTS.api import TTS

# Paths to your custom files
config_path = "/Users/jack/Desktop/text_to_audio/model/config.json"
model_path = "/Users/jack/Desktop/text_to_audio/model/modified_model_file.pth"

# Initialize the model with custom paths
try:
    tts = TTS(model_path=model_path, config_path=config_path)
    print("Model initialized successfully.")

    print("Available speakers:", tts.speakers) # Available speakers: ['female-en-5', 'female-en-5\n', 'female-pt-4\n', 'male-en-2', 'male-en-2\n', 'male-pt-3\n']

    # Test synthesis
    tts.tts_to_file(
        text="Hello, this is a test of text-to-speech.",
        language="comanche",  # Replace with your desired language
        speaker="female-en-5",  # Replace with a valid speaker ID from speakers.json (if applicable)
        file_path="output.wav"
    )
    print("Speech synthesis complete. Check output.wav.")
except Exception as e:
    print("Error during model initialization or synthesis:", e)
