import Aircraft.menu.main_menu as main
import Aircraft.config as config

__version__ = config.get_version()

if __name__ == "__main__":
    main.main_menu()