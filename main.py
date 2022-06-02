from urllib import request, response
import requests


def get_info_ip (ip='127.0.0.1'):
    try:
        response = requests.get(url='http://ip-api.com/json/{ip}').json()
        print(response)
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection to Internet!')


def main():
    ip = input('Please enter IP: ')

    get_info_ip(ip=ip)


if __name__ == '__main__':
    main()
