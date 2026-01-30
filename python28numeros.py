suma=0
n_introducidos=0
n_pares=0
n_impares=0
suma_pares=0
suma_impares=0


n_pedidos=0
while (n_pedidos!=-1): 
    print("INTRODUCE UN NUMERO, PARA ACABABAR INTRODUZCA -1")
    n_pedidos=int(input())
    n_introducidos=n_introducidos+1
    suma=suma+n_pedidos
    if (n_pedidos%2==0):
        suma_pares=suma_pares+n_pedidos
        n_pares=n_pares+1

    
print("SUMA TOTAL", suma)
print("N. INTRODUCIDOS", n_introducidos)
print("N. PARES", n_pares)
print("N. IMPARES", n_impares)
print("SUMA PARES", suma_pares)
print("SUMA IMPARES", suma_impares)





