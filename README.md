# ZeroDuino

ZeroDuino is a project that allows you to connect and control an Arduino board using a Raspberry Pi through a Python/Flask-based web interface.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The ZeroDuino project aims to provide a convenient way to interact with an Arduino board using a Raspberry Pi. By leveraging the power of Python and Flask, it allows you to control the Arduino's inputs and outputs through a web-based interface.

## Features

- Web-based interface for controlling Arduino inputs and outputs
- Real-time monitoring of Arduino sensor data
- Support for multiple Arduino boards
- Easy integration with existing Python projects

## Requirements

To use ZeroDuino, you will need the following:

- Raspberry Pi with Ubuntu 20.04 Server
- Arduino board
- Python 3.x
- Flask

## Installation

1. Clone the ZeroDuino repository to your Raspberry Pi:

    ```shell
    git clone https://github.com/caseybarajas/ZeroDuino.git
    ```

2. Install the required Python packages:

    ```shell
    pip install -r requirements.txt
    ```

3. Connect your Arduino board to the Raspberry Pi.

## Usage

1. Navigate to the project directory:

    ```shell
    cd ZeroDuino
    ```

2. Start the Flask server:

    ```shell
    python app.py
    ```

3. Open a web browser and enter the following URL:

    ```
    http://localhost:5000
    ```

4. You should now see the ZeroDuino web interface. Use it to control and monitor your Arduino board.

## Contributing

Contributions to the ZeroDuino project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).
