import os

historico = []

# Utilitario
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ler_valor(mensagem: str) -> float:
  while True:
    try:
      return float(input(mensagem))
    except ValueError:
      print("\033[31mErro: Por favor, digite apenas números válidos (use ponto para decimais).\033[0m")

def salvar_historico(nome_conversao: str, valor_original: float, resultado: float):
    texto = f"{nome_conversao}: {valor_original} -> {resultado:.4f}"
    historico.append(texto)
    if len(historico) > 3:
        historico.pop(0)

def exibir_historico():
    clear_console()
    print("--- ÚLTIMAS CONVERSÕES ---")
    if not historico:
        print("Nenhuma conversão realizada ainda.")
    else:
        for item in historico:
            print(f"- {item}")
    input("\nPressione ENTER para voltar...")

# Principal
def menu_comprimento():
  clear_console()
  fator_cm = 100
  fator_mm = 1000
  fator_km = 1000
  fator_pol = 39.37
  fator_pes = 3.28

  def m_para_cm(val): return val * fator_cm
  def m_para_mm(val): return val * fator_mm
  def m_para_km(val): return val / fator_km
  def m_para_pol(val): return val * fator_pol
  def m_para_pes(val): return val * fator_pes

  opcoes = {
    "1": ("m para cm", m_para_cm),
    "2": ("m para mm", m_para_mm),
    "3": ("m para km", m_para_km),
    "4": ("m para polegada", m_para_pol),
    "5": ("m para pés", m_para_pes)
  }


  print("--- Menu de Comprimento ---")
  print("1- m para cm\n2- m para mm\n3- m para km\n4- m para polegada\n5- m para pes")
  escolha = input("Escolha a opção: ")
  
  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")
  
  return

