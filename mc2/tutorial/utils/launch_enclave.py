import securexgboost as mc2
import _thread
import multiprocessing
import sys

def launch(clients):
    # Launch enclave
    print("launched enclave")
    enclave_image = "/home/mc2/secure-xgboost/build/enclave/xgboost_enclave.signed"
    mc2.init_server(enclave_image=enclave_image, client_list=clients)

    # Launch RPC server
    print("started enclave rpc server")
    print(clients)
    mc2.serve(all_users=clients, port=50051)
    
if __name__ == "__main__":
    num_clients = len(sys.argv[1]) 
    a = sys.argv[1][1:num_clients - 1] 
    clients_with_quotes = a.split(', ')
    clients = [client[1:len(client) - 1] for client in clients_with_quotes]
    launch(clients)

