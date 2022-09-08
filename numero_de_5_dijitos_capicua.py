# quiz. leer un numero entero de 5 dijitos y determine si es capicua




print("-------------------------------")
print("--numero capicua de 5 dijitos--")
print("-------------------------------")

#input
n =(input("dijite el numero de 5 dijitos:"))
n=int(n)


#processing
if n >= 10000  and  n <= 99999:
    n5 =  n  %  10
    n4 = ( n  %  100 ) //  10
    n3 = ( n  %  1000 ) //  100
    n2 = ( n % 10000 ) //  1000
    n1 =  n // 10000

    if n1 == n5  and  n2 == n4 :
        print( "El numero" , n , "es capicua" )
    else :
        print("El numero" , n , "no es capicua" )

else:
    print ( "El numero" , n , "no es de 5 digitos" )
    

    

