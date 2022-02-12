import json
import requests

TOKEN = "1985514256:AAEVLLoHdDTDPOPqAq5U-H5wXDn469QYJ6s"
URL = "https://api.telegram.org/bot{[/".format(TOKEN)

#This function get take api.telegram url
def get_url(url):
	response = requests.get(url)
	content = response.content.decode("utf8")
	return content
#not description
def get_json_from_url(url):
	content = get_url(url)
	js = json.loads(content)
	return js
#funstiocreates the necessary link for "api-getupdates"
def get_updates():
	url = URL + "getupdates"
	js = get_json_from_url(URL)
	return js
#function can watch last message
def get_last_chat_id_and_text(updates):
	num_updates = len(updates["result"])
	last_update = num_updates - 1
	text = updates["result"][last_update]["message"]["chat"]["id"]
	chat_id = updates["results"][last_updates]["message"]["chat"]["id"]
	return (text, chat_id)

#
def send_message(text, chat_id):
	url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
	get_url(url)

text chat = get_last_chat_id_and_text(get_updates())
send_message(text, chat)
