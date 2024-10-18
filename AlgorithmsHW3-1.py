#Problem 1 part a with memoization

#????????




#%%
#Problem 1 part b:

def step(n):
        if n==0:
            return 1
        elif n==1:
            return 1
        else:
            return (step(n-2)+step(n-1))
    
            
print (step(7))

        
        
    
    
