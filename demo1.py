from flask import Flask
from census_income.logger import logging
from census_income.exception import CustomException
import os,sys

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    try:
        raise Exception('we are testing the custom Exception class is working or not.')
    except Exception as e:
        census= CustomException(e, sys)
        logging.info(census.error_message)
        logging.info("testing logging file")


if __name__ == '__main__':
    app.run(debug=True)
