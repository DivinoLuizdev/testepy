import logging
import os
from datetime import datetime

class RobotLogger:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        
        # Obtendo a data atual e formatando-a
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Diretório de log e nome do arquivo com a data
        self.log_directory = f"C:\\RPA\\{self.robot_name}\\log"
        self.log_filename = os.path.join(self.log_directory, f'{current_date}.txt')

        # Criar diretório de log, se não existir
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        # Configurando o logging para o robô específico
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_filename),  # Log em arquivo com data
                logging.StreamHandler()  # Log no console
            ]
        )
        self.logger = logging.getLogger(self.robot_name)

    def get_logger(self):
        return self.logger
