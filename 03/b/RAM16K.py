for i in range(8):
    print(f'And(a=dmux{i}, b=load, out=and{i});')
    print(f'RAM4K(in=in, load=and{i}, address=address[0..11], out=ram{i});')

