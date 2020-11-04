# RISE Camp 2020

Welcome to the MC<sup>2</sup> tutorial for RISE Camp 2020. MC<sup>2</sup> is a platform for secure collaborative computation. In particular, for this tutorial we present [Secure XGBoost](https://github.com/mc2-project/secure-xgboost), a library for secure collaborative gradient boosted decision tree learning. In this tutorial, you'll collaborate with others to load encrypted data, train a model, and serve encrypted predictions. Below are instructions on how to set up and run the tutorial.

## Cloud Setup
Azure Confidential Computing offers [virtual machines with Intel SGX support](https://azure.microsoft.com/en-us/blog/dcsv2series-vm-now-generally-available-from-azure-confidential-computing/) that you can use with MC2. You can also choose to use non enclave machines, in which case you'll need to build our library in simulation mode, as explained below. 

Follow the README in the [Secure XGBoost repository](https://github.com/mc2-project/secure-xgboost) to install Secure XGBoost. If using a machine without enclave support, build the library in simulation mode -- take a look at step 5 of the ["Installation"](https://github.com/mc2-project/secure-xgboost#installation) section. 

Once you've installed Secure XGBoost, clone this repository, navigate to `risecamp/mc2/tutorial/`, and start a Jupyter server. Begin the tutorial with Exercise 1. 

## Docker Setup
Alternatively, if you choose not to use the cloud, you can also choose to use Docker. However, if you use Docker, there will likely be issues with networking, so you may only be able to do the tutorial by yourself as a collaboration of one. 

Pull the Docker image and start the container with proper port forwarding.

```sh
docker pull mc2project/risecamp:2020

docker run -it -p 50051:50051 -p 50052:50052 -p 8888:8888 -w /root/risecamp/mc2/tutorial/ mc2project/risecamp:2020 /bin/bash
```

You should now be inside the container in the `~/risecamp/mc2/tutorial/` directory. Start the Jupyter notebook.

```sh
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```

Navigate to the URL outputted to the console in a browser to access the notebook. Begin the tutorial with Exercise 1. 


