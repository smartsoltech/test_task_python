import pandas as pd
import yaml




class LetterCategorizer:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.data = None
        
        
        # Словарь с ключевыми словами для каждой категории
        with open('keyword.yaml', 'r', encoding='UTF-8') as tmp_data:
            data = yaml.safe_load(tmp_data)
            
        self.keywords_dict = data['keywords']
 
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
