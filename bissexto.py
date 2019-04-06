#define se o ano é bissexto ou não

def bissexto(ano):
    if(ano % 4 == 0):
        if(ano % 100 != 0):
            return True
        
        else:
            if(ano % 400 != 0):
                return False
            
            else:
                return True
    
    else:
        return False
                

ano = int(input())
print(bissexto(ano))
