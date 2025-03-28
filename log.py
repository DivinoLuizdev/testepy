import requests
import json
import subprocess
import time
import uuid  # Para gerar o execution_id
from log import RobotLogger 

# URL do Logstash
ROBO = 'testepy'

# Gerando um UUID para o execution_id
execution_id = str(uuid.uuid4())

# Configuração do logger usando log.py
robot_logger = RobotLogger(ROBO, execution_id)
logger = robot_logger.get_logger()

try:
    logger.info("Starting the process: waiting for 10 seconds.")
    # Espera 10 segundos
    time.sleep(10)
    logger.info("Wait completed. Creating a text file with the message 'Bom dia'.")

    # Cria um arquivo de texto com "Bom dia"
    with open("mensagem.txt", "w") as file:
        file.write("Bom dia")
    logger.info("File 'mensagem.txt' created successfully.")

    # Abre o arquivo de texto no Bloco de Notas
    logger.info("Opening 'mensagem.txt' in Notepad.")
    subprocess.Popen(['notepad.exe', 'mensagem.txt'])
    logger.info("Notepad opened successfully.")
except Exception as e:
    logger.error(f"An error occurred: {str(e)}")
