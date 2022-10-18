import subprocess
import sys
import os
import psutil
import securexgboost as mc2

running_processes = []

def start_server(clients):
    global running_processes
    
    if not isinstance(clients, list):
        print("Argument to `start_server()` must be a list but was {}".format(type(clients)))
        return

    if running_processes:
    # Kill any running instances of the orchestrator and enclave process from prior runs
        for ps in running_processes:
            ps.kill()
        running_processes = []
    
    # As a secondary check, kill any orchestrator or enclave processes which may have been left over 
    mypid = os.getpid()
    for proc in psutil.process_iter():
        if proc.pid != mypid and proc.name == 'utils/launch_enclave.py' or proc.name == 'utils/start_orchestrator.py':
            proc.kill()
        
    enclave = ["python3", "utils/launch_enclave.py", str(clients)]
    orchestrator = ["python3", "utils/start_orchestrator.py", str(clients)]
    
    process = subprocess.Popen(enclave, preexec_fn=os.setsid)
    running_processes.append(process)
    
    process2 = subprocess.Popen(orchestrator, preexec_fn=os.setsid)
    running_processes.append(process2)
    print("Started server")
                         
def transfer_data(data, ip):
    print("Transferring {} to {}".format(data, ip))
    cmd = ["scp", "-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null", 
                    data, "root@{}:/home/mc2/skycamp/mc2/tutorial/central/".format(ip)]
    run_subprocess(cmd)
    
def generate_certificate(username):
    cmd = ["./config/gen-client.sh", username]
    run_subprocess(cmd)
    
def run_subprocess(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(process.stdout.readline, b''):
        line = line.decode("utf-8")
        sys.stdout.write(line)

