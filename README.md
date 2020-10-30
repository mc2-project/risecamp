# RISE Camp 2020

Welcome to the MC<sup>2</sup> tutorial for RISE Camp 2020. MC<sup>2</sup> is a platform for secure collaborative computation. In particular, for this tutorial we present [Secure XGBoost](https://github.com/mc2-project/secure-xgboost), a library for secure collaborative gradient boosted decision tree learning. Below are instructions on how to set up and run the tutorial.

## Setup
### Cloud Setup
Azure Confidential Computing offers [virtual machines with Intel SGX support](https://azure.microsoft.com/en-us/blog/dcsv2series-vm-now-generally-available-from-azure-confidential-computing/) that you can use with MC2. You can also choose to use non enclave machines, in which case you'll need to build our library in simulation mode, as explained below. 

### Docker Setup
If you choose not to use the cloud, you can also choose to use Docker. 

### Install Secure XGBoost
Follow the README in the [Secure XGBoost repository](https://github.com/mc2-project/secure-xgboost) to install Secure XGBoost. If using a machine without enclave support, build the library in simulation mode -- take a look at step 5 of the ["Installation"](https://github.com/mc2-project/secure-xgboost#installation) section. 

## Start the tutorial
Once you've installed Secure XGBoost, clone this repository and navigate to `risecamp/mc2/tutorial/`. Begin the tutorial with Exercise 1. You'll need multiple people doing the tutorial together for the tutorial.
