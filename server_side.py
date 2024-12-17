import subprocess


def getTimestamp():
    command = "date +%s"
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout[:-1]


timestamp = getTimestamp()

log_file = "/var/log/syslog"
with open(log_file) as file:
    lines = file.readlines()

info, warn, error = 0, 0, 0
for line in lines:
    line = line.lower()
    if 'info' in line:
        info += 1
    elif 'warn' in line:
        warn += 1
    elif 'error' in line:
        error += 1


print(
f"""
{{
"timestamp": {timestamp},
"INFO": {info},
"WARN": {warn},
"ERROR": {error} 
}}
"""
)