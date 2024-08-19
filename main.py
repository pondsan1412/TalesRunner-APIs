from fastapi import FastAPI, APIRouter, Query
from typing import Optional

app = FastAPI(
    description='TalesRunner APIs related to fastapi'
)

router = APIRouter()

characters = [
    {
        "id": 1,
        "name": "Charlie",
        "original_name": "Chowon",
        "thai_name": "โชวอน",
        "description": """
Character Information
Charlie, dubbed "The Athlete", is a very active person who is a natural born leader. He is the local leader of his neighborhood gang. Charlie excels in every sports that he participates in. Although a bit short for his age, Charlie is still a growing boy. Everyone likes Charlie and he attracts a lot of friends. Charlie also likes to joke around and play pranks on people. He is the most balanced person in terms of running abilities. Charlie has neither any strong strengths nor weaknesses.

In the Tales Runner Tournament, Charlie will do very well in all the maps if he gets some nice equipments. Because Charlie is well rounded and balanced in his stats, Charlie will do very well in the Tournament with the help of a good partner. His best compatibility in terms of relationship is with Ming Ming.

A healthy and cheerful little sportsman who loves to run.

He is the leader of the neighborhood and has many friends around him.

In other releases of Tales Runner, this character is called Chowon, Kwong Kwong, or Jaka. In the OGPlanet release of Tales Runner, this character is called Billy.

Charlie has no wish to fulfill using the wish stone and had become a tales runner simply because he enjoys running.

Charlie has balanced stats with no significant weaknesses which makes it suitable for new players and for general racing. Later into the game its lower sum of stat points (12) and lack of strong stats may become limiting.

Charlie's Max Speed and Control stats were updated from 3 to 4.

In the Korean release of Tales Runner Charlie's character model was renewed as part of the February 15, 2017 update.

Other Details
He is 1 of 4 starting characters you can use when starting Tales Runner (Gpotato)
Purchase Price - 30,000 TR (Gpotato)
Once purchased, he is a permanent character in your My Room.
""",
        "appearance":"""
Charlie appearance as a young slim child. He has brown shaggy hair and azure eyes. He is wearing a blue t-shirt and a white long sleeve shirt underneath. He also wears white shorts and a flip flops with the caption TR in blue.

In February 15, 2017 Charlie's character model was renewed. According to her new model design, he still has the same hair design and his style of eyes changed a bit. Now he wears a jeans jacket and white t-shirt underneath. He also wears denim bermuda shorts and some blue boots.
""",
        "age": 11,
        "type": "human",
        "height": "4.7ft (140cm)",
        "weight": "77 lbs (35kg)",
        "bloodtype": "0",
        "birthdate": "May 2",
        "Occupation": "Elementary School Athletic Team Member",
        "Origin": "Korea",
        "Wish": None,
        "speed": 3,
        "acceleration": 3,
        "force": 3,
        "control": 3,
        "special": False,
        "image_url": "https://static.wikia.nocookie.net/talesrunner-sg/images/c/c9/Charlie.png/revision/latest?cb=20140101024429",
        "price": 10000,
        "starting_character": True,
        "releasedate": "July 29, 2005",
    },
    {
        "id": 2,
        "name": "Ming Ming",
        "thai_name": "หมิง หมิง",
        "original_name": None,
        "description": """
Ming Ming, dubbed "The Movie Star", has a very bubbly personality. She has been a child actress since you were born. Because of this "Rich and Famous" lifestyle, she has become a bit of a spoiled brat. Ming Ming takes great pride in her heritage and she loves to play around. As a very proud person, she sometimes has a hard time in expressing her feelings especially towards Charlie, the boy that she likes. Sometimes this can lead to her appearing to be kind of mean and a bully. In terms of running abilities, Ming Ming is very similar to Charlie. She are fairly balanced. In comparison to Charlie, she has a bit more Control and a little less Power.

In the Tales Runner Tournament, like Charlie, if Ming Ming gets some nice equipment, she will be able to do well in any map. With the addition of a bit more Control, at high speeds such as when using Dash Potions or Boots of Speed, she will be able to have a bit more control. However, her Power is not very good which means she will be pushed and bamped pretty often in a race. Her best compatibility in terms of relationship is with Charlie.

She's bright, unpretentious, and adorable. She's a bit of a star from a young age, so she has a bit of an attitude.

Ming Ming is very similar to Charlie, and only differs in sacrificing one Power for Control. As a balanced character it is also suitable for beginners. Later into the game its lower sum of stat points (12) and overall stats distribution may become limiting.

Ming Ming's Max Speed was updated from 3 to 4, and her Power stat was updated from 2 to 3.

In the Korean release of Tales Runner Ming Ming's character model was renewed as part of the February 15, 2017 update.
                """,
        "age": 10,
        "type": "human",
        "height": "4.3ft (130cm)",
        "bloodtype": "B",
        "birthdate": "July 29",
        "occupation": "to be Movie Star",
        "origin": "China",
        "wish": "To become an adult quickly in order to get more movie roles",
        "speed": 3,
        "acceleration": 3,
        "power": 3,
        "control": 4,
        "special": False,
        "image_url": "https://talesrunner.fandom.com/wiki/File:MingMing4.gif",
        "price": 10000,
        "starting_character": True,
        "releasedate": "July 29, 2005",
    }
]

