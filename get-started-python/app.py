#!/usr/bin/python
from flask import Flask
import os  
from config import devConfig,prodConfig 

app = Flask(__name__)

port = int(os.getenv('PORT', 5500))

import os
if os.environ['ENV'] == 'prod':
    prodConfig()
elif os.environ['ENV'] == 'dev':
    devConfig()

@app.route('/')
def root():
    return "Hello Intel"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
