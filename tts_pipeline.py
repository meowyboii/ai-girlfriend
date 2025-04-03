from kokoro import KPipeline
import soundfile as sf
import sounddevice as sd

# Initialize Kokoro TTS pipeline
pipeline = KPipeline(lang_code='a')

def play_response(text):
    """Convert AI response to speech and play it."""
    generator = pipeline(text, voice='af_nicole')
    for i, (gs, ps, audio) in enumerate(generator):
        sf.write("temp.wav", audio, 24000)  # Create temporary wav file
        sd.play(audio, 24000)  # Play the audio
        sd.wait()  # Wait until playback is finished