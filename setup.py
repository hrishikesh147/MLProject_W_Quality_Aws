from setuptools import setup,find_packages

NAME="end to end ml"
VERSION="0.0.0.1"
DESCRIPTION="machine elarning project in AWS"
AUTHOR="hrishikesh bhagawati"
AUTHOR_EMAIL="hrishikeshbhagawati@gmail.com"
URL="https://github.com/hrishikesh147/MLProject_W_Quality_Aws.git"

REQUIREMENTS="requirements.txt"
HYPHEN_E_DOT="-e ."

def get_requirements_list():
    with open(REQUIREMENTS, "r") as req:
        req=req.readlines()
        req=[i.replace("\n","") for i in req] 

    for i in req:
        if i==HYPHEN_E_DOT:
            req.remove(HYPHEN_E_DOT)

    return req


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      packages=find_packages(),
      install_requires=get_requirements_list()
     )