#!/bin/bash

sudo /etc/init.d/ssh start
jupyter notebook --ip "*" --no-browser --port=8890 --allow-root --NotebookApp.token='' --NotebookApp.password=''
