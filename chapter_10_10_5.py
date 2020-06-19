#Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

poll = input('why do you like programming? ')
poll += "\npress 'q' for quit " 
file_name = 'poll_results.txt'
with open(file_name,'w') as file_object:
    while True:
        polling = input(poll)
      
        if poll == 'q':
            break
        
        file_object.write(poll + '\n')
        