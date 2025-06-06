"""
Write a Python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number where,

Consider AL1 as the value for airline

src and dest should be the first three characters of the source and destination cities.

number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, then return the list of all generated ticket numbers.

"""

def generate_ticket_numbers(source, destination, passenger_count):
    airline = "AL1"
    src_code = source[:3].upper()
    dest_code = destination[:3].upper()
    base_number = 101
    
    tickets = []
    for i in range(passenger_count):
        ticket_number = f"{airline}:{src_code}:{dest_code}:{base_number + i}"
        tickets.append(ticket_number)
    
    # Return last 5 tickets (or all if less than 5)
    return tickets[-5:]

# 🔸 Example usage
source_city = "Chennai"
destination_city = "Mumbai"
passenger_count = 10

ticket_list = generate_ticket_numbers(source_city, destination_city, passenger_count)
print("Last 5 ticket numbers:")
for ticket in ticket_list:
    print(ticket)
