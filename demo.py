from flask import Flask
from census_income.logger import logging

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    logging.info("checking logging file is working or not")
    return "working on a project"


if __name__ == '__main__':
    app.run(debug=True)
