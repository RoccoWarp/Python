import os

a = {'my project': [{'settings': []}, {'mainapp': []}, {'adminapp': []}, {'autapp': []}]}
for key, val in a.items():
    if not os.path.exists(key):
        for item in val:
            for k in item.keys():
                os.makedirs(os.path.join(key, k))


