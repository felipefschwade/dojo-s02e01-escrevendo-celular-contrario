#definindo as referências
referencias = {
	'1': '1',
	'ABC2': '2',
	'DEF3': '3',
	'GHI4': '4',
	'JKL5': '5',
	'MNO6': '6',
	'PQRS7': '7',
	'TUV8': '8',
	'WXYZ9': '9',
	' 0': '0',
	'*': '*',
	'#': '#'
}
#Implementando a função de tradução
def traduz(letras):
	#Se não tiver letras da um erro
	if not letras:
		raise ValueError('Vazio')
	#Todas em maiusculo
	letras = letras.upper()
	#Adiciona a letra à lista para cada letra valida
	lista = list((map(adicionaLetraValida, letras)))
	#Transforma a lista em uma String
	resposta = ''.join(lista)
	return resposta

def adicionaLetraValida(letra):	
	#Veritica que se a letra não é algo fora do indice
	if letra == '-':
		return '-'
	if letra == ' ':
		return ' '
	for key in referencias:
		#Procura a letra dentro da chave do index
			if key.find(letra) != -1:
				#Se existir retorna
				return referencias.get(key)
	raise ValueError()

