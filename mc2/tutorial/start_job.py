import subprocess
import sys

def start_job(num_parties, memory, script_path):
    cmd = ["../dmlc-core/tracker/dmlc-submit", "--cluster", "ssh", "--num-workers", str(num_parties), "--host-file", "hosts.config", "--worker-memory", str(memory) + "g", "/opt/conda/bin/python3", script_path]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #while True:
    #    output = process.stdout.readline()
    #    if output == '' and process.poll() is not None:
    #        break
    #    if output:
    #        print(output.strip())
    #rc = process.poll()
    #return rc
    for line in iter(process.stdout.readline, b''):
        sys.stdout.write(line)
