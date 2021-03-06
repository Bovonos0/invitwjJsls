import requests
import json

def login_vc(email, password, deviceId):
	global response
	headers={'NDC-MSG-SIG':'AWe7V9JF4yRIpQL1WhgoY6ZR9IXV', 'NDCDEVICEID':deviceId, 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G925F Build/MMB29K.G925FXXS4DPH8; com.narvii.amino.master/3.4.33563)'}
	data={'email':email, 'secret':'0 '+password, 'deviceID':deviceId}
	data=json.dumps(data)
	url='http://service.narvii.com/api/v1/g/s/auth/login'
	request=requests.post(url=url, headers=headers, data=data)
	response=json.loads(request.text)

def invite_to_voice_chat(sid, deviceId,comId, chatId, userId):
	global response
	comId=str(comId)
	chatId=str(chatId)
	userId=str(userId)
	headers={'NDCAUTH':sid, 'NDCDEVICEID':deviceId}
	data={'uid':userId}
	data=json.dumps(data)
	url='http://service.narvii.com/api/v1/'+comId+'/s/chat/thread/'+chatId+'/vvchat-presenter/invite'
	request=requests.post(url=url, data=data, headers=headers)
	response=json.loads(request.text)