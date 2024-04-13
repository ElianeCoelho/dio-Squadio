#1/3
valor = float(input())

if valor > 0:
  print(f"Deposito realizado com sucesso!")
  print(f"Saldo atual: R$ {valor:.2f}")
elif valor < 0:
  print("Valor invalido! Digite um valor maior que zero.")
else:
  print("Encerrando o programa...")


#2/3
ativos = []

quantidadeAtivos = int(input())

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos_ordenados = sorted(ativos)

for ativo in ativos_ordenados:
    print(ativo)

#3 / 3 - Validando a Força de Senhas no IAM
import re

def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = bool(re.search(r'[A-Z]', senha))
    tem_letra_minuscula = bool(re.search(r'[a-z]', senha))
    tem_numero = bool(re.search(r'[0-9]', senha))
    tem_caractere_especial = bool(re.search(r'[!@#$%^&*()-+=]', senha))

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letras maiúsculas e minúsculas
    if not tem_letra_maiuscula:
        return "Sua senha deve conter pelo menos uma letra maiuscula."
    if not tem_letra_minuscula:
        return "Sua senha deve conter pelo menos uma letra minuscula."

    # Verificando se a senha contém números
    if not tem_numero:
        return "Sua senha deve conter pelo menos um numero."

    # Verificando se a senha contém caracteres especiais
    if not tem_caractere_especial:
        return "Sua senha nao atende aos requisitos de seguranca."

    return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)


