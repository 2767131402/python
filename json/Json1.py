import json

with open("test.json",encoding="utf-8",mode='r') as f:
    f_read = f.read()

# data = json.dumps(f_read)
d = json.loads(f_read)
print(d)
print(type(d))