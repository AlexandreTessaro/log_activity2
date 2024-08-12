import logging

# Configuração básica do logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Função para obter o logger configurado
def get_logger(name):
    return logging.getLogger(name)
