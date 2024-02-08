import sqlite3

class Database():
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    #Таблица пользователей
    def create_db(self):
        try:
            query = ("CREATE TABLE IF NOT EXISTS girls("
                     "id INTEGER PRIMARY KEY,"
                     "girl_name TEXT UNIQUE,"
                     "girl_description TEXT UNIQUE,"
                     "link TEXT UNIQUE);")

            query_broadcasts = ("CREATE TABLE IF NOT EXISTS images_girls("
                                "id INTEGER PRIMARY KEY,"
                                "image_id INTEGER,"
                                "image_url TEXT,"
                                "FOREIGN KEY (image_id) REFERENCES girls(id));")
            self.cursor.execute(query)
            self.cursor.execute(query_broadcasts)
            self.connection.commit()
        except sqlite3.Error as error:
            with open('databaseerrors.txt', 'a') as error_file:
                error_message = f"Ошибка при создании базы данных - {error}\n"
                error_file.write(error_message)
            print(f'Ошибка при создании базы данных - {error}')



    # Получаем информацию о девушках

    def get_girls_info(self):
        try:
            query = "SELECT * FROM girls"
            self.cursor.execute(query)
            girls = self.cursor.fetchall()
            return [girl for girl in girls]
        except sqlite3.Error as error:
            with open('databaseerrors.txt', 'a') as error_file:
                error_message = f"Ошибка при попытке получить girls info - {error}\n"
                error_file.write(error_message)
            print(f'Ошибка при попытке получить girls info - {error}')
            return None




    def get_image_path(self, girl_id):
        try:
            query = "SELECT image_url FROM images_girls WHERE image_id = ?;"
            self.cursor.execute(query, (girl_id,))
            result = self.cursor.fetchall()
            return result
        except sqlite3.Error as error:
            with open('databaseerrors.txt', 'a') as error_file:
                error_message = f"Ошибка при попытке получить путь картинки - {error}\n"
                error_file.write(error_message)
            print(f"Ошибка при попытке получить путь картинки - {error}")
            return None




    def __del__(self):
        self.cursor.close()
        self.connection.close()