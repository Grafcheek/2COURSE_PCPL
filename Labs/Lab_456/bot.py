import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

# Логирование
logging.basicConfig(level=logging.INFO)

# Токен бота и API-ключ OpenWeatherMap
API_TOKEN = "ВАШ_ТОКЕН_БОТА"
WEATHER_API_KEY = "ВАШ_API_КЛЮЧ"

# Создаем бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Функция для получения погоды
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",  # Для температуры в градусах Цельсия
        "lang": "ru"        # Для описания на русском языке
    }
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        return f"Погода в {name}:\n{weather.capitalize()}\n🌡 Температура: {temp}°C\n🤔 Ощущается как: {feels_like}°C"
    else:
        return "Город не найден. Проверьте название."

# Команда /start
@dp.message_handler(commands=["start"])
async def start_command(message: Message):
    await message.reply("Привет! Напиши название города, чтобы узнать погоду 🌦.")

# Обработчик текстовых сообщений (пользователь вводит город)
@dp.message_handler(Text)
async def send_weather(message: Message):
    city = message.text
    weather = get_weather(city)
    await message.reply(weather)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
