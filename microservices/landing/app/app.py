from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    port = 5051
    s_type = "addition"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def minus(n1, n2):
    port = 5052
    s_type = "subtraction"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def multiply(n1, n2):
    port = 5053
    s_type = "multiplication"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def divide(n1, n2):
    port = 5054
    s_type = "division"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def modulo(n1, n2):
    port = 5055
    s_type = "modulo"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def exponent(n1, n2):
    port = 5056
    s_type = "exponent"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]

def gcd(n1, n2):
    port = 5057
    s_type = "gcd"
    url = f"http://{s_type}-service:{port}/{n1}/{n2}"
    response = requests.get(url)
    return response.json()["result"]


@app.route('/', methods=['POST', 'GET'])
def index():
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
        operation = request.form.get('operation')
        result = 0
        if operation == 'add':
            result = add(number_1, number_2)
        elif operation == 'minus':
            result =  minus(number_1, number_2)
        elif operation == 'multiply':
            result = multiply(number_1, number_2)
        elif operation == 'divide':
            if number_2 == 0:
                raise ZeroDivisionError
            result = divide(number_1, number_2)
        elif operation == "modulo":
            if number_2 == 0:
                raise ZeroDivisionError
            result = modulo(number_1, number_2)
        elif operation == "exponent":
            if number_1 == 0 and number_2 < 0:
                raise ZeroDivisionError
            result = exponent(number_1, number_2)
        elif operation == "gcd":
            result = gcd(number_1, number_2)

    except ZeroDivisionError:
        flash("Cannot divide by 0")
    except:
        flash("Input 2 valid integers and select the desired operation to perform")
    else:
        flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    finally:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )