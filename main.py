# Working with Numbers
from pyscript import display, document

# Computing for the Area of a Trapezoid
def area_for_trapezoid(e):
    document.getElementById('output').innerHTML = " " # Limits the amount of clicks per computation by one

    addend1 = float(document.getElementById('Number_1').value)
    addend2 = float(document.getElementById('Number_2').value)
    addend3 = float(document.getElementById('height').value)

    sum = (addend1 + addend2) / 2 * addend3 # Formula

    display(f'The area of this trapezoid is {sum}', target='output')