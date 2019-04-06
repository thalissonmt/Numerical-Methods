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
        euler(float(dado[1]),float(dado[2]),float(dado[3]),int(dado[4]),dado[5])
    # elif dado[0]=="euler_inverso":
     
    # elif dado[0]=="euler_aprimorado":

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

def euler(y0,t0,h,passos,fn):
    gerarSaida("Euler", t0, y0, h)
    y, t = symbols("y t")
    fn = lambdify([y, t], fn)
    yn = y0
    count = 0
    adicionarSaida(count, y0)
    while count <  passos:
        yn = yn + h*fn(yn, t0 + h*count)
        adicionarSaida(count+1, yn)
        count += 1 

arqSaida = open('saida.txt', 'w')
receberEntrada()
arqSaida.close()