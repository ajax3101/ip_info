from configparser import InterpolationMissingOptionError
from urllib import request, response
import requests
from pyfiglet import Figlet


def get_info_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        data = {
            '[IP]': response.get('query'),
            '[ISP]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f'{k} : {v}')
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection to Internet!')


def main():
    text = Figlet()
    print(text.renderText('IP INFO'))
    ip = input('Please enter IP: ')

    get_info_ip(ip=ip)


if __name__ == '__main__':
    main()
