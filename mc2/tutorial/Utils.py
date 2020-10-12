import subprocess
import sys
import _thread
import securexgboost as mc2

def start_rpc_orchestrator(clients):
    print("start rpc orchestrator")
    mc2.serve(all_users=clients, nodes=["127.0.0.1"], port=50052)
    
def launch_enclave(clients):
    print("launched enclave")
    enclave_image = "/home/mc2/secure-xgboost/build/enclave/xgboost_enclave.signed"
    mc2.init_server(enclave_image=enclave_image, client_list=clients)

def start_enclave_rpc_server(clients):
    print("started enclave rpc server")
    mc2.serve(all_users=clients, port=50051)
    
def start_server(clients):
    _thread.start_new_thread(start_rpc_orchestrator, (clients,))
    _thread.start_new_thread(start_enclave_rpc_server, (clients,))
    _thread.start_new_thread(launch_enclave, (clients,))
                         
                         
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
