a = {'scale': 3.6, 'speed':[0., 15., 22., 30.,], 'label': "Scaled speed"}

for i in range(0,4):
    x = a["speed"][i]*a["scale"]
    print(a["label"], x)
