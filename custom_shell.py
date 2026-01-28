class InternalCommands:
    """
    Обработчик встроенных команд AmnesiaSh.
    """
    def __init__(self, logger):
        self.log = logger

    def execute(self, cmd_name, args):
        if cmd_name == "help":
            self._show_help()
        elif cmd_name == "beep":
            print("\a") # Системный звук
            self.log.info("Visual Beep: *BEEP*")
        else:
            self.log.error(f"Unknown command '{cmd_name}'", 
                           reason="Use 'use <shell> <cmd>' or see 'help'")

    def _show_help(self):
        print("\n--- AmnesiaSh Help ---")
        print("Usage:")
        print("  use <shell> <command>  - Execute command in specific shell")
        print("  Example: use bash ls -la")
        print("  Example: use ps Get-Process")
        print("\nSupported Shell IDs: bash, cmd, powershell (ps), wsl")
        print("\nInternal Commands:")
        print("  help - Show this help")
        print("  beep - System bell")
        print("  exit - Close application")