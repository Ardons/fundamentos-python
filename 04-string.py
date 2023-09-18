name = "Lina"
last_name = "Olejua"
print(name)
print(last_name)

# Concatenacion
full_name = name + " " + last_name
print(full_name)

quote = "I'am Alvaro"
print(quote)

quote2 = 'She said "hello"'
print(quote2)

# format
template = "Hola, mi nombre es: " + name + " y mi apellido es: " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print(template)

template = f'Hola, mi nombre es {name} y mi apellido es {last_name}'
print(template)