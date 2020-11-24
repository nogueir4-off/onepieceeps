import tweepy
from boto.s3.connection import S3Connection
from time import sleep

title = ''
numero = 0
second = 0
minute = 0

apikey = S3Connection(os.environ['APIKEY'])
secretkey = S3Connection(os.environ['SECRETKEY'])
token = S3Connection(os.environ['TOKEN'])
secrettoken = S3Connection(os.environ['SECRETTOKEN'])

auth = tweepy.OAuthHandler(apikey, secretkey)
auth.set_access_token(token, secrettoken)

api = tweepy.API(auth, wait_on_rate_limit=True)

def episode():
	global numero
	numero += 1
	return f'frames/HorribleSubs One Piece 483 1080p {str(numero).zfill(4)}.jpg'

def timeEpisode():
	def returnSec():
		global second
		global minute
		second += 1
		if second == 60:
			minute += 1
			second = 0
		if minute == 24 and second > 0: 
			numero = 0
			minute = 0
			second = 0
		return second

	second = returnSec()
	return (f"""
ㅤㅤ 👒
        😁 GOMU GOMU NOO
        🦺 ========🤜
        🩳  time - {str(int(minute)).zfill(2)}:{str(second).zfill(2)}
       // \\\\
	""")

def public():
	api.update_with_media(f'{episode()}', status=f'{timeEpisode()}')

if __name__ == "__main__":
	try:
		while True:
			public();
			sleep(180)
	except Exception as e:
		print(e)
