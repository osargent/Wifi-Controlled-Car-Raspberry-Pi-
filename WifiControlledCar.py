import tweepy 
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)


 

consumer_key = "VUoETm5AMuJTM5WBjDsCrSEPF" 

consumer_secret = "r8yhwjtga4U02zvTcztBvz0wGpwi4PHEVXBEXokPTYUdhBeUpY" 

access_token = "1475976528706031620-gdM1lmxaNjLKyahwWM66avwzKbAHdH" 

access_token_secret = "8cZ7MbGXAsOo6lPzTd2wc1u4UCpavTeXam71aYX2uRQIC" 

 
 

# Subclass Stream to print IDs of Tweets received 

class IDPrinter(tweepy.Stream): 

 
 

    def on_status(self, status): 

        print(status.text) 

        if status.text == 'up1' + ' #hopefullynoonehasusedthishashtagyet123': 

            while True:
                if GPIO.input(25):
                    GPIO.output(18, False)
                else:
                    GPIO.output(18, True) 

 
 

# Initialize instance of the subclass 

printer = IDPrinter( 

  consumer_key, consumer_secret, 

  access_token, access_token_secret 

) 

 
 

# Filter realtime Tweets by keyword 

printer.filter(track=["#hopefullynoonehasusedthishashtagyet123"]) 

 
 

 
