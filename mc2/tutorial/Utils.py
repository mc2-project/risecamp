import subprocess
import sys
import _thread
import securexgboost as mc2

def start_server(clients):
    enclave = ["python3", "utils/launch_enclave.py", str(clients)]
    orchestrator = ["python3", "utils/start_orchestrator.py", str(clients)]
    process = subprocess.Popen(enclave)
    process2 = subprocess.Popen(orchestrator)
    print("Started server")
                         
def transfer_data(data, ip):
    print("Transferring {} to {}".format(data, ip))
    cmd = ["scp", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", 
                    data, "root@{}:/home/mc2/risecamp/mc2/tutorial/central/".format(ip)]
    run_subprocess(cmd)
    
def generate_certificate(username):
    cmd = ["./config/gen-client.sh", username]
    run_subprocess(cmd)
    
def run_subprocess(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(process.stdout.readline, b''):
        line = line.decode("utf-8")
        sys.stdout.write(line)

