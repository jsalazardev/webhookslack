# Import Libraries
import requests

# set variables globals
pathConfig='../config.ini'
headers = {'Content-Type': 'application/json'}


# functions
def verify_result(response):
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' % (response.status_code, response.text))


def build_message(text, title, footer, status):
    return {
        'attachments': [{
            'color': status,
            'title': title,
            'text': text,
            'footer': footer
        }]
    }

def read_parameters():
  params={}
  config=read_config([pathConfig])
  if(config==None):
    return
  try:
    env=config.get('branch','env')
    url=config.get(env+'.webhook', 'url')
    params={'url':url}
    except configparser.NoSectionError, configparser.NoOptionError:
        print ('Lo parametros indicados no existen')
    return params

def send_message_to_slack(text, title, footer, status):
  params=read_parameters()
  if(config==None):
    print('Lo sentimos, no se encontraron los parametros iniciales')
    return
  slack_data = build_message(text, title, footer, status)
  response = requests.post(webhook_url, json=slack_data, headers=headers)
  verify_result(response)
