# MoodWave

MoodWave is an open-source project that aims to transform voices by infusing emotional characteristics. The project utilizes a transformer-based neural network to modify the emotional tone of input voice recordings.

## Table of Contents

- [Introduction](#introduction)
- [Ethical Use Statement](#ethical-use-statement)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Inference](#inference)
- [Dataset](#dataset)
- [License](#license)

## Introduction

MoodWave is designed to enhance voice transformations, allowing users to modify the emotional characteristics of voice recordings. Whether you want to add excitement, calmness, or other emotions to your voice, MoodWave provides a customizable solution.

## Ethical Use Statement

MoodWave is intended for responsible and ethical use. The project strongly discourages any misuse that could lead to deceptive practices, deep fakes, or any form of unethical application. Users are expected to adhere to the following ethical guidelines:

1. **Creative and Educational Purposes:**
   - MoodWave is developed for creative and educational purposes, empowering users to explore innovative ways of expressing emotions through voice transformation.

2. **Avoiding Misuse:**
   - Users are strictly advised against using MoodWave for deceptive or malicious purposes, including the creation of content with the intent to deceive, impersonate, or harm others.

3. **Respecting Privacy:**
   - MoodWave respects privacy rights. Users should obtain proper consent before using someone's voice for transformation and should refrain from using the technology to infringe upon individuals' privacy.

4. **Legal Compliance:**
   - Ensure that your usage of MoodWave complies with all relevant laws and regulations regarding privacy, consent, and the ethical use of synthesized voices.

5. **Transparency and Disclosure:**
   - Be transparent about the capabilities and limitations of MoodWave. Clearly communicate the project's intended use to help users make responsible choices.

6. **Security Measures:**
   - Implement security measures to prevent unauthorized access or misuse of MoodWave, safeguarding against potential deceptive content creation without proper authorization.

By using MoodWave, you acknowledge and agree to adhere to these ethical guidelines. The project maintains a commitment to ethical development practices and encourages users to contribute to positive and creative applications.

## Features

- Voice transformation with emotional characteristics
- Customizable emotional tones
- Easy-to-use interface for both training and inference


## Model Architecture

MoodWave employs a transformer-based neural network architecture for voice transformation. The model consists of an encoder-decoder pair with attention mechanisms to capture sequential dependencies and emotional characteristics.

For more details, refer to [Model Architecture](docs/model_architecture.md).

## Training

To train the MoodWave model on your own dataset, follow the steps outlined in [Training Guide](docs/training_guide.md). Ensure that your dataset includes paired examples of input voice features and corresponding transformed voice features with emotion labels.

## Inference

After training, you can use the trained model for voice transformation. Refer to [Inference Guide](docs/inference_guide.md) for instructions on running inference with the pre-trained model or your own trained model.

## Dataset

MoodWave performs best when trained on a diverse dataset of voice recordings that cover a wide range of emotions. The dataset is structured by emotion categories, allowing the model to learn transformations specific to each emotional context.

### Emotions:

-**Happiness**
-**Disappointment**
-**Sadness**
-**Anger**
-**Worry**
-**Fear**
-**Disgust**
-**Agreement**
-**Disagreement**
-**Neutral**
-**Excitement**
-**Pride**
-**Assertive**
-**Urgency**
-**Surprise**
-**Seductive**
-**Frustrated**
-**Reminiscent**
-**Bored**
-**Shy**

## Images

![MoodWave Training](img/MoodWave%20Training.png)
*Image 1: Visualization of the MoodWave Training Process*

![MoodWave IO process](img/MoodWave%20IO%20process.png)
*Image 2: Visualization of the MoodWave Input/Output Process*


## License

This project is licensed under the [MIT License](LICENSE.md).

