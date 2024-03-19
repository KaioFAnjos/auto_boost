import configparser

config_path = 'C:/ws-python/auto_boost/path/path.ini'

def load_config():
    config = configparser.ConfigParser()
    try:
        with open(config_path, encoding='utf-8') as f:
            config.read_file(f)

        configs = {}

        for section in config.sections():
            for key, value in config.items(section):
                configs[key] = value
        
        return configs
    except FileNotFoundError:
        print(f"Arquivo [{config_path}] não foi encontrado...")
        return {}
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return {}

def get_value(configs, key):    
    return configs[key] if key in configs else print(f"A chave [{key}] nao foi encontrada...")

def main():
    return load_config() 

if __name__ == '__main__':
    dir = 'C:/ws-python/auto_boost/auto_boost/path/path.ini'
    
