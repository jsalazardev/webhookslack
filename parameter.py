import configparser

def read_config():
  config = configparser.ConfigParser()
  config.read("config.ini")
  apple = config.get('dev.webhook',  'url')
  
  try:
    apple = config.get('dev.webhook',  'url')
  except configparser.NoSectionError, configparser.NoOptionError:
    apple = None
  if(apple==None):
    print('ninguna')
    return
  print(apple)

read_config()