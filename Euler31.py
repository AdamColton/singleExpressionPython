print (lambda a,c,f:f(a,c,f))(200,[200,100,50,20,10,5,2,1],lambda a,c,f:((a==0 or len(c)<=1) or sum((f(a-i*c[0],c[1:],f) for i in range(0,1+a/c[0]))),(a==0) or (a%c[0]==0))[a==0 or len(c)<=1])