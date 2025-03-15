import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory if it doesn't exist
if not os.path.exists('lab1/logs'):
    os.makedirs('lab1/logs')

# Configure the logger
logger = logging.getLogger('cloudComputingLogger')
logger.setLevel(logging.INFO)

# Create a file handler that logs messages to a file
file_handler = RotatingFileHandler('lab1/logs/cloud_computing.log', maxBytes=5*1024*1024, backupCount=5)
file_handler.setLevel(logging.INFO)

# Create a console handler to log messages to the console (optional)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)