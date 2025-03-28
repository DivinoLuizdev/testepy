import requests
import json
import subprocess
import time
from log import RobotLogger 

# URL do Logstash
ROBO = 'testepy'

# Configuração do logger usando log.py
robot_logger = RobotLogger(ROBO)
logger = robot_logger.logger  # Acessando diretamente o logger

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
