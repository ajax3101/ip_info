# Информация по IP адресу
[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
По IP адресу пользователя с помощью Python и библиотеки requests получаем страну, регион, город, почтовый индекс, провайдера и даже широту и долготу. 
Красивое превью используем модуль Figlet, а также сохраним карту по координатам с помощью модуля folium.

## Running the Project Locally

First, clone the repository to your local machine:
```bash
$ git clone https://github.com/ajax3101/ip_info.git
$ cd ip_info/
```
Install the requirements:
```bash
$ python -m venv venv
```
The use of venv is now recommended for creating virtual environments: 
Platform POSIX
```bash
$ source <venv>/bin/activate
```
or
Platform Windows
```bash
PS .\venv\Scripts\Activate.ps1
```
To install the package run the following command:
```bash
$ pip install -r requirements.txt
$ python main.py
```