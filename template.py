
from pathlib import Path
import os,sys
import logging

project_name="mlproject"

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

try:
    for filepath in list_of_files:
        filepath=Path(filepath)
        filedir,filename=os.path.split(filepath)

        if filedir!="":
            os.makedirs(filedir,exist_ok=True)
            logging.info(f"created Directory: {filedir}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:
            with open(filepath,"w") as f:
                pass
            logging.info(f"created file: {filepath}")

    else:
        logging.info(f"{filename} already exists")


except Exception as e:
    logging.info(f"Encountered Error : {e}")


    
