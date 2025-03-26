import subprocess
import time

# Espera 10 segundos
time.sleep(10)

# Cria um arquivo de texto com "Bom dia"
with open("mensagem.txt", "w") as file:
    file.write("Bom dia")

# Abre o arquivo de texto no Bloco de Notas
subprocess.Popen(['notepad.exe', 'mensagem.txt'])
