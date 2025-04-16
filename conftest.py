import os
import zipfile
import pytest

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
RESOURCES_DIR = os.path.join(CURRENT_DIRECTORY, 'resources') # делаем склейку пути к текущей директории и папки resources
FILES_DIR = os.path.join(CURRENT_DIRECTORY, 'files') # делаем склейку пути к текущей директории и папки files



@pytest.fixture(scope="session", autouse=True)
def create_archive():
    if not os.path.exists(RESOURCES_DIR):  # проверяем существует ли папка
        os.mkdir(RESOURCES_DIR)  # создаем папку если её нет
    archive_path = os.path.join(RESOURCES_DIR, 'project_archive.zip')
    with zipfile.ZipFile(archive_path, 'w') as zf:  # создаем архив
        for file in ['Programming Language.xlsx', 'Python or Go.pdf', 'Mock data.csv']:  # добавляем файлы в архив
            add_file = os.path.join(FILES_DIR, file)  # склеиваем путь к файлам которые добавляют в архив
            zf.write(add_file, os.path.basename(add_file))  # добавляем файл в архив
    yield

    # Удаление архива после завершения тестов
    if os.path.exists(archive_path):  # проверяем, существует ли архив
        os.remove(archive_path)
        print(f"\nАрхив удален: {archive_path}")
    else:
        print(f"\nАрхив не найден: {archive_path}")
