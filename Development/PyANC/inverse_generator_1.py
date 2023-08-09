import numpy as np
from pydub import AudioSegment

# Function to inverse sound waves
def inverse_sound(input_file, output_file):
    # Load audio file
    audio = AudioSegment.from_file(input_file, format="m4a")

    # Get the audio data as a numpy array
    audio_data = np.array(audio.get_array_of_samples())

    # Check if audio is stereo
    if audio.channels == 2:
        # Split the stereo audio to left and right
        left = audio_data[::2]
        right = audio_data[1::2]

        # Invert the audio data
        left_inverted = np.int16(np.iinfo(np.int16).max - left)
        right_inverted = np.int16(np.iinfo(np.int16).max - right)

        # Interleave left and right inverted
        inverted_audio_data = np.column_stack((left_inverted, right_inverted)).ravel()
    else:
        # Invert the audio data
        inverted_audio_data = np.int16(np.iinfo(np.int16).max - audio_data)

    # Create a new AudioSegment from the inverted audio data
    inverted_audio = AudioSegment(
        inverted_audio_data.tobytes(), 
        frame_rate=audio.frame_rate, 
        sample_width=audio.sample_width, 
        channels=audio.channels
    )

    # Export the inverted audio data to a .wav file
    inverted_audio.export(output_file, format="wav")

output_file = "PyANC_outputs/test1.wav"
input_file = "SoundSamples/fenway_noise_0.m4a"

inverse_sound(input_file, output_file)