#the work out hour receive by input
import requests
import datetime
MY_URL="https://pixe.la/v1/users"
USER_NAME="haftamu7"
TOKEN="vjkskck3kd3xc7"
ID="hafito7"
new_parameter={
    "token":TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"

}
# result=requests.post(url=MY_URL,json=new_parameter)
create_graph=f"{MY_URL}/{USER_NAME}/graphs"
new_graph_para={
    "id":ID,
    "name":"MyCoding Tracker",
    "unit":"hr",
    "type":"int",
    "color":"ichou"
}
header={
    "X-USER-TOKEN":TOKEN
}
#posted=requests.post(create_graph,json=new_graph_para,headers=header)
today=datetime.datetime.now()
formatted=today.strftime("%Y%m%d")
user=int(input("How Many Hours Did you code today  ?"))

add_pixel_endpoint=f"https://pixe.la/v1/users/{USER_NAME}/graphs/{ID}"
pixel_parameter={
    "date":formatted,
    "quantity":f"{user}",
}
#add_=requests.post(add_pixel_endpoint,json=pixel_parameter,headers=header)
update=f"https://pixe.la/v1/users/{USER_NAME}/graphs/{ID}/{formatted}"
update_pixel={
    "quantity":f"{user}",
}
updated=requests.delete(update,headers=header)
print(updated.text)