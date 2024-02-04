from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Инициализировать драйвер браузера
driver = webdriver.Chrome()

# Открыть страницу Instagram
driver.get("https://www.instagram.com")

# Пауза для загрузки страницы
time.sleep(3)

# Найти поля для ввода логина и пароля
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

# Ввести логин и пароль
username_input.send_keys("leva.dsgn")
password_input.send_keys("Realartist99")

# Нажать кнопку входа
password_input.send_keys(Keys.ENTER)

# Пауза для завершения авторизации
time.sleep(5)

# Переход на страницу близких друзей
driver.get("https://www.instagram.com/accounts/close_friends/")

# Пауза для загрузки страницы
time.sleep(5)

# Найти и кликнуть по аккаунту с определенным никнеймом
account_to_click = driver.find_element(By.XPATH, "//span[text()='twitchyxpalm']/ancestor::div[@role='button']")
account_to_click.click()

# Пауза для загрузки профиля
time.sleep(3)

# Закрыть браузер после выполнения необходимых действий
driver.quit()
