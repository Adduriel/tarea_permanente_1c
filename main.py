def find_mod_inv(a,m):

    for x in range(1,m):
        if((a%m)*(x%m) % m==1):
            return x
    raise Exception('No existe el inverso modular.')

a = 13
m = 22

try:
    res=find_mod_inv(a,m)
    print("El inverso modular es: "+ str(res))

except:
    print('No existe el inverso modular')