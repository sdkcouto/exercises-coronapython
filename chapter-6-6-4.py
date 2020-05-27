#Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102) by replacing your series of print statements with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

programming_words = {'print' : 'pra printar',
    'if' : 'para condicionais',
    'and' : 'conjuncao para condicionais',
    'or' : 'conjuncao para condicionais',
    'str' : 'para transformar em string'
    }

programming_words['#'] = 'para comentarios'
programming_words['range'] = 'para series de numeros'

for name in programming_words.items():
    print(name)
programming_words['#'] = 'para comentarios'
    

