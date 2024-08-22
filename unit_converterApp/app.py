from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        'millimeter': 1,
        'centimeter': 10,
        'meter': 1000,
        'kilometer': 1000000,
        'inch': 25.4,
        'foot': 304.8,
        'yard': 914.4,
        'mile': 1609344,
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'milligram': 1,
        'gram': 1000,
        'kilogram': 1000000,
        'ounce': 28349.5,
        'pound': 453592,
        'lbs': 453592,  # Adding pounds (lbs)
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    value = float(request.form['value'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit']
    unit_type = request.form['unit_type']

    if unit_type == 'length':
        result = convert_length(value, from_unit, to_unit)
    elif unit_type == 'weight':
        result = convert_weight(value, from_unit, to_unit)
    elif unit_type == 'temperature':
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = "Unsupported conversion"

    return render_template('index.html', result=result, value=value, from_unit=from_unit, to_unit=to_unit)

if __name__ == '__main__':
    app.run(debug=True)
