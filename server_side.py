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
    segments = line.split()
    if len(segments) < 6 :
        continue
    severity = segments[5]
    if severity == "INFO":
        info += 1
    elif severity == "WARN":
        warn += 1
    elif severity == "ERROR":
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
