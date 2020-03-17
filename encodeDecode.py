choice = input("Encode (e) or Decode (d)? ")
choice = choice.lower()
if (choice == "e" or choice == "encode"):
    choice = "encode"
elif (choice == "d" or choice == "decode"):
    choice = "decode"
else:
    print("That's not a choice!")
    quit()
input_text = input("What should I "+choice+"? ")
output_text = ""
how_far_to_change_characters = 10
characters = list(input_text)
if (choice == "encode"):
    print("Encoding \""+input_text+"\"...")
    for letter in characters:
        letter_as_number = ord(letter)
        letter_as_number_adjusted = letter_as_number + how_far_to_change_characters
        new_letter = chr(letter_as_number_adjusted)
        # print("Encoding "+letter+" as "+new_letter+" ("+str(letter_as_number)+","+str(letter_as_number_adjusted)+")")
        output_text += new_letter
else:
    print("Decoding \""+input_text+"\"...")
    for letter in characters:
        letter_as_number = ord(letter)
        letter_as_number_adjusted = letter_as_number - how_far_to_change_characters
        new_letter = chr(letter_as_number_adjusted)
        # print("Decoding "+letter+" as "+new_letter+" ("+str(letter_as_number)+","+str(letter_as_number_adjusted)+")")        
        output_text += new_letter
print("Output: "+output_text)