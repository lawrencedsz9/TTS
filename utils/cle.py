import os
import logging

logger = logging.getLogger(__name__)

def cleanup_file(filename: str):
    """Clean up a file after it's been sent"""
    try:
        if os.path.exists(filename):
            os.remove(filename)
            logger.info(f"Cleaned up file: {filename}")
    except Exception as e:
        logger.error(f"Error cleaning up file {filename}: {str(e)}")