import subprocess
import os
import configparser
import shutil
import util

#Carrega os paths do arquivo path.ini
def load_config():
    config = configparser.ConfigParser()
    section_config = {}
    if len(config.read('path/path.ini')) == 0:
        print("Erro: Não foi possivel ler o arquivo [path.ini]")
        exit()
    else:
        config.read('path/path.ini')
        for section in config.sections():
            section_config[section] = {}
            for key, value in config.items(section):
                section_config[section][key] = value
        
            
    return section_config   

#Lista o respectivo diretório.
def get_ls(config, dir):
    
    command_ls = ['ls', '-l', config['WINDOWS'][dir]]
    check_ls = subprocess.run(command_ls, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    try:
        print(f'Listando arquivos do diretório: ' + config['WINDOWS'][dir])
        subprocess.run(command_ls, check=True)
       
    except subprocess.CalledProcessError as e:
        print("Erro ao listar diretório...")
        print(f'ERRO: {e}')

#Deleta todos os arquivos dentro do respectivo diretório
def delete_content_dir(config, dir):
    content_folder = os.listdir(config['WINDOWS'][dir])

    try:
        for item in content_folder:
            path_item = os.path.join(config['WINDOWS'][dir], item)

            if os.path.isfile(path_item):
                os.remove(path_item)
                print(f'Apagando arquivo: {item}')

            elif os.path.isdir(path_item):
                shutil.rmtree(path_item)
                print(f'Apagando diretório: {item}')

        print(f"Conteúdo da pasta [{config['WINDOWS'][dir]}] excluído com sucesso...")
    except PermissionError as e :
        print(f"Erro de Permissão negada... {e}")
    except Exception as e:
        print(f"Erro ao apagar arquivos: {e}")
    

def get_config():
    return load_config()

def main():
    config = get_config()

    util.create_threads([
        (delete_content_dir, (config, 'dir_test')),
        (delete_content_dir, (config, 'downloads_path')),
        (delete_content_dir, (config, 'temp_path')),
        (delete_content_dir, (config, 'local_temp_path')),
    ])
    
if __name__ == "__main__":
    main()
    