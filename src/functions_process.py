import psutil

def close_process(process_name=[]):
    for process in psutil.process_iter():

        try:
            for name in process_name:
                if process.name() == name:
                    process.terminate()
                    print(f"Processo [{process.name()}] encerrado com sucesso.")

        except (psutil.NoSuchProcess,  psutil.ZombieProcess):
            print("Processo não existe mais...")
        except psutil.AccessDenied:
            print("Voce nao tem permissao para encerrar este processo...")

def ls_process():
    for process in psutil.process_iter():
        print(process)

def main():
    list = ["XboxGameBarSpotify.exe", "XboxGameBarWidgets.exe", "OneDriveStandaloneUpdater.exe", "gamingservicesnet.exe", "msedgewebview2.exe", "WidgetService.exe"]
    close_process(list)

if __name__ == "__main__":
    main()
