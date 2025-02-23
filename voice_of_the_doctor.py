# Step 1 (a): Setup Text to Speech-TTS-model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioObj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioObj.save(output_filepath)

input_text = "Hi I am AI with Danish"
text_to_speech_with_gtts(input_text, output_filepath="my_gtts_testing.mp3")

# Step 1 (b): Setup Text to Speech-TTS-model with ElevanLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY") or "sk_dd0a3c4ae8e2d7a327d967e7987c1da7f39b684d9560d1b9"
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Jessica",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs(input_text, output_filepath="my_elevenlabs_testing.mp3")

# Step 2: Use Model for Text output to Voice