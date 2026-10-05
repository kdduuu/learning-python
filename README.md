# Learning Python

Repositório de estudos em Python com exemplos de fundamentos da linguagem, exercícios e pequenos projetos desenvolvidos durante o aprendizado.

A estrutura foi organizada para manter os conteúdos fáceis de localizar e acompanhar a evolução dos estudos ao longo do tempo.

## Estrutura

```text
learning-python/
├── fundamentos/
├── modulos-e-pacotes/
│   ├── modulo-simples/
│   └── pacote-local/
├── projetos/
│   ├── arquivos/
│   ├── calculadora/
│   ├── loja-corinthians/
│   └── poo-animais/
├── exercicios/
│   ├── desafios/
│   └── debug/
├── dados/
├── .gitignore
└── README.md
```

## Conteúdos

### Fundamentos

A pasta `fundamentos/` reúne exemplos e anotações sobre:

- dicionários;
- funções nativas;
- palavras reservadas;
- operações com listas;
- operações com strings;
- formatação numérica.

### Módulos e pacotes

`modulos-e-pacotes/` contém exemplos simples de organização de código em arquivos separados, importação de módulos e uso de um pacote local.

### Projetos

Em `projetos/` ficam pequenos programas desenvolvidos para praticar diferentes conceitos:

- `arquivos/`: leitura, escrita e manipulação de dados em JSON;
- `calculadora/`: calculadora de terminal com operações básicas;
- `loja-corinthians/`: cadastro e gerenciamento simples de produtos;
- `poo-animais/`: exemplo de orientação a objetos, herança e sobrescrita de métodos.

### Exercícios

A pasta `exercicios/desafios/` mantém os exercícios numerados em ordem, com nomes padronizados como `desafio_04_01.py` e `desafio_20_03.py`.

`exercicios/debug/` contém exemplos usados para praticar depuração.

### Dados de exemplo

`dados/clientes_exemplo.json` contém somente dados fictícios utilizados para estudo.

## Convenções de nomes

- Arquivos Python usam `snake_case.py`.
- Pastas de conteúdo usam nomes simples e descritivos.
- Exercícios numerados usam dois dígitos para facilitar a ordenação.
- Arquivos gerados pelo Python, ambientes virtuais e variáveis de ambiente são ignorados pelo Git.

## Como executar

Tenha o Python instalado e execute o arquivo desejado pelo terminal. Por exemplo:

```bash
python projetos/calculadora/main.py
```

ou:

```bash
python projetos/loja-corinthians/main.py
```

Para os exemplos de módulos:

```bash
python modulos-e-pacotes/modulo-simples/main.py
python modulos-e-pacotes/pacote-local/main.py
```

## Objetivo

Este repositório funciona como um registro prático da minha evolução em Python, reunindo desde conceitos básicos até pequenos projetos de terminal e exercícios de programação orientada a objetos.
