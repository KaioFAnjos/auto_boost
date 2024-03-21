import psutil
import log
import re

def terminate_processes(process_name=[]):
    for process in psutil.process_iter():
        try:
            for name in process_name:
                if process.name() == name:
                    process.terminate()
                    log.info(f"Processo [{process.name()}] encerrado com sucesso.")

        except (psutil.NoSuchProcess,  psutil.ZombieProcess):
            log.warning("Processo não existe mais...")
        except psutil.AccessDenied:
            log.warning(f"Processo [{process.name()}] sem permissão para encerrar...")

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
