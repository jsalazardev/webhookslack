#!/usr/bin/env python2.7
# Import Libraries
import fire
import module.User

class IngestionStage(object):

  def run(self):
    return 'Ingesting! Nom nom nom...'

class DigestionStage(object):

  def run(self, volume=1):
    return ' '.join(['Burp!'] * volume)

  def status(self):
    return 'Satiated.'

class Menu(object):

  def __init__(self):
    self.user = User()
    self.digestion = DigestionStage()
    
  def listUsers():
    self.user.list()

if __name__ == '__main__':
  fire.Fire(Menu)
