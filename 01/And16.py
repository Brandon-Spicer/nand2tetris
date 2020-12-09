with open('And16.txt', 'w') as f:
    for i in range(16):
        f.write(f'And(a=a[{i}], b=b[{i}], out=out[{i}]);\n')
