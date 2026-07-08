# 🔄 Conversor de Unidades Multi-Menu
 
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
 
Projeto #02 de uma série de exercícios de lógica de programação em Python, com foco em estruturas de decisão, loops e funções separadas por responsabilidade.
 
## 📋 Descrição
 
Sistema de terminal com **menu principal e submenus navegáveis**, que permite converter unidades de diversas categorias — medidas físicas, dados e tempo, engenharia e câmbio financeiro. Após cada conversão, o usuário retorna ao menu correspondente até optar por voltar ou sair do programa.
 
O programa também mantém um pequeno histórico em memória das últimas conversões realizadas, acessível a qualquer momento pelo menu principal.
 
## 🛠️ Tecnologias utilizadas
 
- **Python 3.10+**
- Módulo nativo `os` (limpeza de tela multiplataforma)
- Nenhuma dependência externa
## ⚙️ Funcionalidades
 
### 📐 Medidas Físicas
- **Comprimento**: metro → cm, mm, km, polegada, pés
- **Massa**: quilograma → grama, miligrama, libra, onça
- **Temperatura**: conversões entre Celsius, Fahrenheit e Kelvin
- **Volume**: litro → mililitro, m³, galão
### ⏱️ Dados e Tempo
- **Tempo**: segundos, minutos, horas e dias entre si
- **Dados**: Byte, Kilobyte, Megabyte, Gigabyte e Terabyte
### 🏗️ Engenharia
- **Área**: m² → cm², km², hectare, acre
- **Velocidade**: m/s, km/h, mph e nós
- **Pressão**: atm, bar e Pascal
- **Energia**: caloria, kcal, kWh e Joule
### 💰 Financeiro (câmbio)
- Conversão entre Real (BRL) e Dólar, Euro, Libra e Bitcoin (taxas fixas definidas no código)
### 🧭 Navegação e histórico
- Menu principal com acesso a todas as categorias
- Submenus dedicados por tipo de conversão
- Opção **"Ver Histórico"**, exibindo as últimas 3 conversões realizadas na sessão
- Tela limpa automaticamente a cada transição de menu (`os.system('cls'/'clear')`)
- Validação de opções: entradas fora do intervalo esperado não travam o programa, apenas pedem nova escolha
## 💻 Exemplo de execução
 
```text
--- MENU PRINCIPAL ---
1. Medidas Físicas
2. Dados e Tempo
3. Engenharia
4. Financeiro
5. Ver Histórico (Últimas 3)
6. Sair
Digite oque deseja fazer: 1
 
--- MEDIDAS FÍSICAS ---
1.Comprimento (m -> Para qual voce deseja)
2.Massa (kg -> Para qual voce deseja)
3.Temperatura
4.Volume (L -> Para qual voce deseja)
5.Voltar ao menu
Digite a opção que deseja: 3
 
--- Menu de Temperatura ---
1- Celsius para Fahrenheit
2- Celsius para Kelvin
3- Fahrenheit para Celsius
4- Kelvin para Celsius
Escolha a opção: 1
Digite o valor: 25
Resultado: 77.00
```
 
## 🚀 Como executar
 
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/conversor-unidades.git
 
# Acesse a pasta
cd conversor-unidades
 
# Execute o script
python conversor_de_unidades.py
```
 
> Requer apenas o Python 3.10 ou superior — nenhuma biblioteca externa é necessária.
 
## 🧠 Foco de aprendizado
 
- Estruturas de decisão (`if` / `elif` / `else`) simulando um `switch` de múltiplas opções
- Loops de repetição (`while`) controlando a navegação entre menus
- Funções separadas por responsabilidade — cada categoria e cada submenu tem sua própria função
- Uso de **dicionário de opções** (`{"1": (nome, função), ...}`) para mapear escolhas a conversões, evitando encadeamento de `if`
- Funções auxiliares reutilizáveis (`ler_valor`, `salvar_historico`, `clear_console`) para eliminar repetição de código
- Uso de `lambda` para conversões simples de uma linha
## 🌍 Aplicação no mundo real
 
Sistemas de conversão de unidades são essenciais em cenários como:
 
- **ERPs logísticos**, que precisam lidar com medidas de peso, volume e distância entre fornecedores de diferentes países
- **E-commerce internacional**, convertendo moedas e unidades de medida para o cliente final
- **Sistemas industriais**, onde conversões de área, pressão e energia aparecem constantemente em cálculos de engenharia
O padrão de "menu → submenu → função de cálculo" também é a base de praticamente qualquer sistema CLI (interfaces de linha de comando) usado em ferramentas internas de empresas.
 
## 🛡️ Robustez e defesa de código
 
- A função `ler_valor()` centraliza a validação de números, capturando `ValueError` em loop até receber uma entrada válida
- Escolhas de menu fora do intervalo esperado exibem mensagem de erro e retornam ao próprio menu, sem travar o programa
- Histórico limitado às 3 últimas conversões (`historico.pop(0)`), evitando crescimento indefinido da lista em memória
## 🔧 Próximos passos (ideias de evolução)
 
- [ ] Substituir os "magic numbers" restantes (fatores de conversão soltos no código) por constantes nomeadas no topo do arquivo
- [ ] Buscar cotações de câmbio em tempo real via API, em vez de taxas fixas
- [ ] Persistir o histórico em arquivo (`.txt`/`.csv`), como no Projeto #01
- [ ] Adicionar testes unitários para as funções de conversão
- [ ] Registrar um GIF do menu em funcionamento para exibir no README

## 📄 Licença
 
Este projeto está sob a licença MIT — sinta-se livre para usar, estudar e adaptar.
 
---