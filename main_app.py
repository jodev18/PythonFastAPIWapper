"""
    Main file for handling

"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def main_root():
    """
    Main root application
    :return:
    """
    return{"Message":"Hello World!"}




