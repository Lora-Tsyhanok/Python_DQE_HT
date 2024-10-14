import random
import string

# create a list of random number of dicts (from 2 to 10)
rand_dicts = []
rand_num = random.randint(2, 10)


for i in range(rand_num):
    rand_keys = random.randint(2, 5)
    keys = random.sample(string.ascii_lowercase, rand_keys)
    values = (random.randint(0, 100) for key in keys)
    one_dict = dict(zip(keys, values))
    rand_dicts.append(one_dict)

print(rand_dicts)

# Create dictionary to track maximum values and the dictionary index
temp_dict = {}
key_occur = {}
index = 1

for d in rand_dicts:
    for key, value in d.items():
        if key not in temp_dict or value > temp_dict[key][0]:
            temp_dict[key] = (value, index)
        if key not in key_occur:
            key_occur[key] = 1
        else:
            key_occur[key] += 1
    index += 1

# Create dictionary with renamed keys
common_dict = {}

for key, (value, idx) in temp_dict.items():
    if key_occur[key] > 1:
        new_key = f"{key}_{idx}"
    else:
        new_key = key
    common_dict[new_key] = value

print(common_dict)
