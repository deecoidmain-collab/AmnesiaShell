import sys

class CustomShell:
    """
    Внутренняя реализация оболочки AmnesiaSh. 
    Используется при ошибках системных оболочек или по выбору пользователя.
    """
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True
        print("\n--- AmnesiaSh Internal Shell ---")
        print("Type 'help' for available commands.")

        while self.running:
            try:
                # Чтение ввода пользователя
                user_input = input("AmnesiaSh> ").strip().lower()
                
                if not user_input:
                    continue
                
                self._execute(user_input)
            except EOFError:
                break
            except Exception as e:
                print(f"Internal error: {e}")

    def _execute(self, command):
        """
        Парсинг и выполнение встроенных команд.
        """
        if command == "exit":
            self.running = False
        elif command == "help":
            print("\nAvailable internal commands:")
            print("  help  - Show this message")
            print("  beep  - Trigger a system notification (visual)")
            print("  exit  - Return to the main menu")
        elif command == "beep":
            # Визуальный сигнал, так как звуковой может не работать в терминале
            print("\n* BEEP! * (System Bell Triggered)")
        else:
            print(f"Unknown command: '{command}'. Type 'help' for info.")