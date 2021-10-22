# RISE Camp 2021

Welcome to the MC<sup>2</sup> tutorial for RISE Camp 2021. MC<sup>2</sup> is a platform for secure collaborative computation. In particular, for this tutorial we present [Secure XGBoost](https://github.com/mc2-project/secure-xgboost), a library for secure collaborative gradient boosted decision tree learning. In this tutorial, you'll collaborate with others to load encrypted data, train a model, and serve encrypted predictions. Below are instructions on how to set up and run the tutorial.

## Cloud Setup
Azure Confidential Computing offers [virtual machines with Intel SGX support](https://azure.microsoft.com/en-us/blog/dcsv2series-vm-now-generally-available-from-azure-confidential-computing/) that you can use with MC2. You can also choose to use non enclave machines, in which case you'll need to build our library in simulation mode, as explained below. 

Follow the README in the [Secure XGBoost repository](https://github.com/mc2-project/secure-xgboost) to install Secure XGBoost. If using a machine without enclave support, build the library in simulation mode -- take a look at step 5 of the ["Installation"](https://github.com/mc2-project/secure-xgboost#installation) section. 

Once you've installed Secure XGBoost, clone this repository, navigate to `risecamp/mc2/tutorial/`, and start two separate Jupyter servers from that directory. We need two servers as we'll be representing two different clients -- each client needs to have its own separate process.

If you spin up the notebooks on a VM, you can either 

1) open up the Jupyter ports (8888,8889) under the VM's network configuration and navigate to `<VM_IP>:888{8,9}` (one notebook will be running on port 8888 and the other will be running on port 8889)

2) SSH into the VM with port-forwarding enabled, as shown in the below script.

```
#!/bin/bash

# Change the IP address (or machine name) with each restart.

ADDR=$1
NAME=mc2
LHOST=localhost
SSHKEY=$HOME/.ssh/id_rsa          # change if necessary to the name of your private key file

for i in `seq 8888 8900`; do
    FORWARDS[$((2*i))]="-L"
    FORWARDS[$((2*i+1))]="$i:${LHOST}:$i"
done

ssh -i ${SSHKEY} -X ${FORWARDS[@]} -l ${NAME} ${ADDR}
```

To run this, copy the above into a bash script `ssh.sh` and run the script: `./ssh.sh <VM_IP>`.
