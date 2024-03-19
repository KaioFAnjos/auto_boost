import config_path
import os
import shutil
import util
import log

def delete_arq(file_path):
    try:
        os.remove(file_path)
        log.info(f"Arquivo {file_path} apagado com sucesso")
    except FileNotFoundError:
        log.error("Arquivo nao encontrado...")
    except Exception as e:
        log.error(f"Erro ao apagar o arquivo [{file_path}]: {e}")

def mv_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        log.info(f"Movendo arquivo: {source_path} --> {destination_path}")
    except FileNotFoundError:
        log.error(f"O arquivo [{source_path}] nao foi encontrado...")
    except Exception as e:
        log.error(f"Ocorre um erro ao mover o arquivo {source_path}: \n{e}")

def delete_dir(dir_path):
    try:
        shutil.rmtree(dir_path)
        log.info(f"Diretorio apagado: {dir_path}")
    except FileNotFoundError:
        log.error(f"O diretorio [{dir_path}] nao foi encontrado...")
    except Exception as e:
        log.error(f"Erro ao apagar diretorio [{dir_path}]: \n{e}")

def clear_dir(dir_path):
    try:
        for file in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        log.info(f"Conteudo do diretorio [{dir_path}] apagado com sucesso.")
    except FileNotFoundError:
        log.error(f"O diretorio [{dir_path}] nao foi encontrado...")
    except Exception as e:
        log.error(f"Erro ao apagar o diretorio [{dir_path}]...")

def main(configs):
    print("\tINICIANDO CLEAR FILES")
    list_thread = []
    for key in configs:
        dir = config_path.get_value(configs, key)
        list_thread.append((clear_dir, (dir,)))
    
    util.create_threads(list_thread)