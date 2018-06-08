import random, string
def randomword(length):
    s = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.sample(s,length))
print randomword(10)
        

    
        
            

        
       
        
     
     
        
    
