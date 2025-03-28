import logging
import os
import platform
import uuid
from datetime import datetime
import json
import traceback

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
            format='%(message)s',  # Apenas a mensagem será formatada para JSON
            handlers=[
                logging.FileHandler(self.log_filename, mode='a'),  # Log em arquivo com data
                logging.StreamHandler()  # Log no console
            ]
        )
        self.logger = logging.getLogger(self.robot_name)
        self.start_time = datetime.now()

        # Log inicial com informações do sistema
        self.log_system_info()

    def log_system_info(self):
        """Captura e registra as informações do sistema em formato JSON."""
        system_info = {
            "robot_name": self.robot_name,
            "timestamp": datetime.now().isoformat(),
            "execution_id": self.execution_id,
            "os": platform.system(),
            "os_version": platform.version(),
            "hostname": platform.node(),
            "start_time": datetime.now().isoformat()
        }
        log_data = json.dumps(system_info)
        self.logger.info(log_data)

    def log_execution_progress(self, step_name, message, level="INFO"):
        """Registra o progresso da execução, incluindo o nome da etapa e o status."""
        log_data = {
            "robot_name": self.robot_name,
            "timestamp": datetime.now().isoformat(),
            "execution_id": self.execution_id,
            "level": level,
            "step_name": step_name,  # Nome da etapa ou função
            "message": message
        }
        log_message = json.dumps(log_data)
        self.logger.log(level, log_message)

    def log_error(self, error_message):
        """Log de erro com stack trace para facilitar a depuração."""
        error_details = {
            "robot_name": self.robot_name,
            "timestamp": datetime.now().isoformat(),
            "execution_id": self.execution_id,
            "level": "ERROR",
            "message": error_message,
            "stack_trace": traceback.format_exc()  # Inclui o stack trace para erros
        }
        log_message = json.dumps(error_details)
        self.logger.error(log_message)

    def end_execution(self):
        """Finaliza a execução do robô, registrando o tempo e o status."""
        end_time = datetime.now().isoformat()
        total_execution_time = str(datetime.now() - self.start_time)
        execution_status = "completed"
        
        # Log de término da execução com as informações finais
        execution_info = {
            "robot_name": self.robot_name,
            "timestamp": datetime.now().isoformat(),
            "execution_id": self.execution_id,
            "end_time": end_time,
            "status": execution_status,
            "total_execution_time": total_execution_time
        }
        log_data = json.dumps(execution_info)
        self.logger.info(log_data)

    def log_message(self, level, message):
        """Método para logar mensagens personalizadas em formato JSON."""
        log_data = {
            "robot_name": self.robot_name,
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "execution_id": self.execution_id,
            "message": message
        }
        log_message = json.dumps(log_data)
        self.logger.log(level, log_message)
