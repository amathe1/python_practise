import subprocess

# Function to run the command with the specified value
def run_command(n):
    # Construct the command with the given value of n
    command = f"/opt/ais/if/sre-tools/ststoragesre/bin/get_host.pl content/prod_p{n} | grep if.apple.com | cut -c1-2 | sort | uniq -c"
    
    # Debugging: print the command before running it
    print(f"Running command: {command}")
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Check if the command was successful
    if result.returncode == 0:
        # Print the captured output (standard output)
        print("Command output:")
        print(result.stdout)
    else:
        # If there was an error, print the error message (standard error)
        print(f"Error running command: {result.stderr}")

# Read input file containing the numbers
input_file = '/tmp/input.txt'  # Replace with your input file name

with open(input_file, 'r') as file:
    # Read each line in the file
    for line in file:
        line = line.strip()  # Remove any extra whitespace or newline characters
        if line.isdigit():  # Ensure the line is a number
            run_command(line)  # Run the command for the given number
