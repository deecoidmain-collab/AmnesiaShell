import platform
import os
import shutil

def get_platform_info():
    """
    Определяет текущую ОС и проверяет наличие установленных оболочек.
    Возвращает словарь с системной информацией.
    """
    system = platform.system().lower()
    info = {
        "os_name": system,
        "available_shells": []
    }

    if system == "linux":
        # Для Linux проверяем наличие bash
        if shutil.which("bash"):
            info["available_shells"].append({"id": "bash", "name": "Bash (Linux)"})
            
    elif system == "windows":
        # Для Windows проверяем CMD, PowerShell и WSL
        if shutil.which("cmd.exe"):
            info["available_shells"].append({"id": "cmd", "name": "Windows CMD"})
        
        if shutil.which("powershell.exe"):
            info["available_shells"].append({"id": "powershell", "name": "PowerShell"})
            
        if shutil.which("wsl"):
            info["available_shells"].append({"id": "wsl", "name": "WSL (Windows Subsystem for Linux)"})

    # Кастомная оболочка всегда доступна как fallback
    info["available_shells"].append({"id": "custom", "name": "AmnesiaSh Internal Shell"})
    
    return info