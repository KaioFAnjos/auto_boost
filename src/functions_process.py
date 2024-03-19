import psutil
import log
def close_process(process_name=[]):
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

def ls_process():
    for process in psutil.process_iter():
        print(process)

def main():
    print("\tINICIANDO CLEAR PROCESS")
    list = ["XboxGameBarSpotify.exe", "XboxGameBarWidgets.exe", "OneDriveStandaloneUpdater.exe", "gamingservicesnet.exe", "msedgewebview2.exe", "WidgetService.exe"]
    close_process(list)

if __name__ == "__main__":
    main()
