# Prova Algoritmos e Variáveis
# Aluno: Hugo Alves Veras
# Curso: Data Science
# ----------------------------------------------------------------------------------------------------
# Programa para calcular a área de um retângulo
# ----------------------------------------------------------------------------------------------------
# Saudação inicial, informando o motivo da solicitação dos dados.
print('Se você me informar os valores da base e da altura, posso te ajudar a calcular a área!\n')

# Input dos dados pelo usuario para serem calculados:
base = float(input('Qual a base do Retângulo? '))
altura = float(input('Qual a altura do Retângula? '))

# Variavel onde é feito o calculo dos valores informados:
area_retangulo = base * altura

# Retorno em formato F-String:
print(f'Com base nas informações de base e altura do retangulo, sua área é de {area_retangulo:.2f}')