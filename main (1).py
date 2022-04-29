def fangshe(p,k1,k2):
	c=""
	for i in range(len(p)):
		temp=chr((((ord(p[i])-ord('a'))*k1+k2)%26)+ord('a'))
		c+=temp
	return c

def gcd(x,y):
	if x>y:
		temp=y
	else:
		temp=x
	for i in range(1,temp+1):
		if((x%i==0) and (y%i==0)):
			s=i
	return s

def decode(a,b,str1):
	c1=""
	if(gcd(a,26)==1):
		for i in range(26):
			if((a*i)%26==1):
				k1_re=i
				break
		for i in range(len(str1)):
			temp=chr((((ord(str1[i])-ord('a'))-b)*k1_re)%26+ord('a'))
			c1+=temp
		return c1
    
def main():
	print 8*"*"+" EncryptInput "+8*"*"
	p=raw_input("Please enter the plain:")
	k1=input("Please enter k1:")
	k2=input("Please enter k2:")
	print 8*"*"+" Encryption "+8*"*"
	c=fangshe(p,k1,k2)
	print ("Cipher:"+c)
	print "\n"+8*"*"+" DecryptInput "+8*"*"
	C=raw_input("Please enter the Cipher:")
	key1=input("Please enter k1:")
	key2=input("Please enter k2:")
	print 8*"*"+" Decryption "+8*"*"
	plain=decode(key1,key2,C)
	print "Plain:"+plain
    
if __name__ == '__main__':
	main()