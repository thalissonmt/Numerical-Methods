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
		fn = dado[5]
		passos = int(dado[4])
		h = float(dado[3])
		t0 = float(dado[2])
		y0 = float(dado[1])
		euler(y0, t0, h, passos, fn, true)
	elif dado[0]=="euler_inverso":
		fn = dado[5]
		passos = int(dado[4])
		h = float(dado[3])
		t0 = float(dado[2])
		y0 = float(dado[1])
		euler_inverso(y0, t0, h, passos, fn, true)
	elif dado[0]=="euler_aprimorado":
		fn = dado[5]
		passos = int(dado[4])
		h = float(dado[3])
		t0 = float(dado[2])
		y0 = float(dado[1])
		euler_aprimorado(y0, t0, h, passos, fn, true)
	elif dado[0]=="runge_kutta":
		fn = dado[5]
		passos = int(dado[4])
		h = float(dado[3])
		t0 = float(dado[2])
		y0 = float(dado[1])
		runge_kutta(y0, t0, h, passos, fn, true)

	elif dado[0]=="adam_bashforth":
		fn = dado[-2]
		passos = int(dado[-3])
		h = float(dado[-4])
		t0 = float(dado[-5])
		y0 = float(dado[1])
		gerarSaida("Adam Bashforth", t0, y0, h)

		if dado[-1]=='2': 
			y1 = float(dado[2])
			adam_bashforth_2(y0, y1, t0, h, passos, fn, true)
		elif dado[-1]=='3':
			y1 = float(dado[2])
			y2 = float(dado[3])
			adam_bashforth_3(y0, y1, y2, t0, h, passos, fn, true)
		elif dado[-1]=='4':
			y1 = float(dado[2])
			y2 = float(dado[3])
			y3 = float(dado[4])
			adam_bashforth_4(y0, y1, y2, y3, t0, h, passos, fn, true)
		elif dado[-1]=='5':
			y1 = float(dado[2])
			y2 = float(dado[3])
			y3 = float(dado[4])
			y4 = float(dado[5])
			adam_bashforth_5(y0, y1, y2, y3, y4, t0, h, passos, fn, true)
		elif dado[-1]=='6':
			y1 = float(dado[2])
			y2 = float(dado[3])
			y3 = float(dado[4])
			y4 = float(dado[5])
			y5 = float(dado[6])
			adam_bashforth_6(y0, y1, y2, y3, y4, y5, t0, h, passos, fn, true)
		elif dado[-1]=='7':
			y1 = float(dado[2])
			y2 = float(dado[3])
			y3 = float(dado[4])
			y4 = float(dado[5])
			y5 = float(dado[6])
			y6 = float(dado[7])
			adam_bashforth_7(y0, y1, y2, y3, y4, y5, y6, t0, h, passos, fn, true)
		elif dado[-1]=='8':
			y1 = float(dado[2])
			y2 = float(dado[3])
			y3 = float(dado[4])
			y4 = float(dado[5])
			y5 = float(dado[6])
			y6 = float(dado[7])
			y7 = float(dado[8])
			adam_bashforth_8(y0, y1, y2, y3, y4, y5, y6, y7, t0, h, passos, fn, true)

	elif dado[0]=="adam_bashforth_by_euler":
		fn = dado[-2]
		passos = int(dado[-3])
		h = float(dado[-4])
		t0 = float(dado[-5])
		y0 = float(dado[1])
		gerarSaida("Adam Bashforth por Euler", t0, y0, h)

		if dado[-1]=='2':
			y1 = euler(y0, t0, h, 1, fn, false)
			adam_bashforth_2(y0, y1, t0, h, passos, fn, true)	
		elif dado[-1]=='3':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			adam_bashforth_3(y0, y1, y2, t0, h, passos, fn, true)	
		elif dado[-1]=='4':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			y3 = euler(y0, t0, h, 3, fn, false)
			adam_bashforth_4(y0, y1, y2, y3, t0, h, passos, fn, true)	
		elif dado[-1]=='5':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			y3 = euler(y0, t0, h, 3, fn, false)
			y4 = euler(y0, t0, h, 4, fn, false)
			adam_bashforth_5(y0, y1, y2, y3, y4, t0, h, passos, fn, true)	
		elif dado[-1]=='6':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			y3 = euler(y0, t0, h, 3, fn, false)
			y4 = euler(y0, t0, h, 4, fn, false)
			y5 = euler(y0, t0, h, 5, fn, false)
			adam_bashforth_6(y0, y1, y2, y3, y4, y5, t0, h, passos, fn, true)	
		elif dado[-1]=='7':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			y3 = euler(y0, t0, h, 3, fn, false)
			y4 = euler(y0, t0, h, 4, fn, false)
			y5 = euler(y0, t0, h, 5, fn, false)
			y6 = euler(y0, t0, h, 6, fn, false)
			adam_bashforth_7(y0, y1, y2, y3, y4, y5, y6, t0, h, passos, fn, true)	
		elif dado[-1]=='8':
			y1 = euler(y0, t0, h, 1, fn, false)
			y2 = euler(y0, t0, h, 2, fn, false)
			y3 = euler(y0, t0, h, 3, fn, false)
			y4 = euler(y0, t0, h, 4, fn, false)
			y5 = euler(y0, t0, h, 5, fn, false)
			y6 = euler(y0, t0, h, 6, fn, false)
			y7 = euler(y0, t0, h, 7, fn, false)
			adam_bashforth_8(y0, y1, y2, y3, y4, y5, y6, y7, t0, h, passos, fn, true)	

	elif dado[0]=="adam_bashforth_by_euler_inverso":
		fn = dado[-2]
		passos = int(dado[-3])
		h = float(dado[-4])
		t0 = float(dado[-5])
		y0 = float(dado[1])
		gerarSaida("Adam Bashforth por Euler Inverso", t0, y0, h)
		
		if dado[-1]=='2':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			adam_bashforth_2(y0, y1, t0, h, passos, fn, true)	
		elif dado[-1]=='3':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			adam_bashforth_3(y0, y1, y2, t0, h, passos, fn, true)	
		elif dado[-1]=='4':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			y3 = euler_inverso(y0, t0, h, 3, fn, false)
			adam_bashforth_4(y0, y1, y2, y3, t0, h, passos, fn, true)	
		elif dado[-1]=='5':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			y3 = euler_inverso(y0, t0, h, 3, fn, false)
			y4 = euler_inverso(y0, t0, h, 4, fn, false)
			adam_bashforth_5(y0, y1, y2, y3, y4, t0, h, passos, fn, true)	
		elif dado[-1]=='6':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			y3 = euler_inverso(y0, t0, h, 3, fn, false)
			y4 = euler_inverso(y0, t0, h, 4, fn, false)
			y5 = euler_inverso(y0, t0, h, 5, fn, false)
			adam_bashforth_6(y0, y1, y2, y3, y4, y5, t0, h, passos, fn, true)	
		elif dado[-1]=='7':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			y3 = euler_inverso(y0, t0, h, 3, fn, false)
			y4 = euler_inverso(y0, t0, h, 4, fn, false)
			y5 = euler_inverso(y0, t0, h, 5, fn, false)
			y6 = euler_inverso(y0, t0, h, 6, fn, false)
			adam_bashforth_7(y0, y1, y2, y3, y4, y5, y6, t0, h, passos, fn, true)	
		elif dado[-1]=='8':
			y1 = euler_inverso(y0, t0, h, 1, fn, false)
			y2 = euler_inverso(y0, t0, h, 2, fn, false)
			y3 = euler_inverso(y0, t0, h, 3, fn, false)
			y4 = euler_inverso(y0, t0, h, 4, fn, false)
			y5 = euler_inverso(y0, t0, h, 5, fn, false)
			y6 = euler_inverso(y0, t0, h, 6, fn, false)
			y7 = euler_inverso(y0, t0, h, 7, fn, false)
			adam_bashforth_8(y0, y1, y2, y3, y4, y5, y6, y7, t0, h, passos, fn, true)	
	
	elif dado[0]=="adam_bashforth_by_euler_aprimorado":
		fn = dado[-2]
		passos = int(dado[-3])
		h = float(dado[-4])
		t0 = float(dado[-5])
		y0 = float(dado[1])
		gerarSaida("Adam Bashforth por Euler Aprimorado", t0, y0, h)
		
		if dado[-1]=='2':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			adam_bashforth_2(y0, y1, t0, h, passos, fn, true)	
		elif dado[-1]=='3':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			adam_bashforth_3(y0, y1, y2, t0, h, passos, fn, true)	
		elif dado[-1]=='4':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			y3 = euler_aprimorado(y0, t0, h, 3, fn, false)
			adam_bashforth_4(y0, y1, y2, y3, t0, h, passos, fn, true)	
		elif dado[-1]=='5':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			y3 = euler_aprimorado(y0, t0, h, 3, fn, false)
			y4 = euler_aprimorado(y0, t0, h, 4, fn, false)
			adam_bashforth_5(y0, y1, y2, y3, y4, t0, h, passos, fn, true)	
		elif dado[-1]=='6':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			y3 = euler_aprimorado(y0, t0, h, 3, fn, false)
			y4 = euler_aprimorado(y0, t0, h, 4, fn, false)
			y5 = euler_aprimorado(y0, t0, h, 5, fn, false)
			adam_bashforth_6(y0, y1, y2, y3, y4, y5, t0, h, passos, fn, true)	
		elif dado[-1]=='7':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			y3 = euler_aprimorado(y0, t0, h, 3, fn, false)
			y4 = euler_aprimorado(y0, t0, h, 4, fn, false)
			y5 = euler_aprimorado(y0, t0, h, 5, fn, false)
			y6 = euler_aprimorado(y0, t0, h, 6, fn, false)
			adam_bashforth_7(y0, y1, y2, y3, y4, y5, y6, t0, h, passos, fn, true)	
		elif dado[-1]=='8':
			y1 = euler_aprimorado(y0, t0, h, 1, fn, false)
			y2 = euler_aprimorado(y0, t0, h, 2, fn, false)
			y3 = euler_aprimorado(y0, t0, h, 3, fn, false)
			y4 = euler_aprimorado(y0, t0, h, 4, fn, false)
			y5 = euler_aprimorado(y0, t0, h, 5, fn, false)
			y6 = euler_aprimorado(y0, t0, h, 6, fn, false)
			y7 = euler_aprimorado(y0, t0, h, 7, fn, false)
			adam_bashforth_8(y0, y1, y2, y3, y4, y5, y6, y7, t0, h, passos, fn, true)	
	
	elif dado[0]=="adam_bashforth_by_runge_kutta":
		fn = dado[-2]
		passos = int(dado[-3])
		h = float(dado[-4])
		t0 = float(dado[-5])
		y0 = float(dado[1])
		gerarSaida("Adam Bashforth por Runge-Kutta", t0, y0, h)
		
		if dado[-1]=='2':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			adam_bashforth_2(y0, y1, t0, h, passos, fn, true)	
		elif dado[-1]=='3':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			adam_bashforth_3(y0, y1, y2, t0, h, passos, fn, true)	
		elif dado[-1]=='4':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			y3 = runge_kutta(y0, t0, h, 3, fn, false)
			adam_bashforth_4(y0, y1, y2, y3, t0, h, passos, fn, true)	
		elif dado[-1]=='5':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			y3 = runge_kutta(y0, t0, h, 3, fn, false)
			y4 = runge_kutta(y0, t0, h, 4, fn, false)
			adam_bashforth_5(y0, y1, y2, y3, y4, t0, h, passos, fn, true)	
		elif dado[-1]=='6':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			y3 = runge_kutta(y0, t0, h, 3, fn, false)
			y4 = runge_kutta(y0, t0, h, 4, fn, false)
			y5 = runge_kutta(y0, t0, h, 5, fn, false)
			adam_bashforth_6(y0, y1, y2, y3, y4, y5, t0, h, passos, fn, true)	
		elif dado[-1]=='7':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			y3 = runge_kutta(y0, t0, h, 3, fn, false)
			y4 = runge_kutta(y0, t0, h, 4, fn, false)
			y5 = runge_kutta(y0, t0, h, 5, fn, false)
			y6 = runge_kutta(y0, t0, h, 6, fn, false)
			adam_bashforth_7(y0, y1, y2, y3, y4, y5, y6, t0, h, passos, fn, true)	
		elif dado[-1]=='8':
			y1 = runge_kutta(y0, t0, h, 1, fn, false)
			y2 = runge_kutta(y0, t0, h, 2, fn, false)
			y3 = runge_kutta(y0, t0, h, 3, fn, false)
			y4 = runge_kutta(y0, t0, h, 4, fn, false)
			y5 = runge_kutta(y0, t0, h, 5, fn, false)
			y6 = runge_kutta(y0, t0, h, 6, fn, false)
			y7 = runge_kutta(y0, t0, h, 7, fn, false)
			adam_bashforth_8(y0, y1, y2, y3, y4, y5, y6, y7, t0, h, passos, fn, true)

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
	arqSaida.write('y( '+str(t0)+' ) = '+str(y0))
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
	count = 0
	if flag==true:
		gerarSaida("Euler", t0, y0, h)
		adicionarSaida(count, y0)
	for count in range(passos):
		yn = y0 + h*func(y0, t0)
		y0 = yn
		t0 += h
		if flag==true:
			adicionarSaida(count+1, yn) 
	if flag==true:
		adicionarBarraN()
	return yn

