x = {'perro':2, 'gato':1}

print({k: v for k, v in sorted(x.items(), key=lambda item: item[1])})