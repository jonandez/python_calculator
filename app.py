from flask import Flask, jsonify, request, render_template


app = Flask(__name__)


# -------------------- Index ---------------------
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# -------------------- sum ---------------------
@app.route('/suma/<a>/<b>', methods=['GET'])
def suma(a,b):
    if request.content_type == 'application/json':
        try:
            a = float(a)
            b = float(b)
            sum = a+b
            result = {"digit1": a, "digit2": b, "result": sum}

            return jsonify(result)

        except ValueError:
            result = {"digit1": a, "digit2": b, "result": "Invalid argument"}
            return jsonify(result)
    
    else:
        try:
            a = float(a)
            b = float(b)
            sum = a+b
            print("Sum template")
            return render_template("sum.html", digit1=a, digit2=b, result=sum)

        except ValueError:
            return render_template("invalid_argument.html", digit1=a, digit2=b)


# -------------------- odd ---------------------
@app.route('/resta/<a>/<b>', methods=['GET'])
def odd(a,b):
    if request.content_type == 'application/json':
        try:
            a = float(a)
            b = float(b)
            odd = a-b
            result = {"digit1": a, "digit2": b, "result": odd}

            return jsonify(result)

        except ValueError:
            result = {"digit1": a, "digit2": b, "result": "Invalid argument"}
            return jsonify(result)
    
    else:
        try:
            a = float(a)
            b = float(b)
            odd = a-b
            print("Sum template")
            return render_template("odd.html", digit1=a, digit2=b, result=odd)

        except ValueError:
            return render_template("invalid_argument.html", digit1=a, digit2=b)


# -------------------- multiply ---------------------
@app.route('/multiplicacion/<a>/<b>', methods=['GET'])
def mult(a,b):
    if request.content_type == 'application/json':
        try:
            a = float(a)
            b = float(b)
            mult = a*b
            result = {"digit1": a, "digit2": b, "result": mult}

            return jsonify(result)

        except ValueError:
            result = {"digit1": a, "digit2": b, "result": "Invalid argument"}
            return jsonify(result)
    
    else:
        try:
            a = float(a)
            b = float(b)
            mult = a*b
            print("Sum template")
            return render_template("multiply.html", digit1=a, digit2=b, result=mult)

        except ValueError:
            return render_template("invalid_argument.html", digit1=a, digit2=b)


# -------------------- Divide ---------------------
@app.route('/division/<a>/<b>', methods=['GET'])
def div(a,b):
    if request.content_type == 'application/json':
        try:
            a = float(a)
            b = float(b)
            div = a/b
            result = {"digit1": a, "digit2": b, "result": div}

            return jsonify(result)

        except ValueError:
            result = {"digit1": a, "digit2": b, "result": "Invalid argument"}
            return jsonify(result)
    
    else:
        try:
            a = float(a)
            b = float(b)
            div = a*b
            print("Sum template")
            return render_template("divide.html", digit1=a, digit2=b, result=div)

        except ValueError:
            return render_template("invalid_argument.html", digit1=a, digit2=b)


if __name__ == '__main__':
    app.run(port=8080, debug=True, host='0.0.0.0')
