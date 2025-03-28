import logging
import os
import platform
import uuid
from datetime import datetime
import json

class RobotLogger:
    def __init__(self, robot_name, execution_id):
        self.robot_name = robot_name
        self.execution_id = execution_id  # Recebe o execution_id

        # Diretório de log e nome do arquivo com a data atual
        current_date = datetime.now().strftime("%Y-%m-%d")
        self.log_directory = f"C:\\RPA\\{self.robot_name}\\log"
        self.log_filename = os.path.join(self.log_directory, f'{current_date}.json')  # Arquivo .json

        # Criar diretório de log, se não existir
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

        # Configurando o logging para o robô específico
        logging.basicConfig(
            level=logging.INFO,
            format='%(message)s',  # Apenas a mensagem como JSON
            handlers=[logging.FileHandler(self.log_filename, mode='a'),  # Log em arquivo JSON
                      logging.StreamHandler()]  # Log no console
        )
        self.logger = logging.getLogger(self.robot_name)
        self.start_time = datetime.now()

        # Log de informações do sistema com execution_id
        self.logger.info(json.dumps(self.get_system_info()))  # Log inicial com informações do sistema

    def get_system_info(self):
        """Captura informações do sistema e adiciona o execution_id"""
        return {
            "execution_id": self.execution_id,
            "os": platform.system(),
            "os_version": platform.version(),
            "hostname": platform.node(),
            "robot_name": self.robot_name,
            "start_time": datetime.now().isoformat()
        }

    def get_logger(self):
        return self.logger

    def end_execution(self):
        """Finaliza a execução do robô, registrando o tempo e o status."""
        system_info = self.get_system_info()
        system_info["end_time"] = datetime.now().isoformat()
        system_info["status"] = "completed"
        system_info["total_execution_time"] = str(datetime.now() - self.start_time)

        # Log de conclusão da execução com execution_id
        self.logger.info(json.dumps(system_info))  # Log final com informações da execução

    def log_message(self, message, level="INFO"):
        """Método para logar mensagens personalizadas, com timestamp e execution_id"""
        log_data = {
            "execution_id": self.execution_id,  # ID da execução para vincular os logs
            "timestamp": datetime.now().isoformat(),
            "level": level,  # Nível do log (INFO, ERROR, etc)
            "message": message,
            "robot_name": self.robot_name
        }
        self.logger.info(json.dumps(log_data))  # Log em formato JSON
