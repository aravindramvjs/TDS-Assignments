import os
import subprocess
import whisper
from pytube import YouTube
from pydub import AudioSegment
import sys

# Ensure correct NumPy version
try:
    import numpy as np
    if int(np.__version__.split(".")[0]) >= 2:
        print("Downgrading NumPy to a compatible version...")
        subprocess.run([sys.executable, "-m", "pip", "install", "numpy<2"], check=True)
        print("Restart the script after downgrading NumPy.")
        sys.exit(1)
except ImportError:
    print("NumPy is not installed. Installing a compatible version...")
    subprocess.run([sys.executable, "-m", "pip", "install", "numpy<2"], check=True)
    print("Restart the script after installing NumPy.")
    sys.exit(1)

# Set YouTube Video URL
VIDEO_URL = "https://www.youtube.com/watch?v=NRntuOJu4ok"

# Define file paths
OUTPUT_AUDIO = "audio.mp3"
TRIMMED_AUDIO = "trimmed_audio.mp3"

# Step 1: Download the audio using yt-dlp with retry mechanism
def download_audio(video_url, output_audio):
    command = f'yt-dlp -x --audio-format mp3 -o "{output_audio}" "{video_url}"'
    for attempt in range(3):  # Retry up to 3 times
        try:
            subprocess.run(command, shell=True, check=True)
            print("Download successful!")
            return
        except subprocess.CalledProcessError as e:
            print(f"Attempt {attempt + 1}: yt-dlp failed ({e}). Retrying...")
    print("Failed to download audio. Try using --cookies-from-browser.")
    sys.exit(1)

# Step 2: Trim the audio

def trim_audio(input_audio, output_audio, start_time, end_time):
    audio = AudioSegment.from_file(input_audio, format="mp3")
    trimmed_audio = audio[start_time * 1000 : end_time * 1000]  # Convert seconds to milliseconds
    trimmed_audio.export(output_audio, format="mp3")

# Step 3: Transcribe the trimmed audio

def transcribe_audio(audio_path):
    model = whisper.load_model("medium")  # Choose "tiny", "base", "small", "medium", or "large"
    result = model.transcribe(audio_path)
    return result["text"]

# Execute Steps
download_audio(VIDEO_URL, OUTPUT_AUDIO)  # Step 1: Download audio
trim_audio(OUTPUT_AUDIO, TRIMMED_AUDIO, 222.1, 321.8)  # Step 2: Trim audio
transcript = transcribe_audio(TRIMMED_AUDIO)  # Step 3: Transcribe

# Print transcript
print("Transcribed Text:\n", transcript)
