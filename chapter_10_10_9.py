#Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

cats_files = 'cats.txt'
dogs_files = 'dogs.txt'
    
try:
    dogs = open(dogs_files)
    for line in dogs:
        print(line)  
    dogs.close()         
except FileNotFoundError:
    pass

try:
    cats = open(cats_files)  
    for line in cats:
        print(line)
    cats.close()        
except FileNotFoundError:
    pass