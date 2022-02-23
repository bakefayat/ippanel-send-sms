from core import RestUrl

sender = "+983000505"
receivers = ["+989371304458", ]
message_text = "متن تست"

url = RestUrl()
response = url.post_request_to_url(sender, receivers, message_text)
print(response)
