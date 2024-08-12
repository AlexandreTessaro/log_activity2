# LoggingApp

Este projeto é um exemplo de uma calculadora simples em Python que utiliza a biblioteca `logging` para registrar logs das operações realizadas. O objetivo é demonstrar o uso de diferentes níveis de log (DEBUG, INFO, WARNING, ERROR, CRITICAL) e salvar esses logs em um arquivo.

## Funcionalidades

- **Operações Básicas:** Soma, Subtração, Multiplicação e Divisão.
- **Registro de Logs:** Todas as operações realizadas são registradas em um arquivo `calculator.log`.
- **Tratamento de Erros:** Erros como divisão por zero são capturados e registrados no log.

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a lógica da calculadora e o sistema de logging.
- `calculator.log`: Arquivo onde os logs são salvos automaticamente após a execução do programa.
- `README.md`: Este arquivo onde fica as informações sobre o projeto.

## Como Executar

1. Clone este repositório em sua máquina local:

   ```bash
   git clone https://github.com/seu_usuario/LoggingApp.git

2. Navegue até o diretório do projeto:

    ```bash
    cd LoggingApp

3. Execute o programa:

    ```bash
    python app.py
