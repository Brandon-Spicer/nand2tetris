for i in range(8):
    print(f'And(a=dmux{i}, b=load, out=and{i});')
    print(f'RAM8(in=in, load=and{i}, address=address[0..2], out=ram{i});')

