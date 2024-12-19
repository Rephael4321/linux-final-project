from SshToServer import SshToServer
import json
import pandas as pd
import os


def appendToCsv(file_path: str, data: dict) -> None:
    df_new = pd.DataFrame([data])
    if os.path.isfile(file_path):
        df_existing = pd.read_csv(file_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new
    df_combined.to_csv(file_path, index=False)


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
response = json.loads(response)
appendToCsv(csv_file, response)
