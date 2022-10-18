#!/bin/bash

sudo /etc/init.d/ssh start
jupyter lab --ip "*" --no-browser --port=8890 --allow-root --notebook-dir=/home/mc2/skycamp/mc2/tutorial --NotebookApp.token='SkyCamp2022'
