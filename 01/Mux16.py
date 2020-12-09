print('Not(in=sel, out=notSel);')
for i in range(16):
    # Implement mux for every bit in input bus
    print(f'And(a=a[{i}], b=notSel, out=andA{i});')
    print(f'And(a=b[{i}], b=sel, out=andB{i});')
    print(f'Or(a=andA{i}, b=andB{i}, out=out[{i}]);')