@router.get("/")
async def root():
    return {
        "data": [
            {
                "APIs info": [
                    {
                        "name": "TalesRunner API",
                        "description": "This is an API for TalesRunner",
                        "version": "0.1.0",
                        "Docs": "https://satorn.vercel.app/docs",
                    }
                ],
                "Developer info": [
                    {
                        "author": "Satorn Sukkang",
                        "email": "pondforbusiness@gmail.com",
                        "github": "https://github.com/pondsan1412",
                        "facebook": "https://www.facebook.com/pondcomp",
                        "website": "https://satorn.vercel.app",
                    }
                ],
            }
        ]
    }

@router.get("/character")
async def get_character(
    id: Optional[int] = None,
    name: Optional[str] = None,
    original_name: Optional[str] = None,
    age: Optional[int] = None,
    type: Optional[str] = None,
    height: Optional[str] = None,
    weight: Optional[str] = None,
    bloodtype: Optional[str] = None,
    birthdate: Optional[str] = None,
    occupation: Optional[str] = None,
    origin: Optional[str] = None,
    wish: Optional[str] = None,
    speed: Optional[int] = None,
    acceleration: Optional[int] = None,
    force: Optional[int] = None,
    control: Optional[int] = None,
    special: Optional[bool] = None,
    starting_character: Optional[bool] = None,
    releasedate: Optional[str] = None,
    price: Optional[int] = None
):
    filtered_characters = [
        char for char in characters if
        (id is None or char["id"] == id) and
        (name is None or char["name"].lower() == name.lower()) and
        (original_name is None or char["original_name"] and char["original_name"].lower() == original_name.lower()) and
        
        (age is None or char["age"] == age) and
        (type is None or char["type"].lower() == type.lower()) and
        (height is None or char["height"].lower() == height.lower()) and
        (weight is None or char["weight"].lower() == weight.lower()) and
        (bloodtype is None or char["bloodtype"].lower() == bloodtype.lower()) and
        (birthdate is None or char["birthdate"].lower() == birthdate.lower()) and
        (occupation is None or char["Occupation"].lower() == occupation.lower()) and
        (origin is None or char["Origin"].lower() == origin.lower()) and
        (wish is None or char["Wish"] and char["Wish"].lower() == wish.lower()) and
        (speed is None or char["speed"] == speed) and
        (acceleration is None or char["acceleration"] == acceleration) and
        (force is None or char["force"] == force) and
        (control is None or char["control"] == control) and
        (special is None or char["special"] == special) and
        (starting_character is None or char["starting_character"] == starting_character) and
        (releasedate is None or char["releasedate"].lower() == releasedate.lower()) and
        (price is None or char["price"] == price)
    ]
    return {"data": filtered_characters}


app.include_router(router, prefix='/tr_api')
