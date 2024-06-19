import os
import numpy as np
import librosa
import librosa.feature
import sklearn
from sklearn.preprocessing import StandardScaler



# Function to load audio data from directory
def load_audio_data(directory):
    audio_data = []
    sample_rates = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.wav'):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            try:
                # Load audio file
                audio, sample_rate = librosa.load(file_path, sr=None)
                audio_data.append(audio)
                sample_rates.append(sample_rate)
                print(f"Loaded {filename} successfully.")
            except Exception as e:
                print(f"Failed to load {filename}: {e}")

    return audio_data, sample_rates


# Function to extract features from audio data
def extract_features(audio_data, sample_rate):
    # Initialize empty lists to store features
    mfccs = []
    spectral_centroids = []
    spectral_rolloff = []

    # Iterate over audio samples
    for audio in audio_data:
        # Extract MFCCs (Mel-frequency cepstral coefficients)
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=13)
        mfccs.append(np.mean(mfcc, axis=1))  # Take the mean of MFCCs over time

        # Extract spectral centroid
        centroid = librosa.feature.spectral_centroid(y=audio, sr=sample_rate)
        spectral_centroids.append(np.mean(centroid))

        # Extract spectral rolloff
        rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sample_rate)
        spectral_rolloff.append(np.mean(rolloff))

    # Convert lists to numpy arrays
    mfccs = np.array(mfccs)
    spectral_centroids = np.array(spectral_centroids)
    spectral_rolloff = np.array(spectral_rolloff)

    # Stack features horizontally to create feature matrix
    features = np.hstack((mfccs, spectral_centroids.reshape(-1, 1), spectral_rolloff.reshape(-1, 1)))

    return features


# Function to normalize features
def normalize_features(features):
    # Perform feature-wise normalization
    scaler = sklearn.preprocessing.StandardScaler()
    features_normalized = scaler.fit_transform(features)

    return features_normalized

def save_features(features, filename):
    np.savetxt(filename, features, delimiter=',')  # Save features to a CSV file

# Main function
def main():
    # Directory containing the WAV files
    directory = 'C:\\Users\\ACHAPI-STATION\\Desktop\\wav'

    # Load audio data
    audio_data, sample_rates = load_audio_data(directory)

    # Extract features from audio data
    features = extract_features(audio_data, sample_rates[0])  # Assuming all audio samples have the same sample rate

    # Normalize features
    features_normalized = normalize_features(features)

    # Print shape of the normalized feature matrix
    print("Shape of normalized feature matrix:", features_normalized.shape)

    # Assuming features_normalized is the normalized feature matrix
    # Display the first few rows of the normalized features in the terminal
    print("Normalized Features:")
    print(features_normalized[:5])  # Display the first 5 rows

    # Save the normalized features to a file
    save_features(features_normalized, 'normalized_features.csv')
    print("Normalized features saved to 'normalized_features.csv'")


# Entry point of the script
if __name__ == "__main__":
    main()
