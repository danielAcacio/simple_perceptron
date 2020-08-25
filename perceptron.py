class Perceptron():
	pesos=[]

	def __init__(self, pesos=[]):
		self.pesos=pesos
	
	def inicializarPesos(self, entradas):
		if(len(entradas)>0 and (len(self.pesos)!=len(entradas)) ):
			for i in entradas:
				self.pesos.append(0)

	
	def calcularSoma(self,entradas):
		soma = 0
		for i in range(0, len(entradas)):
			soma+=self.pesos[i]*entradas[i]
		return soma
	#step funtion
	def calcularResultante(self, soma):
		if(soma<1):
			return 0
		else:
			return 1

	def processarDados(self,dados):
		soma = self.calcularSoma(dados)
		return self.calcularResultante(soma)

	def treinarPerceptron(self, entradas, resultados):
		for i in range(0, len(entradas)):
			while True:
				self.inicializarPesos(entradas[i])
				resultadoCalculado = self.processarDados(entradas[i])
				
				if(resultadoCalculado!=resultados[i]):
					self.ajustarPeso(resultadoCalculado, resultados[i])
				if(resultadoCalculado==resultados[i]):
					break
		

	def ajustarPeso(self, resultadoObtido, resultadoEsperado):
		fatorAjuste = 0.1*(resultadoObtido-resultadoEsperado)
		for i in range(0, len(self.pesos)):
			self.pesos[i]=self.pesos[i]-fatorAjuste
		





p = Perceptron()
p.treinarPerceptron([[0,0],[0,1],[1,0],[1,1]],[0.0,0.0,0.0,1.0])

print(p.processarDados([0,0]))
print(p.processarDados([0,1]))
print(p.processarDados([1,0]))
print(p.processarDados([1,1]))
print(p.pesos)
