from sympy import *

def receberEntrada():
    arqEntrada = open('entrada.txt', 'r')
    texto = arqEntrada.readlines()
    for cur in texto:
        interpretarEntrada(cur)
    arqEntrada.close()

def interpretarEntrada(linha):
    dado = linha.split()
    if dado[0]=="euler":
        euler(float(dado[1]),float(dado[2]),float(dado[3]),int(dado[4]),dado[5],true)
    elif dado[0]=="euler_inverso":
     	euler_inverso(float(dado[1]),float(dado[2]),float(dado[3]),int(dado[4]),dado[5],true)
    elif dado[0]=="euler_aprimorado":
    	euler_aprimorado(float(dado[1]),float(dado[2]),float(dado[3]),int(dado[4]),dado[5],true)
    # elif dado[0]=="runge_kutta":

    # elif dado[0]=="adam_bashforth":
    
    # elif dado[0]=="adam_bashforth_by_euler":
    
    # elif dado[0]=="adam_bashforth_by_euler_inverso":
    
    # elif dado[0]=="adam_bashforth_by_euler_aprimorado":
    
    # elif dado[0]=="adam_bashforth_by_runge_kutta":
    
    # elif dado[0]=="adam_multon":
    
    # elif dado[0]=="adam_multon_by_euler":
    
    # elif dado[0]=="adam_multon_by_euler_inverso":
    
    # elif dado[0]=="adam_multon_by_euler_aprimorado":
    
    # elif dado[0]=="adam_multon_by_runge_kutta":
    
    # elif dado[0]=="formula_inversa":
    
    # elif dado[0]=="formula_inversa_by_euler":
    
    # elif dado[0]=="formula_inversa_by_euler_inverso":
    
    # elif dado[0]=="formula_inversa_by_euler_aprimorado":
    
    # elif dado[0]=="formula_inversa_by_runge_kutta":

def gerarSaida(nome, t0, y0, h):
    arqSaida.write("Metodo de "+nome)
    adicionarBarraN()
    arqSaida.write('y('+str(t0)+') = '+str(y0))
    adicionarBarraN()
    arqSaida.write('h = '+str(h))
    adicionarBarraN()

def adicionarSaida(count, yn):
    arqSaida.write(str(count)+' '+str(yn))
    adicionarBarraN()

def adicionarBarraN():
    arqSaida.write('\n')

def euler(y0,t0,h,passos,fn, flag):
    y, t = symbols("y t")
    func = lambdify([y, t], fn)
    yn = y0
    count = 0
    if flag==true:
    	gerarSaida("Euler", t0, y0, h)
    	adicionarSaida(count, y0)
    while count <  passos:
        yn = yn + h*func(yn, t0 + h*count)
        if flag==true:
        	adicionarSaida(count+1, yn)
        count += 1 
    if flag==true:
    	adicionarBarraN()
    return yn

def euler_inverso(y0,t0,h,passos,fn, flag):
    y, t = symbols("y t")
    func = lambdify([y, t], fn)
    yn = y0
    count = 0
    if flag==true:
    	gerarSaida("Euler Inverso", t0, y0, h)
    	adicionarSaida(count, y0)
    while count <  passos:
        yn = yn + h*func(euler(yn, t0 + h*count, h, 1, fn, false), t0 + h*(count+1))
        if flag==true:
        	adicionarSaida(count+1, yn)
        count += 1 
    if flag==true:
    	adicionarBarraN()

def euler_aprimorado(y0,t0,h,passos,fn, flag):
    y, t = symbols("y t")
    func = lambdify([y, t], fn)
    yn = y0
    count = 0
    if flag==true:
    	gerarSaida("Euler Aprimorado", t0, y0, h)
    	adicionarSaida(count, y0)
    while count <  passos:
        yn = yn + h/2*(func(euler(yn, t0 + h*count, h, 1, fn, false), t0 + h*(count+1))+func(yn, t0 + h*count))
        if flag==true:
        	adicionarSaida(count+1, yn)
        count += 1 
    if flag==true:
    	adicionarBarraN()

arqSaida = open('saida.txt', 'w')
receberEntrada()
arqSaida.close()