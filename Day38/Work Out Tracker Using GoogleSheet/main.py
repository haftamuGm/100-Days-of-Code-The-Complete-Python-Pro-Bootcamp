import requests
import datetime
import os
APP_ID=os.environ.get("APP_ID")
APP_KEY=os.environ.get("APP_KEY")
MY_URL="https://trackapi.nutritionix.com/v2/natural/exercise"
My_SHEET_URL=os.environ.get("MY_SHEET_URL")
USER_NAME=os.environ.get("USER_NAME")
PASSWORD=os.environ.get("PASSWORD")
header={

"x-app-key":APP_KEY,
"x-app-id":APP_ID,
}
parameter={
    "query":input()
}
post=requests.post(MY_URL,json=parameter,headers=header)
data=post.json()["exercises"][0]
today=datetime.datetime.now()
work_out_parameter={
    "workout":{
    "date":today.strftime("%Y-%m-%d"),
    "time":today.strftime("%H:%M:%S"),
    "exercise":data["user_input"].title(),
    "duration":data["duration_min"],
    "calories":data["nf_calories"],
    }
 }

headers= {
    "Authorization":"Basic aGFmdGFtdTc6SGdAMTkxODIx"
}


pushed=requests.post(My_SHEET_URL,json=work_out_parameter,headers=headers,auth=(USER_NAME,PASSWORD))
print(pushed.json())





