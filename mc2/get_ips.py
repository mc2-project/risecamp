import json

with open('vmss.json') as f:
  data = json.load(f)

ips = []

for vm in data["value"]:
    ip = vm["properties"]["ipAddress"]
    ips.append(ip)

print(ips)
