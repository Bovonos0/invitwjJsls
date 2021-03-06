import invite_community
import json
import amino

client=amino.Client()
clientx=invite_community
email=input ('Email: ')
password=input ('Password: ')
deviceId=input ('DeviseId: ')
client.login(email=email, password=password)

comId=input ('comId: ')
chatId=input('chatId')

value = input ('How Much You Want To invite: ')

users=client.get_all_users(start=0, size=value)
usersId=users.profile.userId

clientx.login_vc(email=email, password=password, deviceId=deviceId)
sid=clientx.response['sid']
sid='sid='+sid



for userId in usersId:
	clientx.invite_to_voice_chat(sid=sid, deviceId=deviceId,comId=comId, chatId=chatId, userId=userId)
	print ('Invited')
