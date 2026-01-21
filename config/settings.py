import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()


class Config:
    """Конфигурация проекта для автоматизации тестирования API"""

    # ===== Базовые настройки API =====
    BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    API_VERSION = os.getenv("API_VERSION", "")

    # Полный URL API
    API_URL = f"{BASE_URL}{API_VERSION}"

    # ===== Таймауты =====
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", "5"))

    # ===== Логирование =====
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # ===== Настройки отчетов =====
    ALLURE_RESULTS_DIR = os.getenv("ALLURE_RESULTS_DIR", "allure-results")
    HTML_REPORT_DIR = os.getenv("HTML_REPORT_DIR", "reports/html")
    JUNIT_REPORT_DIR = os.getenv("JUNIT_REPORT_DIR", "reports/junit")

    # ===== Настройки тестирования =====
    TEST_RETRIES = int(os.getenv("TEST_RETRIES", "1"))
    TEST_PARALLEL_WORKERS = int(os.getenv("TEST_PARALLEL_WORKERS", "1"))

    # ===== Режимы выполнения =====
    HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
    VERBOSE = os.getenv("VERBOSE", "False").lower() == "true"

    # ===== Безопасность =====
    API_KEY = os.getenv("API_KEY", "")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN", "")

    # ===== Пользовательские заголовки =====
    @staticmethod
    def get_headers() -> dict:
        """Возвращает стандартные заголовки для запросов"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "API-Automation-Framework/1.0"
        }

        # Добавляем авторизацию если есть токен или API ключ
        if Config.AUTH_TOKEN:
            headers["Authorization"] = f"Bearer {Config.AUTH_TOKEN}"
        elif Config.API_KEY:
            headers["X-API-Key"] = Config.API_KEY

        return headers


# Создаём экземпляр конфигурации для импорта
config = Config()