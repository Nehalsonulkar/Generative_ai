import os
from pathlib import Path
import logging

## This list defines the files you want to create
## Here this files which we want to create 
list_of_files=[
    "QAWithPDF/__init__.py",   ## QAWithPDF is my folder and _init_.py is my file 
    "QAWithPDF/data_ingestion.py",
    "QAWithPDF/embeddings.py",
    "QAWithPDF/model_api.py",
    "QAWithPDF/helper.py",
    "Experiments/experiment.ipynb",
    "StreamlitApp.py",
    "logger.py",
    "exception.py",
    "setup.py"
    ]

for filepath in list_of_files:
   filepath = Path(filepath)
   filedir, filename = os.path.split(filepath)

   ## If my file directory is not empty then we created it 
   if filedir !="":
      os.makedirs(filedir, exist_ok=True)
      logging.info(f"Creating directory; {filedir} for the file {filename}")

   ## If the file doesn’t exist or is empty (has a size of 0), it creates an empty file by opening it in write mode ('w') and immediately closing it (pass does nothing, just a placeholder).

   if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
      with open(filepath, 'w') as f:
         pass
         logging.info(f"Creating empty file: {filepath}")

   else:
      logging.info(f"{filename} is already created")

      ## Code run krne ke bad jitne bhi file yaha pe mention ki hai vo automatically create ho jaygi 