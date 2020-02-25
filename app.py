import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
#ine_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
line_bot_api = LineBotApi('xcTiSWI3r5IAOSrn50X/aDiiDIThWFVqyVcEiqAzFSp7atje0zq8LVHW8McV9bd9UIem51c5CB9kt/RiReNSj+E3IfK8xFD8wA68NtR4WlO85l8CcQ8okBLvcPp5Ep/0jIivxDXygBH5Unza7+EbawdB04t89/1O/w1cDnyilFU=')

# Channel Secret
#handler = WebhookHandler('YOUR_CHANNEL_SECRET')
handler = WebhookHandler('29f6ab323f3b1509dbe58f5c1dfca946')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)