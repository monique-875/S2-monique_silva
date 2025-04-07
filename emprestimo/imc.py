#-- coding:UTF-8 --
print("usuario me forneça algumas informações e direi se está em um peso favorável, de acordo com o IMC.") 
peso=float(input("peso:")) 
altura=float(input("altura:")) 
imc=peso/(altura*altura) 
if imc <20: 
    print ("você está abaixo do peso!") 
else: 
    if imc==20 or imc<25: 
        print("você está no peso normal!") 
    else: 
        if imc==25 or imc<30: 
            print ("você está sobre peso!") 


