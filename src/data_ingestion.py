import os
import zipfile
import logging
from dotenv import load_dotenv
import subprocess  # For running shell commands
from utils import setup_logger

load_dotenv()

# Setup logging
logger = setup_logger(__name__, logging.INFO)

def download_kaggle_dataset(dataset_name, download_dir):
    logger.info(f"Starting download for dataset '{dataset_name}'")

    try:
        os.makedirs(download_dir, exist_ok=True)

        # Set Kaggle API credentials in environment variables
        kaggle_username = os.getenv("KAGGLE_USERNAME")
        kaggle_key = os.getenv("KAGGLE_KEY")
        if not kaggle_username or not kaggle_key:
            logger.error("Kaggle API credentials not found. Please set KAGGLE_USERNAME and KAGGLE_KEY in the .env file.")
            return
        os.environ['KAGGLE_USERNAME'] = kaggle_username
        os.environ['KAGGLE_KEY'] = kaggle_key

        # Download the dataset
        command = f"kaggle datasets download -d {dataset_name} -p {download_dir}"
        logger.info(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            logger.error(f"Error downloading dataset: {result.stderr}")
            return

        # zip file path
        zip_file_name = f"{dataset_name.split('/')[1]}.zip"
        zip_file_path = os.path.join(download_dir, zip_file_name)

        if os.path.exists(zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(download_dir)
                logger.info(f"Extracted zip file '{zip_file_path}' to directory '{download_dir}'")
            os.remove(zip_file_path) 
            logger.info(f"Removed zip file '{zip_file_path}'.")
        else:
            logger.warning(f"Zip file '{zip_file_path}' does not exist. Extraction skipped.")

        logger.info(f"Dataset '{dataset_name}' downloaded and extracted to '{download_dir}'.\n")

    except FileNotFoundError as e:
        logger.error(f"File not found: {str(e)}")
    except zipfile.BadZipFile as e:
        logger.error(f"Bad zip file: {str(e)}")
    except Exception as e:
        logger.error(f"Failed to download dataset '{dataset_name}': {str(e)}\n")

if __name__ == "__main__":
    dataset_name = "aslanahmedov/number-plate-detection"  
    download_dir = os.path.join('data', 'raw')
    download_kaggle_dataset(dataset_name, download_dir)