def menu_massa():
  clear_console()
  fator_g = 1000
  fator_mg = 1000000
  fator_lb = 2.204
  fator_onca = 35.27
  def kg_para_g(val): return val * fator_g
  def kg_para_mg(val): return val * fator_mg
  def kg_para_lb(val): return val * fator_lb
  def kg_para_onca(val): return val * fator_onca

  opcoes = {
    "1": ("kg para g", kg_para_g),
    "2": ("kg para mg", kg_para_mg),
    "3": ("kg para libra", kg_para_lb),
    "4": ("kg para onça", kg_para_onca)
  }
  print("--- Menu Massa ---")
  print("1- kg para g\n2- kg para mg\n3- kg para libra\n4- kg para onca")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_temperatura():
  clear_console()
  def c_para_f(val): return (val * 9 / 5) + 32
  def c_para_k(val): return val + 273.15
  def f_para_c(val): return (val - 32) * 5/9
  def k_para_c(val): return val - 273.15

  opcoes = {
    "1": ("Celsius para Fahrenheit", c_para_f),
    "2": ("Celsius para Kelvin", c_para_k),
    "3": ("Fahrenheit para Celsius", f_para_c),
    "4": ("Kelvin para Celsius", k_para_c)
  }

  print("--- Menu de Temperatura ---")
  print("1- Celsius para Fahrenheit\n2- Celsius para Kelvin\n3- Fahrenheit para Celsius\n4- Kelvin para Celsius")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.2f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_volume():
  clear_console()
  fator_ml = 1000
  fator_m3 = 1000
  fator_galao = 3.785

  def l_para_ml(val): return val * fator_ml
  def l_para_m3(val): return val/fator_m3
  def l_para_galao(val): return val / fator_galao

  opcoes = {
    "1": ("Litro para Mililitro", l_para_ml),
    "2": ("Litro para M3(metro cubico)", l_para_m3),
    "3": ("Litro para Galao", l_para_galao)
  }

  print("--- Menu de Volume ---")
  print("1- Litro para Mililitro\n2- Litro para M3(metro cubico)\n3- Litro para Galao")
  escolha = input("Digite qual opção deseja: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_medidas_fisicas():
  menu = True
  while menu:
    clear_console()
    print("--- MEDIDAS FÍSICAS ---")
    print("1.Comprimento (m -> Para qual voce deseja)")
    print("2.Massa (kg -> Para qual voce deseja)")
    print("3.Temperatura")
    print("4.Volume (L -> Para qual voce deseja)")
    print("5.Voltar ao menu")
    escolha = input("Digite a opção que deseja: ")
    if escolha == "1": menu_comprimento()
    elif escolha == "2": menu_massa()
    elif escolha == "3": menu_temperatura()
    elif escolha == "4": menu_volume()
    elif escolha == "5":
      menu = False
      print("Voltando ao menu")
      return
    else: 
      print("Digite um valor valido")
      input("\nPressione ENTER para continuar...")

def menu_tempo():
  clear_console()

  opcoes = {
        "1": ("Segundo para Minutos", lambda v: v/60),
        "2": ("Segundos para Hora", lambda v: v/3600),
        "3": ("Minuto para Segundo", lambda v: v*60),
        "4": ("Minuto para Hora", lambda v: v/60),
        "5": ("Hora para segundo", lambda v: v*3600),
        "6": ("Hora para minuto", lambda v: v*60),
        "7": ("Hora para dia", lambda v: v/24),
        "8": ("Dia para Hora", lambda v: v*24)
    }

  print("--- Menu de Tempo ---")
  print("1- Segundo para Minutos\n2- Segundos para Hora\n3- Minuto para Segundo\n" \
  "4- Minuto para Hora\n5- Hora para segundo\n6- Hora para minuto\n7- Hora para dia\n" \
  "8- Dia para Hora\n9- Dia para Semana\n10- Dia para Ano\n11- Semana para Dia\n12- Ano para Dia")
  escolha = input("Digite qual opção deseja: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_dados():
  clear_console()

  FATOR = 1024
  opcoes = {
    "1": ("B para KB", lambda v: v/FATOR),
    "2": ("KB para B", lambda v: v*FATOR),
    "3": ("KB para MB", lambda v: v/FATOR),
    "4": ("MB para KB", lambda v: v*FATOR),
    "5": ("MB para GB", lambda v: v/FATOR),
    "6": ("GB para MB", lambda v: v*FATOR),
    "7": ("GB para TB", lambda v: v/FATOR),
    "8": ("TB para GB", lambda v: v*FATOR)
  }

  print("--- Menu de Dados ---")
  print("1- Byte para Kilobyte\n2- Kilobyte para Byte\n3- Kilobyte para Megabyte\n" \
  "4- Megabyte para Kilobyte\n5- Megabyte para Gigabyte\n6- Gigabyte para Megabyte\n7- Gigabyte para Terabyte\n" \
  "8- Terabyte para Gigabyte")
  escolha = input("Digite qual opção deseja: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_dados_tempo():
  menu = True
  while menu:
    clear_console()
    print("--- MEDIDAS de Tempo e Dados ---")
    print("1.Tempo (minutos, horas, dias, semanas e anos)")
    print("2.Dados (KB, MB, GB e TB)")
    print("3.Voltar ao menu")
    escolha = input("Digite a opção que deseja: ")
    if escolha == "1":menu_tempo()
    elif escolha == "2":menu_dados()
    elif escolha == "3":
      menu = False
      print("Voltando ao menu")
      return
    else: 
      print("Digite um valor valido")
      input("\nPressione ENTER para continuar...")

def menu_area():
  clear_console()
  opcoes = {
    "1": ("m² para cm²", lambda v: v*10000),
    "2": ("m² para km²", lambda v: v/1000000),
    "3": ("m² para hectare", lambda v: v/10000),
    "4": ("m² para acre", lambda v: v/4046.86)
  }
  print("--- Menu da Área ---")
  print("1- m² para cm²\n2- m² para km²\n3- m² para hectare\n4- m² para acre")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_velocidade():
  clear_console()
  FATOR_KMH = 3.6
  FATOR_MPH = 1.60934
  FATOR_NO = 1.852

  def ms_para_kmh(val): return val * FATOR_KMH
  def mph_para_kmh(val): return val * FATOR_MPH
  def no_para_kmh(val): return val * FATOR_NO
  def kmh_para_ms(val): return val / FATOR_KMH
  def kmh_para_mph(val): return val / FATOR_MPH
  def kmh_para_no(val): return val / FATOR_NO

  opcoes = {
    "1": ("m/s para km/h", ms_para_kmh),
    "2": ("mph para km/h", mph_para_kmh),
    "3": ("Nó para km/h", no_para_kmh),
    "4": ("km/h para m/s", kmh_para_ms),
    "5": ("km/h para mph", kmh_para_mph),
    "6": ("km/h para Nó", kmh_para_no)
  }
  print("--- Menu de Velocidade ---")
  print("1- m/s para km/h\n2- mph para km/h\n3- Nó para km/h\n4- km/h para m/s\n5- km/h para mph\n6- km/h para Nó")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_pressao():
  clear_console()
  opcoes = {
    "1": ("atm para Pa", lambda v: v*101325),
    "2": ("atm para bar", lambda v: v*1.01325),
    "3": ("bar para Pa", lambda v: v*100000),
    "4": ("bar para atm", lambda v: v/1.01325)
  }
  print("--- Menu de Pressão ---")
  print("1- atm para Pa\n2- atm para bar\n3- bar para Pa\n4- bar para atm")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_energia():
  clear_console()
  opcoes = {
    "1": ("kcal para J", lambda v: v*4184),
    "2": ("kWh para J", lambda v: v*3600000),
    "3": ("cal para J", lambda v: v*4.184),
    "4": ("J para kcal", lambda v: v/4184)
  }
  print("--- Menu de Energia ---")
  print("1- kcal para J\n2- kWh para J\n3- cal para J\n4- J para kcal")
  escolha = input("Escolha a opção: ")

  if escolha in opcoes:
    nome_conv, func = opcoes[escolha]
    val = ler_valor("Digite o valor: ")
    resultado = func(val)
    print(f"\033[32mResultado: {resultado:.4f}\033[0m")
    salvar_historico(nome_conv, val, resultado)
    input("\nPressione ENTER para continuar...")
  else:
    print("\033[31mOpção inválida!\033[0m")
    input("\nPressione ENTER para continuar...")

def menu_engenharia():
  
  menu = True
  while menu:
    clear_console()
    print("--- MEDIDAS de 'Engenharia' ---")
    print("1.Área")
    print("2.Velocidade")
    print("3.Pressão")
    print("4.Energia")
    print("5.Voltar ao menu")
    escolha = input("Digite a opção que deseja: ")

    if escolha == "1": menu_area()
    elif escolha == "2": menu_velocidade()
    elif escolha == "3": menu_pressao()
    elif escolha == "4": menu_energia()
    elif escolha == "5":
      menu = False
      print("Voltando ao menu")
    else: 
      print("Digite um valor valido")
      input("\nPressione ENTER para continuar...")

def menu_financeiro():
  while True:
    clear_console()
  
    TAXA_USD = 5.05 
    TAXA_EUR = 5.45      
    TAXA_LIBRA = 6.30    
    TAXA_BTC = 340000.00 

    opcoes = {
        "1": ("Dólar (USD) para Real (BRL)", lambda v: v * TAXA_USD),
        "2": ("Real (BRL) para Dólar (USD)", lambda v: v / TAXA_USD),
        "3": ("Euro (EUR) para Real (BRL)", lambda v: v * TAXA_EUR),
        "4": ("Real (BRL) para Euro (EUR)", lambda v: v / TAXA_EUR),
        "5": ("Libra (GBP) para Real (BRL)", lambda v: v * TAXA_LIBRA),
        "6": ("Real (BRL) para Libra (GBP)", lambda v: v / TAXA_LIBRA),
        "7": ("Bitcoin (BTC) para Real (BRL)", lambda v: v * TAXA_BTC),
        "8": ("Real (BRL) para Bitcoin (BTC)", lambda v: v / TAXA_BTC)
    }

    print("--- Menu Financeiro (Câmbio) ---")
    print("1- Dólar para Real")
    print("2- Real para Dólar")
    print("3- Euro para Real")
    print("4- Real para Euro")
    print("5- Libra para Real")
    print("6- Real para Libra")
    print("7- Bitcoin para Real")
    print("8- Real para Bitcoin")
    print("9- Voltar ao menu principal")

    escolha = input("\nEscolha a opção: ")

    if escolha == "9":
      break

    if escolha in opcoes:
      nome_conv, func = opcoes[escolha]
      val = ler_valor("Digite o valor a ser convertido: ")
      resultado = func(val)
            
      if "Bitcoin" in nome_conv:
        print(f"\033[32mResultado: {resultado:.6f}\033[0m")
      else:
        print(f"\033[32mResultado: {resultado:.2f}\033[0m")
                
      salvar_historico(nome_conv, val, resultado)
      input("\nPressione ENTER para continuar...")
    else:
      print("\033[31mOpção inválida!\033[0m")
      input("\nPressione ENTER para continuar...")


menu = True
while menu:
  clear_console()
  print("--- MENU PRINCIPAL ---")
  print("1. Medidas Físicas")
  print("2. Dados e Tempo")
  print("3. Engenharia")
  print("4. Financeiro")
  print("5. Ver Histórico (Últimas 3)")
  print("6. Sair")

  opcao = input("Digite oque deseja fazer: ")

  if opcao == '1':
    menu_medidas_fisicas()
  elif opcao == '2':
    menu_dados_tempo()
  elif opcao == '3':
    menu_engenharia()
  elif opcao == '4':
    menu_financeiro()
  elif opcao == '5':
    exibir_historico()
  elif opcao == '6':
    print("Desligando sistema....")
    menu = 0
  else:
    print("\033[31mDigite um número válido.\033[0m")
    input("\nPressione ENTER para continuar...")