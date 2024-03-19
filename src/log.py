
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# Função para registrar uma mensagem de log com nível DEBUG
def debug(msg):
    logging.debug(msg)

# Função para registrar uma mensagem de log com nível INFO
def info(msg):
    logging.info(msg)

# Função para registrar uma mensagem de log com nível WARNING
def warning(msg):
    logging.warning(msg)

# Função para registrar uma mensagem de log com nível ERROR
def error(msg):
    logging.error(msg)

# Função para registrar uma mensagem de log com nível CRITICAL
def critical(msg):
    logging.critical(msg)
