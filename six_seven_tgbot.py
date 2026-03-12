import time
import requests
import wmi

TOKEN = "yourBotAPI"
CHAT_ID = "YourTelegramID"

c = wmi.WMI()

while True:
    batteries = c.Win32_Battery()

    if batteries:
        level = batteries[0].EstimatedChargeRemaining

        if level == 67:
            url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
            data = {
                "chat_id": CHAT_ID,
                "text": "67 ALERT HEADS UP!"
            }

            requests.post(url, data=data)
            break

    time.sleep(60)
