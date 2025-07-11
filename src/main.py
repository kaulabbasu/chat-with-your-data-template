import argparse
import asyncio
import os

from absl import logging
from genai_processors.core import audio_io
from genai_processors.core import live_model
from genai_processors.core import text
from genai_processors.core import video
from google.genai import types as genai_types
import pyaudio

# Input processor: combines camera streams and audio streams
input_processor = video.VideoIn('camera') + audio_io.PyAudioIn(pyaudio.PyAudio())

# Output processor: plays the audio parts. Handles interruptions and pauses


# Gemini Live API processor
live_processor = live_model.LiveProcessor(model_name='gemini-2.5-flash-preview-native-audio-dialog',
      realtime_config=genai_types.LiveConnectConfig(
          system_instruction=INSTRUCTION_PARTS,
          # Ground with Google Search
          tools=[genai_types.Tool(google_search=genai_types.GoogleSearch())],
          # Return the transcription of the model audio.
          output_audio_transcription={},
          # Enable affective dialog (only available for native audio out models)
          enable_affective_dialog=True,
          response_modalities=['AUDIO'],
          # Set the language for the Live API.
          speech_config={'language_code': 'en-US'},
      ),
      http_options=genai_types.HttpOptions(api_version='v1alpha'),)

# audio output when the user is speaking.
play_output = audio_io.PyAudioOut(pyaudio.PyAudio())

# Compose the agent: mic+camera -> Gemini Live API -> play audio
# live_processor = live_model.LiveProcessor(...)
live_agent = input_processor + live_processor + play_output

async for part in live_agent(streams.endless_stream()):
  # Process the output parts (e.g., print transcription, model output, metadata)
  print(part)
