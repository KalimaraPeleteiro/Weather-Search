from tkinter import Tk, Entry, Label, Button
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


def city_search(city):
    options = Options()
    options.headless = True  # Evita o navegador de aparecer

    browser = Firefox(options=options)

    city.replace(' ', '+')
    city_link = f'https://www.google.com/search?channel=fs&client=ubuntu&q={city}+clima'

    browser.get(city_link)

    temperatura = browser.find_element(by='id', value='wob_tm')
    chuva = browser.find_element(by='id', value='wob_pp')
    umidade = browser.find_element(by='id', value='wob_hm')
    vento = browser.find_element(by='id', value='wob_ws')

    return temperatura.text, chuva.text, umidade.text, vento.text


def weather_search():
    city = entry_input.get()
    temperature, rain, umidity, wind = city_search(city)

    temperature_label['text'] = f'Temperatura = {temperature}°C'
    rain_label['text'] = f'Chance de Chuva = {rain}'
    umidity_label['text'] = f'Umidade = {umidity}'
    wind_label['text'] = f'Força do Vento = {wind}'


window = Tk()
window.resizable(False, False)
window.title('Weather Search')

Label(window, font=('FreeSerif', 20), text='Qual a cidade que deseja buscar?',
      padx=15, pady=15).pack()

entry_input = Entry(window, font=('FreeSerif', 14), justify='center', width=30)
entry_input.pack()

Button(window, font=('FreeSerif', 16), text='BUSCAR', command=weather_search,
       padx=5, pady=10).pack(pady=10)

temperature_label = Label(window, font=('FreeSerif', 14), text='Temperatura = ?',
                          padx=15, pady=15)
temperature_label.pack()
rain_label = Label(window, font=('FreeSerif', 14), text='Chance de Chuva = ?',
                          padx=15, pady=15)
rain_label.pack()
umidity_label = Label(window, font=('FreeSerif', 14), text='Umidade = ?',
                          padx=15, pady=15)
umidity_label.pack()
wind_label = Label(window, font=('FreeSerif', 14), text='Força do Vento = ?',
                          padx=15, pady=15)
wind_label.pack()

window.mainloop()
