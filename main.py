import sys
from ui import Menu
from shell_manager import ShellManager
from platform_utils import get_platform_info

def main():
    """
    Основная функция AmnesiaSh. 
    Инициализирует компоненты и управляет главным циклом программы.
    """
    platform_info = get_platform_info()
    manager = ShellManager(platform_info)
    menu = Menu(platform_info)

    print(f"--- Welcome to AmnesiaSh ---")
    print(f"Running on: {platform_info['os_name']}")

    while True:
        # Отображение меню и получение выбора пользователя
        choice = menu.show_and_get_choice()
        
        if choice == 'exit':
            print("Exiting AmnesiaSh. Goodbye!")
            sys.exit(0)
            
        # Запуск выбранной оболочки через менеджер
        manager.launch(choice)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
        sys.exit(0)