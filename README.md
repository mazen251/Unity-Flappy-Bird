
# Unity Flappy Bird with Computer Vision

Welcome to the enhanced version of Flappy Bird using computer vision and MediaPipe! This repository contains the code and resources for a unique version of Flappy Bird where you can control the bird using your index finger through computer vision. The game integrates Python and C# with socket programming to achieve this functionality.

## Table of Contents
- [Introduction](#introduction)
- [Demo](#Demo)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Introduction

This project is a modified version of the classic Flappy Bird game. It uses computer vision techniques via MediaPipe to track the player's index finger movements, allowing them to control the bird's vertical position. The game communicates between Python and Unity using socket programming.

## Demo

![Scrn][scrns/img.png]

## Features

- **Computer Vision Control:** Play the game using your index finger.
- **Classic Game Logic:** The original Flappy Bird game logic is available and can be uncommented for a traditional gameplay experience.
- **Socket Programming:** Integrates Python and C# for real-time control.

## Installation

Follow these steps to set up the project on your local machine:

### Prerequisites

- Unity 2021 or later
- Python 3.x
- MediaPipe
- OpenCV
- Socket programming libraries

### Steps

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/mazen251/Unity-Flappy-Bird.git
    cd Unity-Flappy-Bird-master
    ```

2. **Set Up Python Environment:**
    ```sh
    # Navigate to the Python directory
    cd path/to/python/code

    # Install dependencies
    pip install -r requirements.txt
    ```

3. **Open Unity Project:**
    - Open Unity Hub and add the project folder.
    - Open the project in Unity.

4. **Download Ignored Resources:**
    Some resources are ignored in the `.gitignore` file. Make sure to download and place them correctly.
    ```sh
    # Download assets
    git lfs pull
    ```

## Usage

### Running the Game

1. **Run the Python Server:**
    - Open your preferred Python IDE.
    - Run the server socket script to start capturing hand landmarks.
    ```sh
    python hand_tracking_server.py
    ```

2. **Run the Unity Game:**
    - In Unity, run the game to start the Flappy Bird scene.
    - Use your index finger to control the bird's movements based on the captured landmarks.

3. **Classic Game Logic:**
    - To play the traditional Flappy Bird game, uncomment the normal game logic in the Unity C# scripts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

- Mazen Walid [LinkedIn](https://www.linkedin.com/in/mazen-walid-225582208/)

## Acknowledgements

- MediaPipe
- OpenCV
- Unity
- Python
