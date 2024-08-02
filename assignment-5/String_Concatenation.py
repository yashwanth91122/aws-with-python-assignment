# Using + operator
str1 = "Hello"
str2 = "World"
str3 = str1 + " " + str2
print(str3)  # "Hello World"

# Using join() method
words = ["Hello", "World"]
after_join = " ".join(words)
print(after_join)  # "Hello World"

# Using formatted string literals (f-strings)
str1 = "Hello"
str2 = "World"
formatted_string = f"{str1} {str2}"
print(formatted_string)  # "Hello World"