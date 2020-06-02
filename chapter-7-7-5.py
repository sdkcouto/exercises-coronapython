#Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.


ages = '\nHow old are you?'
ages += "\nEnter 'quit' when you are finished."
while True:
    age = input(ages)
    if age == 'quit':
        break
    elif int(age) < 3:
        print('The entrance is free.')
    elif int(age) > 3 and int(age) < 12:
        print('The ticket is $10.')
    else:
        print('The ticket is $15')
