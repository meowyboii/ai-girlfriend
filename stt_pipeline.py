import torch
import torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load Whisper ASR model
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

def speech_to_text(audio):
    """Convert speech to text using Whisper ASR."""
    # Load and preprocess audio
    waveform, sample_rate = torchaudio.load(audio)

    # Ensure correct sample rate (Whisper expects 16kHz)
    if sample_rate != 16000:
        waveform = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)(waveform)

    # Convert to model input format
    input_features = processor(waveform.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_features

    # Generate transcription
    with torch.no_grad():
        predicted_ids = model.generate(input_features)

    # Decode output
    user_input = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]

    return user_input