# MoodWave

MoodWave is an open-source project that aims to transform voices by infusing emotional characteristics. The project utilizes a transformer-based neural network to modify the emotional tone of input voice recordings.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Inference](#inference)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

MoodWave is designed to enhance voice transformations, allowing users to modify the emotional characteristics of voice recordings. Whether you want to add excitement, calmness, or other emotions to your voice, MoodWave provides a customizable solution.

## Features

- Voice transformation with emotional characteristics
- Customizable emotional tones
- Easy-to-use interface for both training and inference

## Getting Started

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/MoodWave.git
    ```

2. Navigate to the project directory:

    ```bash
    cd MoodWave
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

- Follow the instructions in the [Usage Guide](docs/usage_guide.md) to get started with transforming voices using MoodWave.

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

- **Happiness**
- **Sadness**
- **Anger**
- **Fear**
- **Disgust**
- **Neutral**
- **Excitement**
- **Pride**
- **Aversion**
- **Surprise**

## Images

![MoodWave Training](img/MoodWave%20Training.png)
*Image 1: Visualization of the MoodWave Training Process*

![MoodWave IO process](img/MoodWave%20IO%20process.png)
*Image 2: Visualization of the MoodWave Input/Output Process*

## Contributing

We welcome contributions from the community! If you have suggestions, bug reports, or want to contribute to the development of MoodWave, please refer to [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- The MoodWave team extends gratitude to the open-source community for their continuous support and contributions.
