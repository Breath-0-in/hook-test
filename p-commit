#!/usr/bin/env python

import subprocess
import requests
import json

def send_slack_notification():
    # Slack webhook URL 설정
    slack_webhook_url = 'https://hooks.slack.com/services/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'

    # 커밋 정보 가져오기
    commit_info = subprocess.check_output(['git', 'log', '-1', '--pretty=format:%s by %an']).decode('utf-8')

    # Slack 메시지 포맷
    payload = {
        "text": f"New commit: {commit_info}"
    }

    # Slack으로 메시지 전송
    response = requests.post(slack_webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        print(f"Failed to send Slack notification: {response.status_code} - {response.text}")

if __name__ == "__main__":
    send_slack_notification()
