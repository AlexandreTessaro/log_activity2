import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("calculator.log"),
        logging.StreamHandler()
    ]
)

def calculate(num1, num2, operation):
    logging.debug(f"Tentando realizar a operação: {num1} {operation} {num2}")
    try:
        if operation == '+':
            result = num1 + num2
            logging.info(f'Operação: {num1} + {num2} = {result}')
        elif operation == '-':
            result = num1 - num2
            logging.info(f'Operação: {num1} - {num2} = {result}')
        elif operation == '*':
            result = num1 * num2
            logging.info(f'Operação: {num1} * {num2} = {result}')
        elif operation == '/':
            if num2 == 0:
                logging.critical("Tentativa de divisão por zero!")
                raise ZeroDivisionError("Não é possível dividir por zero")
            result = num1 / num2
            logging.info(f'Operação: {num1} / {num2} = {result}')
        else:
            logging.error(f'Operação inválida: {operation}')
            return "Operação inválida"
        
        return result
    except Exception as e:
        logging.error(f"Erro ao realizar a operação: {e}", exc_info=True)
        return "Erro na operação"

def main():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operation = input("Digite a operação (+, -, *, /) ou 'q' para sair: ")

            if operation.lower() == 'q':
                logging.info("Calculadora encerrada pelo usuário.")
                break

            result = calculate(num1, num2, operation)
            print(f"Resultado: {result}")
        except ValueError:
            logging.warning("Valor inválido inserido pelo usuário.")
            print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()
