for i in range(16):
    # if sel == 000, get A[i]
    print(f'And(a=notS0, b=notS1, out=andSA{i});')
    print(f'And(a=notS2, b=andSA{i}, out=andSA{i}x);')
    print(f'And(a=a[{i}], b=andSA{i}x, out=outA{i});')

    # if sel == 001, get B[i]
    print(f'And(a=sel[0], b=notS1, out=andSB{i});')
    print(f'And(a=notS2, b=andSB{i}, out=andSB{i}x);')
    print(f'And(a=b[{i}], b=andSB{i}x, out=outB{i});')

    # if sel == 010, get C[i]
    print(f'And(a=notS0, b=sel[1], out=andSC{i});')
    print(f'And(a=notS2, b=andSC{i}, out=andSC{i}x);')
    print(f'And(a=c[{i}], b=andSC{i}x, out=outC{i});')

    # if sel == 011, get D[i]
    print(f'And(a=sel[0], b=sel[1], out=andSD{i});')
    print(f'And(a=notS2, b=andSD{i}, out=andSD{i}x);')
    print(f'And(a=d[{i}], b=andSD{i}x, out=outD{i});')

    # if sel == 100, get E[i]
    print(f'And(a=notS0, b=notS1, out=andSE{i});')
    print(f'And(a=sel[2], b=andSE{i}, out=andSE{i}x);')
    print(f'And(a=e[{i}], b=andSE{i}x, out=outE{i});')

    # if sel == 101, get F[i]
    print(f'And(a=notS0, b=notS1, out=andSF{i});')
    print(f'And(a=sel[2], b=andSF{i}, out=andSF{i}x);')
    print(f'And(a=f[{i}], b=andSF{i}x, out=outF{i});')

    # if sel == 110, get G[i]
    print(f'And(a=notS0, b=notS1, out=andSG{i});')
    print(f'And(a=sel[2], b=andSG{i}, out=andSG{i}x);')
    print(f'And(a=g[{i}], b=andSG{i}x, out=outG{i});')

    # if sel == 111, get H[i]
    print(f'And(a=notS0, b=notS1, out=andSH{i});')
    print(f'And(a=sel[2], b=andSH{i}, out=andSH{i}x);')
    print(f'And(a=h[{i}], b=andSH{i}x, out=outH{i});')

    # or A[i]..D[i] to get out[i] 
    print(f'Or8Way(in[0]=outA{i}, in[1]=outB{i}, in[2]=outC{i}, in[3]=outD{i}, in[4]=outE{i}, in[5]=outF{i}, in[6]=outG{i}, in[7]=outH{i}, out=out[{i}]);')




