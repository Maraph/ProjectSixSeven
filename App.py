
import yfinance as yf
import requests
import time
import datetime

ticker = 'ALM'

#*******************************************************Manually written conversion rate************************************************
EUR = 1.00
USD = 1.16
current_price = 0.0
Conversion_Rate = EUR/USD#conversion_rate could be gotten from a api 
#*******************************************************Manually written conversion rate************************************************



#*******************************************************Used to send 1 message only*****************************************************
TimeToSend = '00'#could be a scanf 
TempVar = int(TimeToSend)
TimeToRearm = TempVar + 1
TimeToRearm = str(TimeToRearm)
sent = 0
#*******************************************************Used to send 1 message only*****************************************************




#*******************************************************ID of the receiver**************************************************************

#*******************************************************ID of the receiver**************************************************************





while (1) :
    t1 = datetime.datetime.now()
    print("%s" % (t1.minute))#to delete
    time.sleep (1)#to delete 





    #**************************************************Used to send messages***********************************************************
    if (sent == 0) :
        AllowSend = 1
    if (("%s" % (t1.minute)) == TimeToRearm) :
        sent = 0
    if (("%s" % (t1.minute)) == TimeToSend and AllowSend == 1) :
        sent = 1
        AllowSend = 0
        symbol = yf.Ticker(ticker)
        data = symbol.history(period="1d")
        if not data.empty :
            current_price = data['Close'].iloc[0]
            current_price = current_price * Conversion_Rate
            print(current_price)

        token = "a6bmku29c3dgtk7u2pwak17721ab1u"
        user = "ux7rirjnno7dkdn3mv4bcfbaky1ior"
        message = f"The current price of Almonty Stock is : {current_price:.2f}"
            
        resp = requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": token,
                "user": user,
                "message": message
            }
        )
        print(resp.text)
        #**************************************************Used to send messages***********************************************************


# In[ ]:




