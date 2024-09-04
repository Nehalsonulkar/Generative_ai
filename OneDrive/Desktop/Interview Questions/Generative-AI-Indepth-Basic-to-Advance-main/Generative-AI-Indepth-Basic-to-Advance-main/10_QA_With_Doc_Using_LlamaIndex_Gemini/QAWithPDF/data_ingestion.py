from llama_index.core import SimpleDirectoryReader
import sys
from Exception import customexception
from Logger import logging

def load_data(data):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary.
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data")   ## Here we are reading the data
        documents=loader.load_data()       ## Here we loading the data 
        logging.info("data loading completed...")
        return documents    ## Here we returning a particular documents
    except Exception as e:
        logging.info("exception in loading data...")
        raise customexception(e,sys)



    