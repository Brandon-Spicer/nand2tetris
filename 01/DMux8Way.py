print('Not(in=sel[0], out=notS0);')
print('Not(in=sel[1], out=notS1);')
print('Not(in=sel[2], out=notS2);')

outs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i, out in enumerate(outs):
    # DEC -> BIN to get inputs to And gates
    S0 = 'sel[0]' if i % 2 else 'notS0'
    S1 = 'sel[1]' if (i // 2) % 2 else 'notS1'
    S2 = 'sel[2]' if (i // 4) % 2 else 'notS2'

    # And(S0, S1, S2, in)
    print(f'And(a={S0}, b={S1}, out=inner{i}0);')
    print(f'And(a=inner{i}0, b={S2}, out=inner{i}1);')
    print(f'And(a=inner{i}1, b=in, out={out});')


    
