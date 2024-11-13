import random
from logo import logo,data,vs
print(logo)
a=random.choice(data)
print(f"Compare A :{a['name']} , {a['description'] } From {a['country']}")
score=0
game_end=True
while game_end:
    print(vs)
    b = random.choice(data)
    print(f"Compare B :{b['name']} , {b['description']} From {b['country']}")
    user = input("Who has more followers ?").lower()
    if a['follower_count'] > b['follower_count'] and user == 'a':
        print(logo)
        print(f"Compare A :{a['name']} , {a['description']} From {a['country']}")

        score += 1
    elif b['follower_count'] > a['follower_count'] and user == 'b':
        a=b
        print(f"Compare A :{b['name']} , {b['description']} From {b['country']}")
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score:   {score}")
        game_end = False







