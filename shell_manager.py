import subprocess
from custom_shell import InternalCommands

class ShellManager:
    """
    Управляет парсингом команд 'use' и запуском соответствующих оболочек.
    """
    def __init__(self, platform_info, logger):
        self.platform_info = platform_info
        self.log = logger
        self.internal = InternalCommands(logger)

    def process_input(self, user_input):
        """
        Парсит ввод. Если начинается с 'use', направляет в системную оболочку.
        Иначе проверяет внутренние команды.
        """
        parts = user_input.split(maxsplit=2)
        
        if parts[0].lower() == "use" and len(parts) >= 2:
            shell_id = parts[1].lower()
            command = parts[2] if len(parts) > 2 else ""
            self._execute_remote(shell_id, command)
        else:
            # Попытка выполнить как внутреннюю команду (help, beep и т.д.)
            self.internal.execute(parts[0].lower(), parts[1:] if len(parts) > 1 else [])

    def _execute_remote(self, shell_id, command):
        """
        Запуск команды в конкретной системной оболочке.
        """
        # Проверяем, доступна ли оболочка на этой платформе
        available_ids = [s['id'] for s in self.platform_info['available_shells']]
        
        if shell_id not in available_ids:
            self.log.error(f"Shell '{shell_id}' is not supported or missing on this OS.")
            return

        if not command:
            self.log.error(f"No command provided for '{shell_id}'. Example: use {shell_id} whoami")
            return

        # Формирование аргументов запуска
        exec_args = self._get_exec_args(shell_id, command)
        
        try:
            # Выполняем команду и захватываем вывод для логирования
            result = subprocess.run(
                exec_args,
                capture_output=True,
                text=True,
                timeout=30 # Предотвращаем зависание
            )

            if result.returncode == 0:
                self.log.shell_output(shell_id, result.stdout)
            else:
                self.log.error(f"Command failed in {shell_id}", reason=result.stderr.strip())

        except FileNotFoundError:
            self.log.error(f"Could not connect to {shell_id}", reason="Executable not found in PATH")
        except subprocess.TimeoutExpired:
            self.log.error(f"Connection to {shell_id} timed out")
        except Exception as e:
            self.log.error(f"Failed to connect to {shell_id}", reason=str(e))

    def _get_exec_args(self, shell_id, command):
        """
        Подготовка аргументов командной строки для разных оболочек.
        """
        if shell_id == "bash":
            return ["bash", "-c", command]
        elif shell_id == "cmd":
            return ["cmd.exe", "/c", command]
        elif shell_id == "powershell" or shell_id == "ps":
            return ["powershell.exe", "-Command", command]
        elif shell_id == "wsl":
            return ["wsl", "--", "bash", "-c", command]
        return None