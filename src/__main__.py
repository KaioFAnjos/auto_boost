from functions_file import main as clear_files
from functions_process import main as clear_process
from config_path import main as config
import argparse



def main():

    parser = argparse.ArgumentParser(description='Definir qual script executar')
    parser.add_argument('--config_file', type=str, help='Caminho absoluto do arquivo de configuracao')
    parser.add_argument('--execute', type=str, help='Script a ser executado')

    args = parser.parse_args()


    if args.execute == 'clear_files':
        print("\tAUTO_BOOST --- INICIANDO CLEAR FILE")
        clear_files(config())
    elif args.execute == 'clear_process':
        print("\tAUTO_BOOST --- INICIANDO CLEAR PROCESS")
        clear_process()
    else:
        print("\tAUTO_BOOST --- INICIANDO TODOS OS PROCESSOS")
        clear_files(config())
        clear_process()


if __name__ == "__main__":
    main()
