# Import Libraries
import requests
import configparser
from module.readConfig import read_config

# set variables globals
pathConfig = 'module/config.ini'
headers = {'Content-Type': 'application/json'}


# functions
def verify_result(response):
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))


def build_message(text, title, footer, status, username,field):
    return {
        'username': username,
        'attachments': [{
            'color': status,
            'title': title,
            'text': text,
            'fields': '' if field=='' else field,
            'footer': footer
        }]
    }


def read_parameters():
    params = None
    config = read_config(pathConfig)
    if config is None:
        return params
    try:
        env = config.get('branch', 'env')
        url = config.get(env+'.webhook', 'url')
        params = {
            'url': url
        }
    except configparser.NoSectionError, configparser.NoOptionError:
        print ('Lo parametros indicados no existen')
    return params


def send_message_to_slack(text, title, footer, status, username, field):
    params = read_parameters()
    if params is None:
        print('Lo sentimos, no se encontraron los parametros iniciales')
        return
    slack_data = build_message(text, title, footer, status, username, field)
    response = requests.post(params['url'], json=slack_data, headers=headers)
    verify_result(response)
