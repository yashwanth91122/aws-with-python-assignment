# Using % operator
name = "ashwan"
age = 20
result = "My name is %s and I am %d years old." % (name, age)
print(result)  # "My name is Ashwan and I am 20 years old."

# Using str.format() method
result = "My name is {} and I am {} years old.".format(name, age)
print(result)  # "My name is Ashwan and I am 20 years old."

# Using formatted string literals (f-strings)
result = f"My name is {name} and I am {age} years old."
print(result)  # "My name is Ashwan and I am 20 years old."