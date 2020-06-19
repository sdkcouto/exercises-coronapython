#Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

cats_files = 'cats.txt'
dogs_files = 'dogs.txt'
    
try:
    dogs = open(dogs_files)
    for line in dogs:
        print(line)  
    dogs.close()         
except FileNotFoundError:
    print("Sorry, i couldn't find this file: {0}".format(dogs_files))


try:
    cats = open(cats_files)  
    for line in cats:
        print(line)
    cats.close()        
except FileNotFoundError:
    print("Sorry, i couldn't find this file: {0}".format(cats_files))


