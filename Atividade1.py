
def saudacao():
    print("Olá! Bem-vindoà demonstração de funções.")


saudacao()


def cumprimentar(nome):
    print(f"Olá, {nome}! Como você está?")


nome_pessoa = "Alice"
cumprimentar(nome_pessoa)


def calcular_area_retangulo(comprimento, largura):
    area = comprimento * largura
    return area


comprimento_retangulo = 5
largura_retangulo = 3
area_calculada = calcular_area_retangulo(comprimento_retangulo, largura_retangulo)
print(f"A área do retângulo é: {area_calculada} unidades²")