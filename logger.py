from flask import Flask
import logging
import os,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import *

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("we are testing our logging file")
    return "welcome to the project"

if __name__=="__main__":
    app.run(debug=True)







    

