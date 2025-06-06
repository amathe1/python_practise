import pexpect

# Replace with your actual SSH credentials and command
ssh_user = "amathe1"
ssh_host = "mr44p01if-quld01180102.mr.if.apple.com"
command_to_run = "sudo -u pbossh fl rsync -t 40000 --forklift-file /cassandra/d1/opslogs/forklift-clouddb-clouddb_p62/clouddb_p62_mr.forklift --dc mr --env if-prod --app clouddb --cluster clouddb_p62"
first_password = "xxxx"
second_password = "#####"

# Start the SSH session
ssh_command = f"ssh {ssh_user}@{ssh_host}"
child = pexpect.spawn(ssh_command, encoding='utf-8')

# Log the output for debugging
child.logfile = open("ssh_log.txt", "w")

try:
    # Wait for the password prompt
    child.sendline("cd /cassandra/d1/opslogs")

    # Run your command
    child.sendline(command_to_run)

    child.expect("Password:", timeout=10)
    child.sendline(first_password)

    # Press enter (if needed)
    child.sendline("")

    # Wait for the shell prompt (assume it's a $, >, or #)
    child.expect("Password:", timeout=10)
    child.sendline(second_password)

    # Press enter (if needed)
    child.sendline("")

    print("Command executed successfully.")

except pexpect.exceptions.TIMEOUT:
    print("Timeout occurred during the SSH session.")
except pexpect.exceptions.EOF:
    print("Unexpected end of file. SSH session failed.")
finally:
    child.close()
