from pyscript import display, document

#For the Periodic Table Element Checker tab
periodic_table= {
    'H': ('Hydrogen', 'Nonmetal', 1, 1.0078),
    'He': ('Helium', 'Nonmetal (Noble Gas)', 2, 4.0026),
    'Li': ('Lithium', 'Metal', 3, 6.9410),
    'Be': ('Beryllium', 'Metal', 4, 9.0122),
    'B': ('Boron', 'Metalloid', 5, 10.811),
    'C': ('Carbon', 'Nonmetal', 6, 12.011),
    'N': ('Nitrogen', 'Nonmetal', 7, 14.007),
    'O': ('Oxygen', 'Nonmetal', 8, 15.999),
    'F': ('Fluorine', 'Nonmetal', 9, 18.998),
    'Ne': ('Neon', 'Nonmetal (Noble Gas)', 10, 20.180),
    'Na': ('Sodium', 'Metal', 11, 22.990),
    'Mg': ('Magnesium', 'Metal', 12, 24.305),
    'Al': ('Aluminium', 'Metal', 13, 26.982),
    'Si': ('Silicon', 'Metalloid', 14, 28.086),
    'P': ('Phosphorus', 'Nonmetal', 15, 30.974),
    'S': ('Sulfur', 'Nonmetal', 16, 32.065),
    'Cl': ('Chlorine', 'Nonmetal', 17, 35.453),
    'Ar': ('Argon', 'Nonmetal (Noble Gas)', 18, 39.948),
    'K': ('Potassium', 'Metal', 19, 39.098),
    'Ca': ('Calcium', 'Metal', 20, 40.078),
    'Sc': ('Scandium', 'Metal', 21, 44.956),
    'Ti': ('Titanium', 'Metal', 22, 47.867),
    'V': ('Vanadium', 'Metal', 23, 50.942),
    'Cr': ('Chromium', 'Metal', 24, 51.996),
    'Mn': ('Manganese', 'Metal', 25, 54.938),
    'Fe': ('Iron', 'Metal', 26, 55.845),
    'Co': ('Cobalt', 'Metal', 27, 58.933),
    'Ni': ('Nickel', 'Metal', 28, 58.693),
    'Cu': ('Copper', 'Metal', 29, 63.546),
    'Zn': ('Zinc', 'Metal', 30, 65.380),
    'Ga': ('Gallium', 'Metal', 31, 69.723),
    'Ge': ('Germanium', 'Metalloid', 32, 72.640),
    'As': ('Arsenic', 'Metalloid', 33, 74.922),
    'Se': ('Selenium', 'Nonmetal', 34, 78,960),
    'Br': ('Bromine', 'Nonmetal', 35, 79.904),
    'Kr': ('Krypton', 'Nonmetal (Noble Gas)', 36, 83.798),
    'I': ('Iodine', 'Nonmetal', 53, 126.90),
    'Xe': ('Xenon', 'Nonmetal (Noble Gas)', 54, 131.29),
    'Rn': ('Radon', 'Nonmetal (Noble Gas)', 86, 222),
} #All nonmetal elements, WITH the addition of a few more elements
# This is more variety, I also added their type/classification because I might use this.


def checkE(e):
    document.getElementById('element-result').innerHTML = ""
    
    element = document.getElementById('symbol-input').value.strip().title()
    #I think this part of the code takes the symbol input from the text box and formats it for checking

    # .get - no if statements
    details = periodic_table.get(element, ('Element not found','N/A','',''))
    #I think this one checks if the element in the input box is a valid key in the dictionary to grab its value
    # If the key doesn't exist, it gets the other value which is the tuple

    document.getElementById('element-result').innerHTML = f"""
    <b>Symbol</b> {element} <br>
    <b>Element</b> {details[0]} <br>
    <b>Type</b> {details[1]} <br>
    <b>Atomic Number</b> {details[2]} <br>
    <b>Atomic Mass</b> {details[3]}
    """

    #The {} are placeholders. I researched using w3schools, here are the source links I used in order to understand the code:
    # https://www.w3schools.com/python/python_string_formatting.asp https://www.w3schools.com/python/ref_dictionary_get.asp
    #basically I remembered that we can get specific elements in a tuple using index number starting from 0


#For Club Membership Checker:

SSCMembers = ['Sage Aguinaldo', 'Cyra Cheang', 'Michael Barrameda', 'Mikaela Lindaya', 'Andrey Santos', 'Heather Son']


def clubCheck(e):
    document.getElementById('club-result').innerHTML = ""

    first = document.getElementById('fname').value
    last = document.getElementById('lname').value
    candidate = first + ' ' + last
    checker = candidate.title() in SSCMembers

    notification = (f"""Greetings, <b>{candidate}</b><br><br> We are sorry, but you are not a member of the Social Sciences Club at the moment""",
                    f"""Good day, <b>{candidate}</b><br><br> We are pleased to inform that you are a member of the Social Sciences Club""")
    #I fixed and improved the f string by referencing the Element Checker code & using triple double quotation marks (""""""), which fixed it

    document.getElementById('club-result').innerHTML = notification[checker]

    

#I made use of this source link for study reference too: https://peps.python.org/pep-0008/