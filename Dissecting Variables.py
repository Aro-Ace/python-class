#Dissecting Variables
user_input = input("type something: ")
print('are there only spaces?', user_input.isspace())
print('is it a number?', user_input.isdigit())
print('is it alphabetic?', user_input.isalpha())
print('is it alphanumeric?', user_input.isalnum())
print('is it lowercase?', user_input.islower())
print('is it uppercase?', user_input.isupper())
print('is it capital case?', user_input.istitle())
