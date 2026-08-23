# Data Types in Python

from pyscript import display, document

name = 'Keane Alexis L. Pacana'
age = 16
height = 162.32
countries_to_visit = ['Japan','Australia','Denmark']
student_type = False
sample_dictionary = {'color':'green','car_brand':'toyota', 'shoe_size':'8.5', 'best_friend':'Almakram Cody Basty'}
favorite_fruits = {'avocado', 'blueberry', 'mango', 'banana', 'dragon fruit!!!'}
seven_days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


document.getElementById('result').innerHTML = f' <h1>Understanding Data Types</h1> Name: {name}<br> Age: {age}<br> Height: {height} cm <br> Countries I want to visit: {countries_to_visit}<br> Student Type: {student_type}<br> Dictionary: {sample_dictionary}<br>  Favorite Fruits: {favorite_fruits}<br> Days of the Week: {seven_days}<br>'
