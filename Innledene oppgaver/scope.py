def minFunksjon(): 
    for x in range(2):  
        c = 2  
        print(c) 
        c += 1 
        b = 10 
        b += c  
        print(b) 
        return(b) 

 #Først lager vi variabel c med verdi 2 og b med verdi 10. Vi tar c og 
 #plusser på 1 må er den 3.
 #også plsuuer vi c til b og den blir 13.
 #vi returnerer 13.




def hovedprogram():  

    a = 42 
    b = 0  
    print(b)  
    
    b = a 
    a = minFunksjon()  

    print (b) 
    print (a)  
# vi lager variabel a og b. A er verdi 42 og b er verdi 0.
# Vi gir verdi b veriden a som er 42 nå er b 42. og vi gjør a om til min funksjon som 
# returnere 13. b er 42 a er 13.
     

hovedprogram() 