class Menu:
    """
    Отвечает за отображение интерфейса выбора оболочки.
    """
    def __init__(self, platform_info):
        self.platform_info = platform_info

    def show_and_get_choice(self):
        """
        Выводит меню и проверяет ввод пользователя.
        """
        while True:
            print("\n" + "="*30)
            print(" AmnesiaSh - Shell Launcher")
            print("="*30)
            
            shells = self.platform_info["available_shells"]
            
            for i, shell in enumerate(shells, 1):
                print(f"{i}. {shell['name']}")
            
            print(f"{len(shells) + 1}. Exit")
            print("-" * 30)
            
            try:
                user_input = input(f"Select shell (1-{len(shells) + 1}): ")
                index = int(user_input) - 1
                
                # Проверка на выход
                if index == len(shells):
                    return "exit"
                
                # Проверка корректности индекса
                if 0 <= index < len(shells):
                    return shells[index]["id"]
                else:
                    print(f"Please enter a number between 1 and {len(shells) + 1}.")
            
            except ValueError:
                print("Invalid input. Please enter a number.")