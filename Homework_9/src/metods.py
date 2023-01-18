import datetime  
from datetime import datetime
import requests

def welkom(message):
    logger(message)
    hello = ["здравствуйте","здорова","привет","добрый день","здрасте"]
    for h in hello:
        if h in message.text:
            return f"Привет, {message.from_user.first_name}" 
        elif message.text == "погода":
            r = requests.get("https://wttr.in/?0T")
            return r.text          
    
    
def logger(message):
    with open('logger.txt', 'a+', encoding="utf-8") as f:
        f.write(f"{message.from_user.first_name} {message.from_user.last_name} {datetime.now()}: {message.text}\n")

