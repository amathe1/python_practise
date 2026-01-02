import subprocess
import re

# List of Cassandra nodes
nodes = [
 "mr81p01if-quln10121302-i1.mr.if.apple.com",
"mr81p01if-quln06100701-i1.mr.if.apple.com",
]

# Supported instances
supported_instances = [1, 2, 3, 4]

def extract_instance_number(hostname):
    """Extracts instance number from hostname like '-i1' or '-i4'."""
    match = re.search(r'-i(\d+)', hostname)
    return int(match.group(1)) if match else None

def run_commands_on_node(node):
    print(f"\n== Running on {node} ==")
    instance_number = extract_instance_number(node)

    if instance_number not in supported_instances:
        print(f"⚠️  Skipping {node} — unsupported instance '-i{instance_number}'")
        return

    # Build instance-specific disablegossip command
    disable_cmd = f"nodetool {instance_number} disablegossip"
    enable_cmd = f"nodetool {instance_number} enablegossip"

    commands = [disable_cmd, "sleep 5", enable_cmd]

    for cmd in commands:
        full_cmd = f'ssh {node} "{cmd}"'
        try:
            print(f"Executing: {full_cmd}")
            result = subprocess.run(full_cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(result.stdout.decode())
            if result.stderr:
                print("stderr:", result.stderr.decode())
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed on {node}: {e.stderr.decode()}")

# Run for all nodes
for node in nodes:
    run_commands_on_node(node)
