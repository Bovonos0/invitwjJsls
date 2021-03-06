from .lib import invite_community
import json
import amino

client=amino.Client()
clientx=invite_community
email='kanimetoon4455@gmail.com'
password='123abcd#@!alisadiq2007'
deviceId='0190F50468220B12A108EB49262156E90E7291C585A1B41B561569A43310F22A349DAAE35184D703B3'
client.login(email=email, password=password)


users=client.get_all_users(start=0, size=26)
usersId=users.profile.userId

clientx.login_vc(email=email, password=password, deviceId=deviceId)
sid=clientx.response['sid']
sid='sid='+sid

comId='x113944376'
chatId='78675aa6-8757-4962-9fd3-4a85751f2258'
userId='98056205-d9f2-4622-a10a-41ed63b82765'

clientx.invite_to_voice_chat(sid=sid, deviceId=deviceId,comId=comId, chatId=chatId, userId=userId)
print (clientx.response)
