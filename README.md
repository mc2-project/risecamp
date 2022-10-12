# Sky Camp 2022

Welcome to the MC<sup>2</sup> tutorial for Sky Camp 2021. MC<sup>2</sup> is a platform for secure collaborative computation. In particular, for this tutorial we present [Secure XGBoost](https://github.com/mc2-project/secure-xgboost), a library for secure collaborative gradient boosted decision tree learning. In this tutorial, you'll collaborate with others to load encrypted data, train a model, and serve encrypted predictions. Below are instructions on how to set up and run the tutorial.

## Participant Instructions

1. **Install Docker Desktop for your platform:** [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

1. **Verify that Docker has been installed correctly**
    1. Mac: TODO
    2. Windows: TODO
    3. Linux: TODO

1. **Pull and run the docker image for the tutorial**
    
    View the image on Dockerhub [here](https://hub.docker.com/repository/docker/mc2project/skycamp2022/general)
    
    *Note that the image size is ~3.4gb, so make sure to have at least this much storage space available on your machine before running the below commands.*
    

```bash
# This command pulls the tutorial image from Dockerhub
docker pull mc2project/skycamp2022:v1

# This command is running docker with port binding on port 8888
# This is necessary for accessing the tutorial notebook in your local browser
# The `/home/mc2/risecamp/mc2/quick_start.sh` script contains commands to:
#  1. Start the ssh service on Linux (needed for tutorial)
#  2. Start a jupyter notebook on port 8888
docker run -p 8888:8888 -it mc2project/skycamp2022:v1 /home/mc2/risecamp/mc2/quick_start.sh
```

4. **You should see output similar to the following if the Jupyter notebook has started successfully**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fdcda775-e426-4c5f-8c73-101937a0ae71/Untitled.png)

5. **Navigate to the displayed url at [http://127.0.0.1:8888](http://127.0.0.1:8888/) to view the Jupyter notebook interface and click on** `Welcome - Start Here.ipynb` **to start the tutorial!**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2c3ced1-8cb9-456d-99f4-512616829ef8/Untitled.png)

6. **Leave feedback for the Sky Camp MC2 tutorial [here](https://forms.gle/mRZNqMHa9Xgcrg9F6) 🙏**