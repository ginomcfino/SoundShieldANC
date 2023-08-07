import sys
import numpy as np
from pydub import AudioSegment

def inverse_sound(input_file, output_file):
    audio = AudioSegment.from_file(input_file, format="m4a")

    audio = audio.set_channels(1)

    audio_data = np.array(audio.get_array_of_samples())

    inverted_audio_data = np.int16(np.iinfo(np.int16).max - audio_data)

    inverted_audio = AudioSegment(
        inverted_audio_data.tobytes(),
        frame_rate=audio.frame_rate,
        sample_width=audio.sample_width,
        channels=1
    )

    inverted_audio.export(output_file, format="wav")

output_file = "PyANC_outputs/test0.wav"
input_file = "SoundSamples/fenway_noise_0.m4a"

inverse_sound(input_file, output_file)