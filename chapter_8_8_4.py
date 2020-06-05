#Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size,message):
    print("The shirt size is " + size +  " and the message is " + "'" + message + "'" + ".")
make_shirt(size = 'Large',message='I love python')
make_shirt('large',message = "c'est la vie")
make_shirt('medium',message = "c'est la vie")
make_shirt('XL',message = 'I am fat')