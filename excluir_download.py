'''
Este script move todos os arquivos e pastas da pasta Downloads para a lixeira do Windows.
'''
import os
from pathlib import Path
from send2trash import send2trash

def limpar_downloads():
    downloads_path = Path(os.path.expanduser("~")) / "Downloads"

    if not downloads_path.exists():
        print("Pasta Downloads não encontrada!")
        return

    print(f"Movendo para lixeira: {downloads_path}")
    print("=" * 50)

    arquivos_excluidos = 0
    pastas_excluidas = 0

    for item in downloads_path.iterdir():
        try:
            if item.is_file():
                send2trash(str(item))
                print(f"Arquivo movido para lixeira: {item.name}")
                arquivos_excluidos += 1

            elif item.is_dir():
                send2trash(str(item))
                print(f"Pasta movida para lixeira: {item.name}")
                pastas_excluidas += 1

        except Exception as e:
            print(f"Erro ao mover {item.name}: {e}")

    print("=" * 50)
    print(f"Concluido! {arquivos_excluidos} arquivos e {pastas_excluidas} pastas movidos para lixeira.")

# ===================== EXECUÇÃO =====================
if __name__ == "__main__":
    resposta = input("Tem certeza que deseja mover TODOS os arquivos da pasta Downloads para a lixeira? (s/N): ")

    if resposta.lower() == 's':
        limpar_downloads()
    else:
        print("Operacao cancelada.")