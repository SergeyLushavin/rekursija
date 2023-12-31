#######################################################
#              РАСЧЕТ ЧИСЕЛ ФИБОНАЧЧИ                 #
#              с применением рекурсии                 #
#######################################################

def fibonachi(n1,n2,N,i,fbnch):
# Расчет чисел Фибоначчи
# n1, n2 - предыдущие два числа, начальные значения 0 и 1.
# N - количество итераций
# i - счетчик итераций, начальное значение: 1
# fbnch - числа Фибоначчи (список)    
    n3 = n1 + n2
    if i > 1:
        fbnch.append(str(n3))
    else: 
        fbnch.append(str(n1))
        fbnch.append(str(n2))
        fbnch.append(str(n3))
    n1 = n2
    n2 = n3        
    i = i + 1
    if i > N:		 
        return ",".join(fbnch)
    else: 
        return fibonachi(n1,n2,N,i,fbnch)        
    
N = 20 # количество итераций
fb = [] # список, содержащий числа Фибоначчи
resultat = fibonachi(0,1,N,1,fb)
print(f"Последовательность Фибоначчи (итераций:{N}):")
print(resultat)
