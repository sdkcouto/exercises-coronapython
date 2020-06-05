#Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

from chapter_8_8_13 import build_profile

user_profile = build_profile('andre', 'faria', age='30', nationality='brazilian', height='1,84')
print(user_profile)
