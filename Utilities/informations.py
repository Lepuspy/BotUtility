#-*-coding:utf-8-*-
import json
import requests


class Discord:

    def __init__(self,url,name=None,icon=None):
        self.name = name
        self.webhock_url = url
        self.icon_url = icon

    def send(self,message):
        data = json.dumps({"content":message, "username":self.name, "avatar_url":self.icon_url})
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.webhock_url, data=data, headers=headers)
        print(r)
        if r.status_code == 204:
            print("正常に送信しました")
        elif r.status_code == 404:
            raise RuntimeError("指定URLは存在しません")


class Line:
    
    def __init__(self,token):
        self.line_token = token
        self.line_notify_api ='https://notify-api.line.me/api/notify'

    def send(self,message):
        payload={'message': message}
        headers={'Authorization':'Bearer '+ self.line_token}  # 発行したトークン
        r = requests.post(self.line_notify_api, data=payload, headers=headers)
        if r.status_code == requests.codes.ok:
            print("正常に送信しました")
        elif r.status_code == 400:
            raise RuntimeError("リクエスト内容が間違っています")
        elif r.status_code == 401:
            raise RuntimeError("指定トークンは存在しません")
        elif r.status_code == 500:
            raise RuntimeError("Lineサーバーエラーにより失敗")
        else:
            print("予期せぬレスポンス :" + r.status_code)

if __name__ == '__main__':
    url = "WebHockURL"
    d = Discord(url=url,name="test")
    d.send("これはテストです")

    l = Line("Lineトークン")
    l.send("テスト")