import functions

def main():
    print("! AUTO-BOOST INICIADO !")
    config = functions.get_config()
    functions.get_ls(config)


if __name__ == "__main__":
    main()