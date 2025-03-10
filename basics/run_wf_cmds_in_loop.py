import time
import subprocess


# Path to your file containing the commands
file_path = "/tmp/1"

# Function to run the commands with a 5-minute interval
def run_commands_with_interval(file_path):
    # Open the file and read each command
    with open(file_path, 'r') as file:
        commands = file.readlines()

    # Loop through each command
    for command in commands:
        command = command.strip()  # Remove any extra whitespace/newlines
        if command:
            print(f"Running command: {command}")
            # Run the command
            subprocess.run(command, shell=True)

            # Wait for 5 minutes before running the next command
            print("Waiting for 5 minutes before the next command...")
            time.sleep(5 * 60)  # 5 minutes in seconds

# Run the function
if __name__ == "__main__":
    run_commands_with_interval(file_path)

