# Human Scream Detection - 

## Authors
- Ingrid Guevara - [c0919292@mylambton.ca](mailto:c0919292@mylambton.ca)
- Axel Cano - [c0914678@mylambton.ca](mailto:c0914678@mylambton.ca)
- Dev Parmar - [c0908036@mylambton.ca](mailto:c0908036@mylambton.ca)
- Aniketh Vaglapuram - [c0903304@mylambton.ca](mailto:c0903304@mylambton.ca)

## Introduction

Crime rates are rising globally, often due to delayed law enforcement responses caused by a lack of accurate and timely information. This project aims to develop a system that detects human screams in real-time using machine learning, which can help provide immediate alerts and potentially reduce crime response times.

## Methodology

### Approach
The system utilizes machine learning and deep learning models, specifically:
- **Support Vector Machines (SVM)**
- **Multilayer Perceptron (MLP)**

### Key Features
- Binary classification (scream vs. non-scream)
- Integration of advanced audio processing techniques

### Support Vector Machine (SVM)
- **Purpose**: Detect human screams in audio data.
- **Dataset**:
  - Positive Class: 2,000 scream instances
  - Negative Class: 3,000 non-scream sounds
- **Functionality**: Categorizes audio using the decision function \( f(x) = \text{sign}(w \cdot x + b) \).

### Multilayer Perceptron (MLP)
- **Role**: Enhances detection reliability by validating SVM outputs.
- **Capabilities**: Recognizes complex patterns in audio data using deep learning.

## Data Processing

- **Tool Used**: LibRosa library for feature extraction.
- **Key Feature Extracted**: Mel Frequency Cepstral Coefficients (MFCCs).
- **Importance of MFCCs**: Essential for understanding speech and audio characteristics.

## System Integration

- **Platform Used**: TensorFlow for model storage and execution.
- **Integration Benefits**: Ensures seamless collaboration between SVM and MLP models for robust detection performance.

## Results

The system achieved an accuracy of 75.5% in scream detection on test datasets. It displays results as "Scream Detected" or "No Scream Detected."

## Visual Results

Here are visual examples of the system's outputs:
- **No Scream Detected**: [Image]
- **Scream Detected**: [Image]

## Conclusion

The project successfully implemented a scream detection system using SVM and MLP models. Future enhancements include real-time classification capabilities and SMS notifications for detected screams.

## References

1. Chung, S., & Chung, Y. (2017). Scream sound detection based on SVM and GMM. IEEE.
2. Mathur, R., et al. (2022). Identification of Illicit Activities Using Deep Learning. IEEE.
3. O’Donovan, R., et al. (2020). Detecting Screams Using Transfer Machine Learning. JMIR.

---

Thank you for your interest in our project! We welcome feedback and contributions.
