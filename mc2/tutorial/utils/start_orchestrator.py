import securexgboost as mc2
import sys

def start_rpc_orchestrator(clients):
    print("start rpc orchestrator")
    print(clients)
    mc2.serve(all_users=clients, nodes=["127.0.0.1"], port=50052)

if __name__ == "__main__":
    num_clients = len(sys.argv[1]) 
    a = sys.argv[1][1:num_clients - 1] 
    clients_with_quotes = a.split(', ')
    clients = [client[1:len(client) - 1] for client in clients_with_quotes]
    start_rpc_orchestrator(clients)
