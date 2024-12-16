from SshToServer import SshToServer
import os


def getResponse(ssh_obj: SshToServer, command: str) -> str:
    stdout, stderr = ssh_obj.runRemoteCommand(command)
    return stdout

key_pair = input("Input key-pair path: ")
public_ip = input("Input public ip: ")
user_name = input("Input user name: ")
server_side_script_path = input("Input path of server script (from ~): ")

my_ssh = SshToServer(key_pair, public_ip, user_name)
response = getResponse(my_ssh, f"python3 {server_side_script_path}")

if response == "":
    raise ValueError("ERROR no response")

csv_file = "stat.csv"
if os.path.exists(csv_file):
    with open(csv_file, 'a') as file:
        file.write(response)
else:
    with open(csv_file, "w") as file:
        file.writelines(("timestamp,INFO,WARN,ERROR\n", response))
