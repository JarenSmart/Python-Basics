first_name = "Jaren"  # Variable
last_name = "Smart"  # Variable

full_name = first_name + " " + last_name
# The variable above combines the first initial variables with a space in between
# marked by the quotes in the middle. Without the quotes the first_name and last_name
# variables would print --> JarenSmart INSTEAD of Jaren Smart
print(full_name)

greeting = f"Hello there, my name is {first_name} {last_name}"
# the 'f' in the beginning of the string is Pythons way of concatenating
print(greeting)

greeting_with_quotes = "Ed once said \"Magic is dead\" "
# the backslashes tell Python that we want it to print the quotes in the output
print(greeting_with_quotes)

greeting_with_triple_quotes = """This is a multi line
print statement
that allows you to print multiple
lines in the output
"""

print(greeting_with_triple_quotes)
