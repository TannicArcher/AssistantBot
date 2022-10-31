import asyncio
import requests
from time import sleep
from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import ImportChatInviteRequest


api_id = 2695662
api_hash = 'b3c0c16ece4b7fb3fb364ca4e4916c8c'

client = TelegramClient('utils\\btc_account', api_id, api_hash, device_model="Iphone", system_version="6.12.0",
                        app_version="10 P (28)")
client.start()

async def pars_bot(link):
	#client.send_message('me', f'парс чата {link}')
	
	chats = []
	last_date = None
	chunk_size = 200
	groups = []

	if 'https://t.me/joinchat/' in link:
		links = link.split('/')[4]
		update = await  client(ImportChatInviteRequest(links))
	elif 'https://t.me/' in link:
		links = link.split('/')[3]
	else:
		links = link

	all_participants = []
	all_participants = await client.get_participants(link, aggressive=True)
	#print(all_participants)


	t = open(f'docs\\chat_{links}.txt', 'w+') 
	for i in all_participants:
		if i.username != None:
			username = i.username
			t.write( username + '\n')



def parser(link):
        client.loop.run_until_complete(pars_bot(link))
