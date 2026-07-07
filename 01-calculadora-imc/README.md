# 🧮 Calculadora de IMC com Diagnóstico
 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
 
Projeto #01 de uma série de exercícios de lógica de programação em Python, com foco em variáveis, tipos de dados, operadores aritméticos e estruturas condicionais.
 
## 📋 Descrição
 
Programa de terminal que calcula o Índice de Massa Corporal (IMC) do usuário a partir do peso e da altura informados, e retorna uma classificação personalizada de acordo com a **idade** e a **faixa de IMC**, seguindo referências usadas em sistemas de saúde para adultos e idosos.
 
O resultado é exibido no terminal com cores ANSI (verde, amarelo, vermelho) para facilitar a leitura rápida do diagnóstico, e o usuário pode optar por salvar o histórico de cálculos em um arquivo `.txt` local.
 
## 🛠️ Tecnologias utilizadas
 
- **Python 3.10+** — uso de recursos modernos como *type hints* e tuplas de exceções estruturadas (`except (ValueError, ZeroDivisionError):`)
- Módulos nativos apenas — nenhuma dependência externa
## ⚙️ Funcionalidades
 
- Cálculo do IMC a partir de peso (kg) e altura (m)
- Classificação por faixa etária:
  - **20 a 59 anos**: abaixo do peso, peso adequado, sobrepeso, obesidade grau I, II e III
  - **60 anos ou mais**: faixas ajustadas conforme recomendação para idosos
  - **0 a 19 anos**: aviso informando que não há tabela fixa aplicável
- Mensagens coloridas no terminal (verde = adequado, amarelo = atenção, vermelho = risco)
- Validação de entradas: rejeita peso, altura ou idade menores ou iguais a zero, pedindo nova tentativa
- Tratamento de erros para entradas não numéricas (`try/except`)
- Opção de salvar cada resultado em `historico_imc.txt`, com nome, idade, peso, altura e IMC
- Loop de execução contínua, perguntando se o usuário deseja fazer um novo cálculo
## 💻 Exemplo de execução
 
```text
Por favor digite seu nome: Maria
Digite o seu peso: 68
Digite sua altura: 1.65
Digite sua idade: 32
 
Seu IMC é de 24.98
O seu peso está no peso adequado baseado na sua idade
 
Deseja salvar este resultado no historico? (s/n): s
O resultado foi salvo com sucesso no arquivo 'historico_imc.txt'!
 
Deseja colocar outro numero (s/n): n
Desligando sistema...
```
 
## 🚀 Como executar
 
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/calculadora-imc.git
 
# Acesse a pasta
cd calculadora-imc
 
# Execute o script
python calculadora_imc.py
```
 
> Requer apenas o Python 3.10 ou superior instalado — nenhuma biblioteca externa é necessária.
 
## 🧠 Foco de aprendizado
 
- Variáveis e tipagem (`type hints`)
- Operadores aritméticos (cálculo do IMC)
- Estruturas condicionais (`if` / `elif` / `else`)
- Tratamento moderno de exceções (`except (ValueError, ZeroDivisionError):`)
- Manipulação de arquivos (escrita em modo append)
- Boas práticas: uso de type hints nas funções (`def calcular_imc(peso: float, altura: float) -> float`)
## 🌍 Aplicação no mundo real
 
A lógica de classificar um valor numérico em faixas é a base de diversos sistemas do dia a dia:
 
- Apps de telemedicina e saúde digital (classificação de IMC, pressão arterial, glicemia)
- Sistemas de crédito (faixas de score)
- Precificação de seguros (categorização de risco)
Qualquer sistema que precise transformar um número em um "nível" segue essencialmente o mesmo padrão de condicionais usado aqui.
 
## 🛡️ Robustez e defesa de código
 
O projeto foi construído pensando em cenários de falha (*edge cases*) desde a primeira versão:
 
- Peso, altura ou idade menores ou iguais a zero são rejeitados antes do cálculo, blindando o sistema contra erros de divisão por zero
- Entradas de texto inválidas onde se esperam números são capturadas pelo bloco `except`, impedindo que o programa quebre (*crash*)
- Loop de validação contínuo até receber dados estritamente corretos
## 📁 Estrutura de saída (persistência)
 
Ao optar por salvar o histórico, os dados são gravados em `historico_imc.txt` no formato:
 
```
Nome: Maria | Idade: 32 anos | Peso: 68.0Kg | Altura: 1.65m | IMC: 24.98
```
 
## 🔧 Próximos passos (ideias de evolução)
 
- [ ] Exportar histórico em formato CSV para abertura em planilhas
- [ ] Criar uma versão com interface gráfica utilizando a biblioteca nativa Tkinter
- [ ] Adicionar testes unitários automatizados com `unittest` ou `pytest` para as funções de cálculo e faixa
- [ ] Adicionar suporte a múltiplos idiomas
## 📄 Licença
 
Este projeto está sob a licença MIT — sinta-se livre para usar, estudar e adaptar.
 
---