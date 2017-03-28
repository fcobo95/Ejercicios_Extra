from flask import Flask, json, jsonify, redirect, request, Response, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return redirect('/api/welcome/', code=302)


@app.route('/api/welcome/', methods=['GET'])
def welcome_screen():
    return render_template('mainpage.html')


def params():
    return request.args


@app.route('/api/even_or_odd/', methods=['GET', 'POST'])
def determine_even_or_odd():
    param = params()

    number = param['number']

    if int(number) % 2 == 0:
        isEven = {
            'Result': 'It is Even!',
            'number': number
        }
    else:
        isEven = {
            'Result': 'It is Odd!!',
            'number': number
        }

    return Response(json.dumps(isEven), mimetype='application/json')


    # @app.route('/api/is_it_prime', methods=['GET'])
    # def is_it_prime():
    #     param = params()
    #
    #     number = param['number']

    # Tarea Vectores Erick Fernando Cobo Enriquez 3/27/2017


# This method will handle request to calculate the square root of 1000 numbers that go into an array.
@app.route('/api/square-root/', methods=['GET'])
def square_roots():
    the_result_array = []
    the_array = []
    # I fill the_array with float values
    for el_valor in range(1000):
        the_array.append(float(el_valor))
    """
    I iterate through all the values of "the_array" and calculate their respective square root value
    it then appends it to "the_result_array" and transforms it into a JSON.
    """
    for each_number in the_array:
        square_root = each_number ** (1 / 2)
        the_result_array.append({
            "Number": each_number,
            "Square Root": square_root
        })
    the_JSON_result = json.dumps(the_result_array)
    return Response(the_JSON_result, status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='localhost')
