import subprocess
import sys

def transfer_data(data, ip):
    cmd = ["scp", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", 
                    data, "root@{}:~".format(ip)]
    run_subprocess(cmd)
    
def generate_certificate(username):
    cmd = ["./config/gen-client.sh", username]
    run_subprocess(cmd)
    
def run_subprocess(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(process.stdout.readline, b''):
        line = line.decode("utf-8")
        sys.stdout.write(line)
