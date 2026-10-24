rom http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

# Определяем базовый путь к папке проекта для надежного поиска файлов
BASE_DIR = Path(__file__).resolve().parent

# Настройки запуска из конспекта
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
    Класс, отвечающий за обработку входящих запросов от клиентов.
    """

    def do_GET(self):
        """Метод для обработки входящих GET-запросов."""
        # Путь к HTML-файлу контактов
        file_path = BASE_DIR / "contacts.html"

        # Чтение содержимого файла через with open()
        with open(file_path, "r", encoding="utf-8") as file:
            page_content = file.read()

        # 1. Отправка статуса 200 OK
        self.send_response(200)

        # 2. Замена Content-type с application/json на text/html
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()

        # 3. Отправка содержимого HTML-страницы клиенту
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт сервера в цикле прослушивания
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Корректное освобождение порта при завершении через Ctrl + C
    webServer.server_close()
    print("Server stopped.")