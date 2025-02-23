# Step 1 (a): Setup Text to Speech-TTS-model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioObj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioObj.save(output_filepath)

input_text = "Hi I am AI with Danish"
# text_to_speech_with_gtts_old(input_text, output_filepath="my_gtts_testing.mp3")

# Step 1 (b): Setup Text to Speech-TTS-model with ElevanLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Jessica",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text, output_filepath="my_elevenlabs_testing.mp3")

# Step 2: Use Model for Text output to Voice
import subprocess
import platform

def play_audio(file_path):
    """Plays the audio file using the appropriate command for the OS."""
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', file_path])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{file_path}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', file_path])  # Proper MP3 playback
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"Error playing audio: {e}")

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"
    audioObj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioObj.save(output_filepath)
    print(f"gTTS audio saved: {output_filepath}")
    play_audio(output_filepath)

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Jessica",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    print(f"ElevenLabs audio saved: {output_filepath}")
    play_audio(output_filepath)

input_text = "Hi I am AI with Danish, autoplay testing"
text_to_speech_with_gtts(input_text, output_filepath="gtts_testing_autoplay.mp3")
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")