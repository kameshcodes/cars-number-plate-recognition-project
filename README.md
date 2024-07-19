# Car Number Plate Detection

## Overview

This project aims to develop a system to detect and read vehicle number plates from images. The system uses Object Detection techniques to locate the number plate in a picture and Optical Character Recognition (OCR) to convert the plate’s characters into readable text.

The application flow of the project is illustrated below:

![Application Flow](imgs/application-flow.png)


## Technologies Used

- **Deep Learning Framework**: PyTorch
- **Object Detection**: Faster R-CNN (or another method based on your implementation)
- **OCR**: Paddle OCR
- **Programming Language**: Python

## Installation Instructions

### Prerequisites

Ensure you have Python 3 installed on your system. If not, you can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

1. **Clone the repository to your local machine:**

    ```bash
    git clone https://github.com/kameshcodes/car-number-plate-detection.git
    ```
    
    ```bash
    cd car-number-plate-detection
    ```

### Project Setup

1. **Create a Virtual Environment:**

    ```bash
    python -m venv venv_name
    ```

   - **On Windows:**

    ```bash
    venv_name\Scripts\activate
    ```

   - **On macOS and Linux:**

    ```bash
    source venv_name/bin/activate
    ```

2. **Upgrade pip to the latest version:**

    ```bash
    python -m pip install --upgrade pip
    ```

3. **Install Requirements and Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Connect Virtual Environment to Jupyter Kernel:**

    ```bash
    pip install ipykernel 
    python -m ipykernel install --user --name=venv_name --display-name venv_name
    ```

5. **Add Kaggle API:**

   To access Kaggle datasets from kaggle for downloading, you need a Kaggle API key. Follow these steps:

   - **Obtain Kaggle API Key:**
     - Log in to your Kaggle account.
     - Go to your [Kaggle Account Settings](https://www.kaggle.com/settings).
     - Scroll down to the **API** section and click **Create New API Token**. This will download a `.kaggle` folder containing the `kaggle.json` file.
     - Open the `kaggle.json` file inside `.kaggle` directory and retrieve:
       - `your_username` - your Kaggle username
       - `your_api_key` - your Kaggle API key

   - **Add Credentials to `.env` File:**
     1. Create a new `.env` file inside project directory.
     2. Add the following lines to the `.env` file:

        ```plaintext
        KAGGLE_USERNAME=your_username
        KAGGLE_KEY=your_api_key
        ```

   **Note:** Ensure that the `.env` file is not included in version control. Add it to `.gitignore` to keep your credentials secure.