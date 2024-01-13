# Your code goes here:
def render_person(name, date_of_birth, eye_color, years_old, gender):
    return f'{name} is a {years_old} years old {gender} born in {date_of_birth} with {eye_color} eyes'


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))