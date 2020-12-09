for i in range(8):
    print(f'And(a=load, b=load{i}, out=and{i});')
    print(f'Register(in=in, load=and{i}, out=reg{i});')
