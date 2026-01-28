import subprocess
import sys
from custom_shell import CustomShell

class ShellManager:
    """
    Класс для управления жизненным циклом дочерних процессов оболочек.
    """
    def __init__(self, platform_info):
        self.platform_info = platform_info
        self.internal_shell = CustomShell()

    def launch(self, shell_id):
        """
        Запускает выбранную оболочку. Если запуск невозможен, 
        автоматически переключается на внутреннюю оболочку.
        """
        if shell_id == "custom":
            self.internal_shell.run()
            return

        # Словарь соответствия ID и системных команд
        commands = {
            "bash": ["bash"],
            "cmd": ["cmd.exe"],
            "powershell": ["powershell.exe"],
            "wsl": ["wsl"]
        }

        cmd = commands.get(shell_id)
        if not cmd:
            print(f"Error: Unknown shell ID '{shell_id}'. Falling back...")
            self.internal_shell.run()
            return

        try:
            # Запуск системной оболочки как подпроцесса
            # shell=True не используется из соображений безопасности и специфики запуска бинарников
            process = subprocess.run(cmd)
            
            # После завершения работы оболочки возвращаемся в меню
            print(f"\nShell '{shell_id}' terminated with exit code {process.returncode}")
            
        except Exception as e:
            print(f"\n[!] Failed to launch {shell_id}: {e}")
            print("[!] Falling back to AmnesiaSh Internal Shell...")
            self.internal_shell.run()