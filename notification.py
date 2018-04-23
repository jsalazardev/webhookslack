#!/usr/bin/env python2.7
# Import Libraries
import fire
from module.webHook import send_message_to_slack

class Notification(object):

    def __init__(self, text, footer='', title='', status='good'):
        self._text=text
        self._footer=footer
        self._title=title
        self._status=status

    def deploy(self):
        params={
            'text':self._text,
            'title':'Notification Deploy' if self._title == '' else self._title,
            'footer':'Instance {footer} '.format(footer='dev' if self._footer == '' else self._footer),
            'status':self._status
        }
        send_message_to_slack(**params)

    def pull_request(self):
        params = {
            'text': self._text,
            'title': 'Notification Pull-Request' if self._title == '' else self._title,
            'footer': 'Merge {footer} '.format(footer='dev' if self._footer == '' else self._footer),
            'status': self._status
        }
        send_message_to_slack(**params)

    def notification(self):
        params = {
            'text': self._text,
            'title': 'Notification ' if self._title == '' else self._title,
            'footer': '{footer} '.format(footer='' if self._footer == '' else self._footer),
            'status': self._status
        }
        send_message_to_slack(**params)

if __name__ == '__main__':
  fire.Fire(Notification)