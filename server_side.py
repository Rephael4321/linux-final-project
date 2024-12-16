import subprocess


def executeCommand(command):
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout[:-1]


def getTimestamp():
    command = "date +%s"
    result = executeCommand(command)
    return result

def getLines(look_for):
    log_file = "/var/log/syslog"
    command = f"grep -i '{look_for}' {log_file} | wc -l"
    result = executeCommand(command)
    return result


timestamp = getTimestamp()
info_lines = getLines('info')
warning_lines = getLines('warn')
error_lines = getLines('error')

print(f"{timestamp},{info_lines},{warning_lines},{error_lines}")
