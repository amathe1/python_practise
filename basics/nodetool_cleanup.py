import os
import time

input_file = '/Users/Arunkumar_Mathe/Documents/nodetool_cleanup_cluster_list.txt'  # Your input file with app,cluster pairs
working_dir = '/Users/Arunkumar_Mathe/git/cass-wf-cli'  # Directory where you want to run the command

with open(input_file, 'r') as file:
    for line in file:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # Skip empty lines or comments

        parts = line.split(',')
        if len(parts) != 2:
            print(f"Skipping invalid line: {line}")
            continue
        
        app, cluster = parts[0].strip(), parts[1].strip()

        cmd = f'uv run cas-pbo-workflow nodetool-cleanup -e if-prod -a {app} -c {cluster} -m "rdar://161545519 (If-PROD : Run nodetool cleanup for system_auth across fleet)" -ks system_auth'        
        print(f"Running: {cmd} in {working_dir}")
        
        # Change directory, run command, then change back
        current_dir = os.getcwd()
        try:
            os.chdir(working_dir)
            os.system(cmd)
        finally:
            os.chdir(current_dir)

        print("Sleeping for 20 seconds...")
        time.sleep(20)
