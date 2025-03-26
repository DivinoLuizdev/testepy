import logging
import json
import requests

# Configuração do logger para enviar logs via HTTP
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # HTTP handler for ELK
    elk_url = "http://localhost:5044"  # URL do Logstash
    http_handler = LoggingHTTPHandler(elk_url)
    http_handler.setFormatter(formatter)
    logger.addHandler(http_handler)

    return logger

class LoggingHTTPHandler(logging.Handler):
    def __init__(self, elk_url):
        super().__init__()
        self.elk_url = elk_url

    def emit(self, record):
        try:
            log_entry = self.format(record)
            log_message = {
                "level": record.levelname,
                "message": record.getMessage(),
                "timestamp": self.formatTime(record),
                "logger": record.name,
                "pathname": record.pathname,
                "lineno": record.lineno,
                "funcName": record.funcName
            }
            response = requests.post(
                self.elk_url,
                headers={"Content-Type": "application/json"},
                data=json.dumps(log_message)
            )
            if response.status_code != 200:
                print(f"Erro ao enviar log: {response.status_code}, {response.text}")
        except Exception:
            self.handleError(record)