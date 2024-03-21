import psutil
import log
import re
import subprocess

def terminate_processes(process_name=[]):
    try:
        for name in process_name:
            if is_process_running(name):
                subprocess.run(["powershell", "-Command", f"Stop-Process -Name {name.replace('.exe', '')} -Force"], check=True)
                log.info(f"Processo [{name}] encerrado com sucesso.")

    except subprocess.CalledProcessError:
        log.warning(f"Não foi possível encerrar o processo [{name}] com privilégios elevados...")
    except Exception as e:
        log.warning(f"Erro ao tentar encerrar o processo [{name}]: {e}")

def is_process_running(process_name):
    for process in psutil.process_iter():
        try:
            if process_name.lower() == process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            log.warning("Processo não existe, não tem permissão para acessar ou é um processo zumbi")
            continue

        log.warning(f"O processo [{process_name}] não está em execução no momento...")
        return False
       
def list_processes():
    process_info_pattern = re.compile(r"pid=(\d+),\s+name='([^']+)',\s+status='([^']+)'")
    for process in psutil.process_iter():
        match = process_info_pattern.search(str(process))
        if match:
            log.info(f"Pid: {match.group(1)} | Name: {match.group(2)} | Status: {match.group(3)}")

def choice_process():
    print("[1. List Processes]")
    print("[2. Terminate Processes]")
    print("[3. Encerrar]")
    choice = input("Escolha subprocesso a ser iniciado: ")
    return choice

def main():
    list = ["XboxGameBarSpotify.exe", "XboxGameBarWidgets.exe", "OneDriveStandaloneUpdater.exe", "gamingservicesnet.exe", "msedgewebview2.exe", "WidgetService.exe"]
    
    while True:
        user_choice = choice_process()
        
        if user_choice.lower() == "list processes":
            list_processes()   
        elif user_choice.lower() == "terminate processes":
            terminate_processes(list)
        elif user_choice.lower() == "encerrar":
            log.info("Encerrando sistema...")
            break    
        else:
            log.warning("Este processo não existe...")

if __name__ == "__main__":
    main()
