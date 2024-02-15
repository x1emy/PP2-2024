import json

with open('sample-data.json','r') as file:
    data=json.load(file)
things=data['imdata']
print("Interface status")
print("="*80)
print("DN                                                 Speed   Deccription          MTU  ")
print("-------------------------------------------------- -----   -------------------- ------")
for i in things:
    dn=i["l1PhysIf"]["attributes"]["dn"]
    speed=i["l1PhysIf"]["attributes"]["speed"]
    mtu=i["l1PhysIf"]["attributes"]["mtu"]

    if 'eth1/33' in dn or 'eth1/34' in dn or 'eth1/35' in dn:
        print(dn, " " * 7, speed, " " *20, mtu)
    