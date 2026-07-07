def calcular_imc(peso: float, altura: float) -> float:
  imc = peso/(altura ** 2)
  return imc

def faixa(imc: float, idade: int) -> str:

  print(f"Seu IMC é de {imc:.2f}")

  if idade >= 60:
    if imc < 22.0:
      return "\033[31m O seu peso está abaixo do indicado para saude \033[0m"

    elif imc <= 27.0:
      return "\033[32m O seu peso está no peso adequado baseado na sua idade \033[0m"

    else:
      return "\033[31m O seu peso está acima do peso adequado baseado na sua idade \033[0m"
  
  elif idade >= 20 and idade <= 59:
    if imc < 18.5:
      return "\033[31m O seu peso está abaixo do indicado para saude \033[0m"

    elif imc >= 18.5 and imc <= 24.9:
      return "\033[32m O seu peso está no peso adequado baseado na sua idade \033[0m"

    elif imc >= 25.0 and imc <= 29.9:
      return "\033[33m O seu peso está acima do peso adequado baseado na sua idade \033[0m"

    elif imc >= 30.0 and imc <= 34.9:
      return "\033[31m O seu IMC é considerado como obesidade grau I \033[0m"

    elif imc >= 35.0 and imc <= 39.9:
      return "\033[31m O seu IMC é considerado como obesidade grau II \033[0m"

    else:
      return "\033[31m O seu IMC é considerado como obesidade grau III \033[0m"

  else:
    return "Para idade de 0 a 19 não existe uma tabela de valores fixos"
  

menu = True

while menu:
  try:
    nome = input("Por favor digite seu nome: ")
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite sua altura: "))
    idade = int(input("Digite sua idade: "))

    if peso <= 0 or altura <= 0 or idade <= 0:
      print("\033[31mErro: Peso, altura e idade devem ser maiores que zero!\033[0m")
      continue

    imc = calcular_imc(peso, altura)
    resultado = faixa(imc, idade)
    print(resultado)

    salvar = input("\nDeseja salvar este resultado no historico? (s/n): ").strip().lower()
    if salvar == 's':
      with open("historico_imc.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome:{nome} | Idade: {idade} anos | Peso: {peso}Kg | Altura: {altura}m | IMC: {imc:.2f}\n")
      print("\033[32mO resultado foi salvo com sucesso no arquivo 'historico_imc.txt' !\033[0m")

    escolha = input("Deseja colocar outro numero (s/n)").strip().lower()
    if escolha != 's':
      print("Desligando sistema")
      menu = False
    
  except (ValueError, ZeroDivisionError):
    print("\033[31mErro: Por favor, digite apenas números válidos.\033[0m")