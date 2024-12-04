import requests
result=requests.get("https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean")
question_data=result.raise_for_status()
question_data=result.json()["results"]

