"""
continue keyword will ignore, rest of the code next to it in loop ;
but it won't exit loop like break statement

"""

for i in range(5):
    print("Starting the loop : " +str(i))
    stop = input("Do you want to stop the loop (y/n) ? ")
    if stop == "y":
        continue 
    print("Ending the loop : " +str(i))
    

print("PROGRAM FINISHED! ")