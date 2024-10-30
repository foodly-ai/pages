# app.py
from flask import Flask, render_template_string
import os
import random 


app = Flask(__name__)


@app.route('/')
def home():
    
    # Read the HTML file
    with open("products/Sion-Softside-Expandable-Roller-Luggage-Black-Checked-Large-29-Inch.html", 'r') as f:
        content = f.read()
    # with open("scrap.html", 'r') as f:
    #     content = f.read()
    
    # read script.js style.css buy-on-amazon-button-png-3.png
    # replace them to avoid path issues
    # Render the content
    return render_template_string(content)

if __name__ == '__main__':
    app.run(debug=True, port = 5050)
