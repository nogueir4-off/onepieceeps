import tweepy
from time import sleep

title = ''
numero = 0
second = 0
minute = 0

auth = tweepy.OAuthHandler('2OUYi5khnoB6ZBMB4YZHKR1Q1',	'xXAyrL27aZyzdsDKIISPoxdxTxEXCVrYzw087OZtOCOMtrfWFT')
auth.set_access_token('1330647738342641666-JvMSvWNZqPoBxdzrx5JUBm3JQcnTyI', 'xIDj4WHICB7eyYiA44QRe1GtFqEXYh7a67K9Fj6zPtkMQ')

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
