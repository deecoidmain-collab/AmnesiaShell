import sys
from shell_manager import ShellManager
from platform_utils import get_platform_info
from logger import Logger

def main():
    """
    Точка входа AmnesiaSh. 
    Инициализирует систему и запускает интерактивный режим команд.
    """
    platform_info = get_platform_info()
    log = Logger()
    manager = ShellManager(platform_info, log)

    log.info(f"AmnesiaSh v2.0 started on {platform_info['os_name']}")
    log.info("Type 'help' for commands or 'use <shell> <cmd>' to execute.")

    while True:
        try:
            # Чтение основной команды
            user_input = input("\nAmnesiaSh> ").strip()
            
            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                log.info("Exiting AmnesiaSh...")
                break

            # Обработка команды через менеджер
            manager.process_input(user_input)

        except KeyboardInterrupt:
            print("\n")
            log.info("Use 'exit' to quit safely.")
        except Exception as e:
            log.error(f"Unexpected system error: {e}")

if __name__ == "__main__":
    main()