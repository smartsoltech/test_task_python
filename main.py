import pandas as pd

class LetterCategorizer:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
        
        # Словарь с ключевыми словами для каждой категории
        self.keywords_dict = {
            "Security": ["безопасность", "пароль", "взлом", "защита", "подозрительная активность", "код доступа"],
            "Refunds": ["возврат", "возмещение", "отмена", "деньги", "средства", "заказ"],
            "Troubleshooting": ["проблема", "не работает", "ошибка", "падение", "сбой", "зависает"],
            "Account": ["аккаунт", "профиль", "регистрация", "вход", "выход", "доступ"],
            "Advertising and Collaboration": ["реклама", "сотрудничество", "партнерство", "бренд", "продвижение"],
            "Limits": ["лимит", "ограничение", "предел"],
            "Payments": ["оплата", "платеж", "счет", "банковская карта", "транзакция"],
            "Features": ["функционал", "возможность", "функция", "новинка", "опция"]
        }

    def _categorize_letter(self, letter):
        """Категоризация письма на основе ключевых слов."""
        categories = []
        for category, keywords in self.keywords_dict.items():
            for keyword in keywords:
                if keyword in letter.lower():  # учет регистронезависимости
                    categories.append(category)
                    break  # переход к следующей категории после обнаружения ключевого слова
        return ', '.join(categories)

    def load_data(self):
        """Загрузка данных из CSV-файла."""
        self.data = pd.read_csv(self.input_path)
        
    def categorize_data(self):
        """Категоризация всех писем."""
        self.data['Categories'] = self.data[self.data.columns[0]].apply(self._categorize_letter)
        
    def save_results(self):
        """Сохранение результатов в CSV-файл."""
        # Группировка данных по категориям и объединение текстов писем
        grouped_data = self.data.groupby('Categories')[self.data.columns[0]].apply('\n'.join).reset_index()
        grouped_data.columns = ['Category', 'Letters']
        grouped_data.to_csv(self.output_path, index=False)
        
    def run(self):
        """Запуск процесса категоризации."""
        self.load_data()
        self.categorize_data()
        self.save_results()

# Запуск скрипта
if __name__ == "__main__":
    input_path = 'sample.csv'
    output_path = 'result.csv'
    categorizer = LetterCategorizer(input_path, output_path)
    categorizer.run()
