from flask import Flask, render_template, request

app = Flask(__name__)


def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'multiply':
        return num1 * num2
    if operation == 'divide':
        if num2 == 0:
            return 'Cannot divide by zero'
        return num1 / num2
    return 'Invalid operation'


@app.route('/', methods=['GET', 'POST'])
def home():
    result = ''
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = calculator(num1, num2, operation)
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
