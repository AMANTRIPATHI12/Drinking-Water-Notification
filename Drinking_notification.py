import time
from plyer import notification

if __name__ == '__main__':
	while True:
		notification.notify(
			title = "Please Drink Water Now...",
			message ="Eight Glass of Water a day keeps the doctor away...",
			app_icon = "D:\\Aman\\My Projects\\Drinking Water notification\\icon.ico",
			timeout= 10
			)
		time.sleep(60*30)