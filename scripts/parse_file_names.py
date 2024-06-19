import os

def parse_file_name(file_name):
    # Mapping between German emotion letters and English emotions
    emotion_mapping = {
        'W': 'anger',
        'L': 'boredom',
        'E': 'disgust',
        'A': 'anxiety',
        'F': 'happiness',
        'T': 'sadness',
        'N': 'neutral'
    }

    # Extract emotion code from file name
    emotion_code = file_name[5]

    # Map emotion code to emotional category
    emotion = emotion_mapping.get(emotion_code, 'unknown')

    return emotion
