import json
import pandas as pd

with open('vmss.json') as f:
  data = json.load(f)

ips = []

for vm in data["value"]:
    ip = vm["properties"]["ipAddress"]
    ips.append(ip + ":8888")

#  print(ips)

df = pd.DataFrame(ips)
df.to_csv("ip.csv", index=False)
