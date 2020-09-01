language = 'Python'

print(len(language))
# the len() modifier tells print to count the number of characters in the given variable,
# and output the length in a number. In this example, it should print 6

print(language[0])
# This is how to access an individual index in a given variable.
# This should output the letter "P"

print(language[0:3])
# This will print "Pyt" by using the ':' to tell Python where to start and end
print(language[3:])  # Prints "hon"
print(language[1:3])  # Prints "yt"
print(language[:4])  # Prints "Pyth"

print(language[-1])  # Prints while starting at the end of

# String Methods
# --------------

# Uppercase
example_string_uppercase = 'upper'
upper_example = example_string_uppercase.upper()
print(upper_example)

# Lowercase
example_string_lowercase = 'LOWER'
lower_example = example_string_lowercase.lower()
print(lower_example)
