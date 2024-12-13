import streamlit as st
import librosa
import numpy as np
import keras
from io import BytesIO
import keras

# Load your trained model
model = keras.models.load_model("C:\\Users\\axelf\\Downloads\\model.h5")

# Function to preprocess audio file
def preprocess_audio(audio_file, suitable_length):
    # Load audio file
    y, sr = librosa.load(audio_file, sr=None)  # Load with original sample rate
    # Ensure length matches suitable_length
    if len(y) > suitable_length:
        y = y[:suitable_length]
    else:
        y = np.pad(y, (0, max(0, suitable_length - len(y))), mode='constant')
    return y

# Streamlit frontend setup
def main():
    st.title("Scream Detection Model Demo")
    st.write("Upload a .wav audio file to detect if it contains a scream.")

    # Upload .wav file for prediction
    uploaded_file = st.file_uploader("Choose a .wav file", type=["wav"])

    if uploaded_file is not None:
        # Read the file as a byte stream
        audio_bytes = uploaded_file.read()
        audio_file = BytesIO(audio_bytes)  # Convert to byte stream for librosa
        
        # Read input dimension for the model
        with open("D://Universidad//Lambton//Third_Term//Neural Networks//Human_Scream_Detection_using_ml_and_deep_learning-main//scream_detection_main//input dimension for model.txt", "r") as file:
            suitable_length_for_model = int(file.read().strip())

        # Preprocess the uploaded audio file
        audio_data = preprocess_audio(audio_file, suitable_length_for_model)

        # Reshape data to be compatible with the model input
        X2 = np.array([audio_data])  # Create a batch of size 1

        # Make predictions with the model
        predictions = model.predict(X2)
    

        # Round predictions to get binary results (0 or 1)
        rounded = [round(x[0]) for x in predictions]

        # Display the results
        if predictions >= 0.397:
            st.warning("Scream detected!")
            print(rounded[0])
        else:
            st.success("No scream detected.")
            print(rounded[0])
            print(predictions)

if __name__ == "__main__":
    main()