def euler_inverso(y0,t0,h,passos,fn, flag):
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	if flag==true:
		gerarSaida("Euler Inverso", t0, y0, h)
		adicionarSaida(0, y0)
	for count in range(passos):
		yn = y0 + h*func(euler(y0, t0, h, 1, fn, false), t0+h)
		y0 = yn
		t0 += h
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def euler_aprimorado(y0,t0,h,passos,fn, flag):
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	if flag==true:
		gerarSaida("Euler Aprimorado", t0, y0, h)
		adicionarSaida(0, y0)
	for count in range(passos):
		yn = y0 + h*(func(euler(y0, t0, h, 1, fn, false), t0+h)+func(y0, t0))/2
		y0 = yn
		t0 += h
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def runge_kutta(y0,t0,h,passos,fn,flag):
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	if flag==true:
		gerarSaida("Runge-Kutta", t0, y0, h)
		adicionarSaida(0, y0)
	for count in range(passos):
		k1 = func(y0, t0)
		k2 = func(y0 + (k1*h/2.0), t0 + (h/2.0))
		k3 = func(y0 + (k2*h/2.0), t0 + (h/2.0))
		k4 = func(y0 + k3*h, t0+h)
		yn = y0 + (h*(k1 + (2.0*k2) + (2.0*k3) + k4)/6.0)
		y0 = yn
		t0 += h
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_2(y0,y1,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(1, passos):
		yn = y1 + h*(((3/2)*func(y1,t0 + h*(count))) - ((1/2)*func(y0,t0 + h*(count-1))))
		y0 = y1
		y1 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_3(y0,y1,y2,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(2, passos):
		yn = y2 + h*(((23/12)*func(y2,t0 + h*(count))) - ((4/3)*func(y1,t0 + h*(count-1))) + ((5/12)*func(y0,t0 + h*(count-2))))
		y0 = y1
		y1 = y2
		y2 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_4(y0,y1,y2,y3,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
		adicionarSaida(3,y3)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(3, passos):
		yn = y3 + h*(((55/24)*func(y3,t0 + h*(count))) - ((59/24)*func(y2,t0 + h*(count-1))) + ((37/24)*func(y1,t0 + h*(count-2))) - ((3/8)*func(y0,t0 + h*(count-3))))
		y0 = y1
		y1 = y2
		y2 = y3
		y3 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_5(y0,y1,y2,y3,y4,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
		adicionarSaida(3,y3)
		adicionarSaida(4,y4)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(4, passos):
		yn = y4 + h*(((1901/720)*func(y4,t0 + h*(count))) - ((1387/360)*func(y3,t0 + h*(count-1))) + ((109/30)*func(y2,t0 + h*(count-2))) - ((637/360)*func(y1,t0 + h*(count-3))) + ((251/720)*func(y0,t0 + h*(count-4))))
		y0 = y1
		y1 = y2
		y2 = y3
		y3 = y4
		y4 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_6(y0,y1,y2,y3,y4,y5,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
		adicionarSaida(3,y3)
		adicionarSaida(4,y4)
		adicionarSaida(5,y5)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(5, passos):
		yn = y5 + h*(((4277/1440)*func(y5,t0 + h*(count))) - ((2641/480)*func(y4,t0 + h*(count-1))) + ((4991/720)*func(y3,t0 + h*(count-2))) - ((3649/720)*func(y2,t0 + h*(count-3))) + ((959/480)*func(y1,t0 + h*(count-4))) - ((95/288)*func(y0,t0 + h*(count-5))))
		y0 = y1
		y1 = y2
		y2 = y3
		y3 = y4
		y4 = y5
		y5 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_7(y0,y1,y2,y3,y4,y5,y6,t0,h,passos,fn,flag):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
		adicionarSaida(3,y3)
		adicionarSaida(4,y4)
		adicionarSaida(5,y5)
		adicionarSaida(6,y6)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(6, passos):
		yn = y6 + h*(((198721/60480)*func(y6,t0 + h*(count))) - ((18637/2520)*func(y5,t0 + h*(count-1))) + ((235183/20160)*func(y4,t0 + h*(count-2))) - ((10754/945)*func(y3,t0 + h*(count-3))) + ((135713/20160)*func(y2,t0 + h*(count-4))) - ((5603/2520)*func(y1,t0 + h*(count-5))) + ((19087/60480)*func(y0,t0 + h*(count-6))))
		y0 = y1
		y1 = y2
		y2 = y3
		y3 = y4
		y4 = y5
		y5 = y6
		y6 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

def adam_bashforth_8(y0,y1,y2,y3,y4,y5,y6,y7,t0,h,passos,fn):
	if flag==true:
		adicionarSaida(0,y0)
		adicionarSaida(1,y1)
		adicionarSaida(2,y2)
		adicionarSaida(3,y3)
		adicionarSaida(4,y4)
		adicionarSaida(5,y5)
		adicionarSaida(6,y6)
		adicionarSaida(7,y7)
	y, t = symbols("y t")
	func = lambdify([y, t], fn)
	for count in range(7, passos):
		yn = y7 + h*(((16083/4480)*func(y7,t0 + h*(count))) - ((1152169/120960)*func(y6,t0 + h*(count-1))) + ((242653/13440)*func(y5,t0 + h*(count-2))) - ((296053/13440)*func(y4,t0 + h*(count-3))) + ((2102243/120960)*func(y3,t0 + h*(count-4))) - ((115747/13440)*func(y2,t0 + h*(count-5))) + ((32863/13440)*func(y1,t0 + h*(count-6))) - ((5357/17280)*func(y0,t0 + h*(count-7))))
		y0 = y1
		y1 = y2
		y2 = y3
		y3 = y4
		y4 = y5
		y5 = y6
		y6 = y7
		y7 = yn
		if flag==true:
			adicionarSaida(count+1, yn)
	if flag==true:
		adicionarBarraN()
	return yn

arqSaida = open('saida.txt', 'w')
receberEntrada()
arqSaida.close()