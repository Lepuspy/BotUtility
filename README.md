# BotUtility
仮想通貨のBOT Dev向け便利系モジュールです

使い方:
-------------------
pip install pandas　をする
```python
from Utilities import output

log = output.Logs()

# お知らせ
log.Info("test")
# エラーログ
log.Error("test")
```

pip install requests　をする
```python
from Utilities import informations

discord = informations.Discord(url="WebhockURL",name="表示名",icon="アイコンURL")
discord.send("任意のメッセージ")

line = informations.Line("Lineトークン")
line.send("任意のメッセージ")
```
