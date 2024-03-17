import config_path
import os
import shutil
import util

def delete_arq(file_path):
    try:
        os.remove(file_path)
        print(f"Arquivo {file_path} apagado com sucesso")
    except FileNotFoundError:
        print("Arquivo nao encontrado...")
    except Exception as e:
        print(f"Erro ao apagar o arquivo [{file_path}]: {e}")

def mv_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"Movendo arquivo: {source_path} --> {destination_path}")
    except FileNotFoundError:
        print(f"O arquivo [{source_path}] nao foi encontrado...")
    except Exception as e:
        print(f"Ocorre um erro ao mover o arquivo {source_path}: \n{e}")

def delete_dir(dir_path):
    try:
        shutil.rmtree(dir_path)
        print(f"Diretorio apagado: {dir_path}")
    except FileNotFoundError:
        print(f"O diretorio [{dir_path}] nao foi encontrado...")
    except Exception as e:
        print(f"Erro ao apagar diretorio [{dir_path}]: \n{e}")

def clear_dir(dir_path):
    try:
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        print(f"Conteudo do diretorio [{dir_path}] apagado com sucesso.")
    except FileNotFoundError:
        print(f"O diretorio [{dir_path}] nao foi encontrado...")
    except Exception as e:
        print(f"Erro ao apagar limpar o diretorio [{dir_path}]: \n{e}")

def main(configs):
    list_thread = []
    for key in configs:
        dir = config_path.get_value(configs, key)
        list_thread.append((clear_dir, (dir,)))
    
    util.create_threads(list_thread)