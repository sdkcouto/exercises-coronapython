#Guest Book: Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.



greeting = "what is your name? "
greeting += "\n'q' for exit "
file_name = 'guest_book.txt'
with open(file_name,'w') as file_object:
    while True:
        greet = input(greeting)
      
        if greet == 'q':
            break
        
        file_object.write(greet + '\n')
        print("Wellcome " + greet+ ".")