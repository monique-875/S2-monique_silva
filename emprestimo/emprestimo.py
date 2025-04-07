#-- coding:UTF-8 --

print ("oi, nesse programa eu caucularei se você pode fazer um empréstimo de acordo com o seu salário bruto") 

salario_bruto= float(input("me diga o seu salário")) 

prestaçao= float(input("me diga o valor da prestação")) 

cauculo= salario_bruto*0.30 

if prestaçao <= cauculo: 

     print ("voce pode fazer o emprestimo") 

