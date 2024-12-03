for i in range(5):
    print("Starting the loop : " +str(i))
    stop = input("Do you want to stop the loop (y/n) ? ")
    if stop == "y":
        break
    print("Ending the loop : " +str(i))

print("PROGRAM FINISHED! ")