from tensorflow.keras.models import load_model
import numpy as np
import librosa

# Load the model
model = load_model(r'D:\backup\PROJECT\SER\models\cnn_model.h5')

# Load the WAV file
file_path = r'D:\backup\PROJECT\SER\speech-emotion-recognition\recording\recorded_audio.wav'
audio_data, _ = librosa.load(file_path, sr=16000)  # Adjust sr according to your audio data

# Preprocess your audio data
# For example, you might need to reshape and normalize the data
audio_data = np.expand_dims(audio_data, axis=0)  # Add batch dimension if necessary
# You might need to perform additional preprocessing based on how the model was trained

# Make predictions
predictions = model.predict(audio_data)

# Interpret predictions
# Replace this with your logic to interpret predictions
print(predictions)
