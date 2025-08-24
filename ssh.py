import paramiko
import getpass

# SSH connection details
hostname = input("Enter hostname or IP: ")
port = 22  # default SSH port
username = input("Enter SSH username: ")
password = getpass.getpass("Enter SSH password: ")

def ssh_login(hostname, port, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port, username, password)

        stdin, stdout, stderr = client.exec_command('whoami')
        print("Logged in as:", stdout.read().decode().strip())

        client.close()

    except paramiko.AuthenticationException:
        print("Authentication failed. Please check your username/password.")
    except paramiko.SSHException as sshException:
        print(f"SSH connection error: {sshException}")
    except Exception as e:
        print(f"Error: {e}")

ssh_login(hostname, port, username, password)
