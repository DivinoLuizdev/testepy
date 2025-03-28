import logging
import os
import platform
import uuid
from datetime import datetime
import json

class RobotLogger:
    def __init__(self, robot_name):
        self.robot_name = robot_name
        self.execution_id = str(uuid.uuid4())  # Gerar um ID único para a execução

        # Diretório de log e nome do arquivo com a data atual
        current_date = datetime.now().strftime("%Y-%m-%d")
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
                logging.FileHandler(self.log_filename, mode='a'),  # Log em arquivo com data
                logging.StreamHandler()  # Log no console
            ]
        )
        self.logger = logging.getLogger(self.robot_name)
        self.start_time = datetime.now()

        # Adiciona informações do sistema ao log
        self.logger.info(json.dumps(self.get_system_info(), indent=4))

    def get_system_info(self):
        """Captura informações do sistema"""
        return {
            "os": platform.system(),
            "os_version": platform.version(),
            "hostname": platform.node(),
            "robot_name": self.robot_name,
            "execution_id": self.execution_id,
            "start_time": datetime.now().isoformat()
        }

    def get_logger(self):
        return self.logger

    def end_execution(self):
        """Finaliza a execução do robô, registrando o tempo e o status."""
        self.system_info["end_time"] = datetime.now().isoformat()
        self.system_info["status"] = "completed"
        self.system_info["total_execution_time"] = str(datetime.now() - self.start_time)
        
        # Adiciona a informação de término da execução ao log
        self.logger.info("Execution completed:")
        self.logger.info(json.dumps(self.system_info, indent=4))

    def log_message(self, message):
        """Método para logar mensagens personalizadas, com timestamp"""
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "message": message
        }
        self.logger.info(json.dumps(log_data, indent=4))
