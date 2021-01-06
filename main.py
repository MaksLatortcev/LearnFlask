# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from flask import Flask    # сперва подключим модуль

app = Flask(__name__)      # объявим экземпляр фласка

@app.route('/')            # объявим путь /
def hello():               # объявим функцию для пути /
  return 'Hello, World!'   # выведем текст, который будет при обращении на /

app.run('0.0.0.0',8000)    # запустим сервер на 8000 порту!


