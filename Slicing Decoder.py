#Slicing decoder
message = input("Enter a message to decode: ")
start = int(input("Enter the start index for slicing: "))
end = int(input("Enter the end index for slicing: "))
step = int(input("Enter the step value for slicing: "))
decoded_message = message[start:end:step]
print("Decoded message:", decoded_message)