import time
from src import data

def main():
    covid = data.CovidData(update=None)
    while True:
        print(time.localtime())
        covid.update(type='all')
        time.sleep(3*60*60)  # 3 hours

if __name__ == '__main__':
    main()
