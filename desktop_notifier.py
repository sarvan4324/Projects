from plyer import notification
import time
#import requests



if __name__=="__main__":
    #data=requests.get("https://www.google.com/search?q=live+cricket+score&rlz=1C1ONGR_enIN1046IN1046&oq=&aqs=chrome.0.35i39i362l8.229853245j0j15&sourceid=chrome&ie=UTF-8#sie=m;/g/11k3qpvm5_;5;/m/021q23;dt;fp;1;;")
    notification.notify(title="WATER TIME",message="its time to have some water sarvan......\ndont think anything go right now",
                        app_icon="C:/Users/sarva/Downloads/Bottle_of_Water_icon-icons.com_68778.ico",
                        app_name="Water Notifier",
                        timeout=5,toast=False,ticker=False)
    