#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("\n******************* Python Calculator *******************")

print("\nSelecione o número da operação desejada: \n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão \n")

calc = int(input("Digite sua opção 1/2/3/4 \n"))

if calc == 1 or calc == 2 or calc == 3 or calc == 4: 
   if calc == 1:    
       num1 = int(input("\n Digite primeiro numero: "))
       num2 = int(input("\n Digite segundo numero: "))
       soma = num1 + num2
       print("\n Total: ", soma)
   
   if calc == 2:
       num1 = int(input("\n Digite primeiro numero: "))
       num2 = int(input("\n Digite segundo numero: "))
       soma = num1 - num2
       print("\n Total: ", soma)

   if calc == 3:
       num1 = int(input("\n Digite primeiro numero: "))
       num2 = int(input("\n Digite segundo numero: "))
       soma = num1 * num2
       print("\n Total: ", soma)

   if calc == 4:
       num1 = int(input("\n Digite primeiro numero: "))
       num2 = int(input("\n Digite segundo numero: "))
       soma = num1 / num2
       print("\n Total: ", int(soma))

else:
   print("Opção Invalida")


# In[ ]:





# In[ ]:





# In[ ]:




