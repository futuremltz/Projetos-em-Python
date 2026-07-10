import time

def corrigir_valor(senha: str) -> bool:
  if len(senha.strip()):
    return True
  else:
    return False

def tem_tamanho_minimo(senha: str) -> bool:
  return len(senha) >= 8

def tem_maiuscula(senha: str) -> bool:
  for caractere in senha:
    if caractere.isupper():
      return True
  return False

def tem_numero(senha: str) -> bool:
  for caractere in senha:
    if caractere.isdigit():
      return True
  return False

def tem_simbolo(senha: str) -> bool:
  for caractere in senha:
    if not caractere.isalnum() and not caractere.isspace():
      return True
  return False

def iniciar_validador():
  tentativas_ruins = 0

  while True:
    if tentativas_ruins >= 3:
      print("\n[!] SISTEMA BLOQUEADO: 3 tentativas de senhas fracas.")
      print("Aguarde 5 segundos para tentar novamente...")
      time.sleep(5)
      tentativas_ruins = 0
    
    senha_digitada = input("Digite sua senha: ")
    senha_limpa = senha_digitada.strip()
    
    if not corrigir_valor(senha_limpa):
      print("Erro: A senha não pode ser vazia ou conter apenas espaços!")
      continue

    print("\nAnalisando segurança da senha...")
    pontos = 0

    if tem_tamanho_minimo(senha_limpa):
      pontos += 1
    else:
      print("Falta: Ter no mínimo 8 caracteres.")

    if tem_maiuscula(senha_limpa):
      pontos += 1
    else:
      print("Falta: Precisa ter pelo menos uma letra maiuscula.")
    
    if tem_numero(senha_limpa):
      pontos += 1
    else:
      print("Falta: Precisa ter pelo menos um numero.")
    
    if tem_simbolo(senha_limpa):
      pontos += 1
    else:
      print("Falta: Precisa ter no minimo um simbolo especial.")

    if pontos <= 1:
      print("Força da Senha: FRACA [##--------]")
      tentativas_ruins += 1
    elif pontos == 2 or pontos == 3:
      print("Força da Senha: MÉDIA [######----]")
      tentativas_ruins = 0
      print("Senha aceita, mas poderia ser melhor!")
      break
    else:
      print("Força da Senha: FORTE [##########]")
      print("Senha excelente! Cadastro aprovado.")
      break

iniciar_validador()