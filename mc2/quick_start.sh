#!/bin/bash

sudo /etc/init.d/ssh start
jupyter notebook --ip 0.0.0.0 --no-browser --port=8888 --allow-root

