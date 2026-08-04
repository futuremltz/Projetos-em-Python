# Organizador de Arquivos Automático
 
![Python](https://img.shields.io/badge/linguagem-Python-blue.svg)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen.svg)
 
## 📋 Descrição
 
Script em Python que varre uma pasta (por padrão, a pasta de **Downloads**) e organiza automaticamente os arquivos em subpastas de acordo com sua extensão — documentos, músicas, vídeos, imagens e arquivos de programação. Um problema simples e extremamente comum no dia a dia, resolvido com automação.
 
O foco principal deste projeto é fixar conceitos de manipulação de arquivos e diretórios em Python:
- Módulos `os` e `shutil`
- Dicionários como estrutura de mapeamento (extensão → categoria)
- Laços de repetição e condicionais aplicados a arquivos reais do sistema
**Esforço:** Rápido
 
## 🚀 Funcionalidades
 
- **Varredura da pasta alvo** com `os.listdir()`, ignorando subpastas já existentes (`os.path.isdir()`).
- **Identificação da extensão** de cada arquivo com `os.path.splitext()`, normalizada para minúsculas (`.lower()`) — evitando que `.PDF` e `.pdf` sejam tratados como categorias diferentes.
- **Mapeamento extensão → categoria** feito via dicionário, cobrindo:
  - `.pdf`, `.docx` → **Documentos**
  - `.mp3` → **Músicas**
  - `.mp4` → **Vídeos**
  - `.png`, `.jpg` → **Imagens**
  - `.c` → **Programação**
- **Criação automática da subpasta de destino**, caso ainda não exista (`os.makedirs()`).
- **Movimentação do arquivo** para a pasta correta com `shutil.move()`.
- **Feedback no terminal** a cada arquivo movido, informando origem e destino.
## 🌍 Aplicação no mundo real
 
Organização automática de arquivos é a base de:
- **Ferramentas de produtividade** (ex: Hazel no macOS, File Juggler no Windows), que aplicam regras automáticas de organização de pastas.
- **Pipelines de ingestão de dados**, que classificam arquivos recebidos (logs, imagens, relatórios) em diretórios apropriados antes do processamento.
- **Sistemas de backup e arquivamento**, que categorizam arquivos por tipo antes de armazená-los em diferentes destinos (frio/quente, local/nuvem).
O padrão central — **inspecionar metadados de um item (aqui, a extensão) e decidir seu destino com base em regras** — se repete em praticamente qualquer sistema que precisa lidar com grandes volumes de arquivos de forma automática.
 
## ⚙️ O desafio em Python
 
Os principais pontos de atenção neste projeto foram:
- Diferenciar corretamente **arquivos de pastas** antes de tentar processá-los (`os.path.isdir()`), já que tentar mover ou ler uma subpasta como se fosse um arquivo causaria erro.
- Normalizar a extensão (minúsculas) antes de comparar com as chaves do dicionário, evitando falhas silenciosas de categorização por diferença de maiúsculas/minúsculas.
- Usar `os.path.join()` em vez de concatenar strings manualmente, garantindo compatibilidade entre sistemas operacionais (Windows usa `\`, Linux/macOS usam `/`).
## ✅ Boas práticas aplicadas (Clean Code)
 
- **Estrutura de dados como configuração**: o dicionário `categorias` centraliza as regras de organização, facilitando adicionar novas extensões sem alterar a lógica do script.
- **Checagem de existência antes de criar pastas**: `os.path.exists()` evita erro ao tentar criar uma pasta que já existe.
- **Uso de `os.path` para tudo que envolve caminhos**, em vez de manipulação manual de strings, tornando o script portátil entre sistemas operacionais.
## 🛠️ Como executar
 
1. Ajuste a variável `pasta` no início do script para o caminho desejado:
```python
pasta = "C:/Users/MeuUsuario/Downloads"
```
 
2. Rode o script:
```bash
python organizador.py
```
 
## 💬 Exemplo de saída
 
```
Sucesso! O arquivo 'relatorio.pdf' foi movido para a pasta 'Documentos'
Sucesso! O arquivo 'musica.mp3' foi movido para a pasta 'Musicas'
Sucesso! O arquivo 'foto.jpg' foi movido para a pasta 'Imagens'
```
 
## ⚠️ Observação importante
 
Este script **move** arquivos de verdade (`shutil.move`), então é recomendável testá-lo primeiro em uma pasta de exemplo (não a pasta de Downloads real) antes de usá-lo em arquivos importantes.
 
## 📌 Possíveis melhorias futuras
 
- Usar `pathlib.Path` no lugar de `os.path`, aproveitando uma API mais moderna e orientada a objetos.
- Receber a pasta alvo via argumento de linha de comando (`argparse`), em vez de fixá-la no código.
- Tratar exceções de `shutil.move()` (ex: arquivo em uso, permissão negada) em vez de deixar o script quebrar.
- Adicionar uma categoria "Outros" para extensões não mapeadas, em vez de simplesmente ignorá-las.
- Registrar um log (`logging`) das movimentações, além do `print` no terminal.
- Adicionar um modo "simulação" (`--dry-run`) que mostra o que seria movido sem mover de fato.
## 📝 Commit
 
```
feat: add automatic file organizer script
```
 
---
 
*Projeto #04 de uma série de exercícios de programação em Python, com foco em fixar fundamentos da linguagem através de projetos práticos e aplicáveis ao mundo real.*
