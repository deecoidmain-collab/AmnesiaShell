import datetime

class Logger:
    """
    Класс для унифицированного вывода сообщений, ошибок и системных логов.
    """
    def info(self, message):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[*] [{timestamp}] {message}")

    def error(self, message, reason=None):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        error_msg = f"[!] [{timestamp}] ERROR: {message}"
        if reason:
            error_msg += f" | Reason: {reason}"
        print(error_msg)

    def shell_output(self, shell_name, output):
        print(f"--- {shell_name.upper()} OUTPUT ---")
        if output:
            print(output.strip())
        print(f"--- END OF {shell_name.upper()} ---")