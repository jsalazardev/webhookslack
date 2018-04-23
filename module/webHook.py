# Import Libraries
import requests

# set variables globals
webhook_url = 'https://hooks.slack.com/services/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'
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


def send_message_to_slack(text, title, footer, status):
    slack_data = build_message(text, title, footer, status)
    response = requests.post(webhook_url, json=slack_data, headers=headers)
    verify_result(response)