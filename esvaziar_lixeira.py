import subprocess
import ctypes
import os
from pathlib import Path

def popup(mensagem, titulo="Lixeira"):
    # Exibe popup na tela com icone de informacao
    ctypes.windll.user32.MessageBoxW(0, mensagem, titulo, 0x40)

def esvaziar_lixeira():
    print("Esvaziando lixeira...")
    print("=" * 50)

    try:
        # Esvazia a lixeira silenciosamente via PowerShell
        subprocess.run(
            ["PowerShell", "-Command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"],
        )
        print("Lixeira esvaziada com sucesso!")
        popup("Lixeira esvaziada com sucesso!", "Lixeira")

    except Exception as e:
        print(f"Erro ao esvaziar lixeira: {e}")
        popup(f"Erro ao esvaziar lixeira: {e}", "Lixeira - Erro")

    print("=" * 50)

def agendar_tarefa():
    # Caminho completo do script esvaziar_lixeira.py
    script = str(Path(__file__).resolve())

    # Caminho do Python no venv
    python = str(Path(__file__).resolve().parent / "venv" / "Scripts" / "python.exe")

    print("Agendando tarefa no Windows...")

    subprocess.run([
        "schtasks", "/create",
        "/tn", "EsvaziarLixeira",           # nome da tarefa
        "/tr", f"{python} {script}",        # executa esvaziar_lixeira.py
        "/sc", "daily",                     # frequência diária
        "/mo", "10",                        # a cada 10 dias
        "/st", "08:00",                     # horário de execução
        "/f"                                # sobrescreve se já existir
    ], check=True)

    print("Tarefa agendada com sucesso!")
    print("O script vai rodar automaticamente a cada 10 dias as 08:00.")

# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    # Agenda a tarefa no Windows
    agendar_tarefa()

    # Executa a limpeza imediatamente
    esvaziar_lixeira()