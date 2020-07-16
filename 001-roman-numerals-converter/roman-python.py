from flask import Flask, render_template, request

app = Flask(__name__)

def roman_con(num):
    mappings = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    result = ""
    for k,v in mappings.items():
        value = num // k
        result += v * value
        num%=k
    
    return result


@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', devoloper_name='Rehab', not_valid = False)

@app.route('/' ,methods=['POST'])
def main_post():
    x = request.form['number']
    if not x.isdecimal():
       return render_template('index.html', devoloper_name='Rehab', not_valid=True)
    number = int(x)
    if not 0 < number < 4000:
       return render_template('index.html', name='Rehab', not_valid=True)
    return render_template('result.html', number_decimal=number, number_roman=roman_con(number), devoloper_name='Rehab')


@app.route('/')
def home():
    return render_template('index.html', name='Rehab')




if __name__ == '__main__':
    #app.run(debug=True)
    app.run('0.0.0.0', port=80)