names = ["John Doe", "Alice Smith", "Bob Ford"]

for name in names:
    print(name.split()[0][0] + name.split()[1][0])
    
##  Extracting Initials Using Map
names = ["John Doe", "Alice Smith", "Bob Ford"]
initials = list(map(lambda name:''.join([n[0] for n in name.split()]), names))
print(initials)
