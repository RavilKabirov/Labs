import json
file_path = r"d:\PP2\Python\Lab4\sample-data.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Extract interfaces
interfaces = data["imdata"]

# Print the header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)

# Print interface details
for item in interfaces:
    interface = item["l1PhysIf"]["attributes"]
    dn = interface["dn"]
    description = interface.get("descr", "")  # Some descriptions might be missing
    speed = interface.get("speed", "inherit")
    mtu = interface.get("mtu", "")

    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")
