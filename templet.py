import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(message)s')


project_name = "disease-classifier"


list_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f'src/{project_name}/utils/__init__.py',
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/traials.ipynb",
    "templates/index.html"
]


for filepath in list_file:
    filepath = Path(filepath)
    fildir,filename = os.path.split(filepath)
    
    if fildir !="":
        os.makedirs(fildir,exist_ok=True)
        logging.info('filedirector is created ')
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info("creating file")
    else:
        logging.info('file already exits')
    import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s] %(message)s')


project_name = "nlp"


list_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f'src/{project_name}/utils/__init__.py',
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/traials.ipynb",
    "templates/index.html"
]


for filepath in list_file:
    filepath = Path(filepath)
    fildir,filename = os.path.split(filepath)
    
    if fildir !="":
        os.makedirs(fildir,exist_ok=True)
        logging.info('filedirector is created ')
        
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info("creating file")
    else:
        logging.info('file already exits')
    