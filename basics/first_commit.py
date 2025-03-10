import subprocess

def get_first_commit_for_host_in_file(host_name, file_name):
    # Build the git log command to search for the host name in the specific file
    command = ['git', 'log', '-S', host_name, '--', file_name]
    
    # Run the git log command
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        # Process the output, we want the first commit (oldest)
        log_output = result.stdout.strip()
        
        # If there are commits, return the first one
        if log_output:
            # Extract commit hash and message (we're assuming 'oneline' format)
            first_commit = log_output.splitlines()[0]
            return first_commit
        else:
            print("No matching commits found.")
            return None
    else:
        print("Error:", result.stderr)
        return None

"""
# Example Usage
host_name = "st14p01if-quln21050502"  # Replace with the actual host name you want to search for
file_name = "st.sparehosts"  # Replace with the file name you want to search in

# Collect the first commit details
first_commit = get_first_commit_for_host_in_file(host_name, file_name)
if first_commit:
    print("First commit details:", first_commit)
"""

host_names = []
file_names = ["<spare_hosts_file>"]  # List of files to search in

for host in host_names:
    for file in file_names:
        print(f"Searching for '{host}' in '{file}'...")
        first_commit = get_first_commit_for_host_in_file(host, file)
        if first_commit:
            print(f"First commit for host '{host}' in file '{file}': {first_commit}")
