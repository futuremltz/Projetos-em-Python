# 🔐 Validador de Senha Forte

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

Projeto #03 de uma série de exercícios de lógica de programação em Python, com foco em manipulação de strings/caracteres, contadores e laços `for`.

## 📋 Descrição

Programa de terminal que analisa uma senha digitada pelo usuário e classifica sua força em **fraca**, **média** ou **forte**, com base em quatro critérios de segurança: tamanho mínimo, presença de letra maiúscula, número e símbolo especial.

O projeto simula regras reais de segurança usadas por sistemas de login corporativos — o mesmo tipo de validação encontrado em bancos, e-commerces e plataformas SaaS antes de aceitar o cadastro de uma senha.

## 🛠️ Tecnologias utilizadas

- **Python 3.10+**
- Módulo nativo `time` (simulação de bloqueio temporário)
- Métodos nativos de string (`.isupper()`, `.isdigit()`, `.isalnum()`, `.isspace()`, `.strip()`)
- Nenhuma dependência externa

## ⚙️ Funcionalidades

- Validação de senha vazia ou composta apenas por espaços em branco
- Análise por critério, cada um em uma função própria:
  - `tem_tamanho_minimo` — mínimo de 8 caracteres
  - `tem_maiuscula` — pelo menos uma letra maiúscula
  - `tem_numero` — pelo menos um dígito
  - `tem_simbolo` — pelo menos um símbolo especial (não alfanumérico e não espaço)
- Feedback específico no terminal, informando **exatamente qual critério** está faltando
- Barra de força visual (`[##--------]`, `[######----]`, `[##########]`) conforme a pontuação
- Classificação final:
  - **0-1 ponto** → Senha **FRACA**
  - **2-3 pontos** → Senha **MÉDIA** (aceita, mas com sugestão de melhoria)
  - **4 pontos** → Senha **FORTE** (cadastro aprovado)
- Contador de tentativas fracas consecutivas, com **bloqueio simulado de 5 segundos** após 3 tentativas seguidas de senha fraca

## 💻 Exemplo de execução

```text
Digite sua senha: abc123

Analisando segurança da senha...
Falta: Ter no mínimo 8 caracteres.
Falta: Precisa ter pelo menos uma letra maiuscula.
Falta: Precisa ter no minimo um simbolo especial.
Força da Senha: FRACA [##--------]

Digite sua senha: Abcdef12

Analisando segurança da senha...
Falta: Precisa ter no minimo um simbolo especial.
Força da Senha: MÉDIA [######----]
Senha aceita, mas poderia ser melhor!
```

## 🚀 Como executar

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/validador-senha.git

# Acesse a pasta
cd validador-senha

# Execute o script
python validador_senha.py
```

> Requer apenas o Python 3.10 ou superior — nenhuma biblioteca externa é necessária.

## 🧠 Foco de aprendizado

- Manipulação de strings e caracteres (`for caractere in senha`)
- Contadores de pontuação e de tentativas
- Laços `for` para varrer cada caractere da senha
- Extração de cada critério de validação em uma função separada, mantendo o código legível e testável isoladamente
- Uso de métodos nativos de string (`.isupper()`, `.isdigit()`) em vez de comparações manuais de código ASCII
- Simulação de bloqueio temporário com o módulo `time`

## 🌍 Aplicação no mundo real

Validação de senha é um requisito obrigatório em praticamente qualquer sistema de autenticação:

- **Bancos e fintechs**, onde a força da senha impacta diretamente a segurança da conta do cliente
- **E-commerces e plataformas SaaS**, que precisam balancear segurança e experiência do usuário no cadastro
- **Compliance e proteção de dados** (LGPD/GDPR), já que políticas de senha forte fazem parte das boas práticas exigidas para proteger dados pessoais

O padrão de "somar pontos por critério atendido e classificar o resultado" também aparece em sistemas de score de crédito e triagem de risco — reforçando um tema recorrente nesta série de projetos.

## 🛡️ Robustez e defesa de código

- Senhas vazias ou compostas só de espaços são rejeitadas antes de qualquer análise (`corrigir_valor`)
- A senha é sempre normalizada com `.strip()` antes da validação, evitando espaços acidentais no início/fim
- O bloqueio simulado impede tentativas ilimitadas de senhas fracas em sequência, simulando uma proteção básica contra tentativa e erro

## 🔧 Próximos passos (ideias de evolução)

- [ ] Adicionar cores ANSI à barra de força (vermelho/amarelo/verde), como nos projetos anteriores da série
- [ ] Usar expressões regulares (`re`) para consolidar as verificações de símbolo e maiúscula
- [ ] Permitir configurar os critérios (tamanho mínimo, exigência de símbolo, etc.) via constantes no topo do arquivo
- [ ] Adicionar verificação contra senhas comuns (ex: lista de senhas mais usadas/vazadas)
- [ ] Adicionar testes unitários para cada função de critério (`tem_maiuscula`, `tem_numero`, etc.)

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, estudar e adaptar.

---

**Commit sugerido:** `feat: add password strength validator with character analysis`