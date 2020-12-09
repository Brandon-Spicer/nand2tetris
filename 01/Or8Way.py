for i in range(7):
    if i == 0:
        print('Or(a=in[0], b=in[1], out=or1);')
    elif 1 <= i <= 5:
        print(f'Or(a=or{i}, b=in[{i+1}], out=or{i+1});')
    else:
        print(f'Or(a=or{i}, b=in[{i+1}], out=out);')
