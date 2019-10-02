import subprocess

def start_job(num_parties, memory, script_path):
    cmd = ["dmlc-core/tracker/dmlc-submit", "--cluster", "ssh", "--num-workers", str(num_parties), "--host-file", "hosts.config", "--worker-memory", str(memory), "python3", script_path]
    print(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc
