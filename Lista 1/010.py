n = int(input("Informe um número: "))
cont = 0
i = 1

if n == 2:
    print("Dois é primo!")

else:
    if(n % 2 == 0):
        print("{} não é primo!".format(n))

    else:
        while i <= n:
            if (n % i == 0):
                cont = cont + 1
        
            i = i + 2

        if cont == 2:
            print("{} é primo!".format(n))
        else:
            print("{} não é primo!".format(n))
    

    
    
