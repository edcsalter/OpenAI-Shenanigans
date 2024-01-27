import os
from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="All things considered, I'm not saying that he's a hoe... but he IS a hoe. The dude straight up belongs in the streets. No cap, you know what I'm saying?"
)
response.stream_to_file(speech_file_path)

os.system("mpg123 " + str(speech_file_path))
