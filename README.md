## API Documentation

Hello! Call me Satorn. I'm a Web Developer!
![image](https://github.com/user-attachments/assets/d1d862f4-56be-4f02-9abc-682ba9de6c2e)

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns general information about the API and the developer.

**Response:**

```json
{
    "data": [
        {
            "APIs info": [
                {
                    "name": "TalesRunner API",
                    "description": "This is an API for TalesRunner",
                    "version": "0.1.0",
                    "Docs": "https://satorn.vercel.app/docs"
                }
            ],
            "Developer info": [
                {
                    "author": "Satorn Sukkang",
                    "email": "pondforbusiness@gmail.com",
                    "github": "https://github.com/pondsan1412",
                    "facebook": "https://www.facebook.com/pondcomp",
                    "website": "https://satorn.vercel.app"
                }
            ]
        }
    ]
}
```

#### 2. Character Endpoint

- **URL**: `/character`
- **Method**: `GET`
- **Description**: Retrieves information about characters. Supports filtering by various fields.

**Query Parameters:**

- `id` (optional): The ID of the character.
- `name` (optional): The name of the character.
- `original_name` (optional): The original name of the character.
- `age` (optional): The age of the character.
- `type` (optional): The type of the character.
- `height` (optional): The height of the character.
- `weight` (optional): The weight of the character.
- `bloodtype` (optional): The blood type of the character.
- `birthdate` (optional): The birthdate of the character.
- `occupation` (optional): The occupation of the character.
- `origin` (optional): The origin of the character.
- `wish` (optional): The wish of the character.
- `speed` (optional): The speed attribute of the character.
- `acceleration` (optional): The acceleration attribute of the character.
- `force` (optional): The force attribute of the character.
- `control` (optional): The control attribute of the character.
- `special` (optional): Indicates if the character is special.
- `starting_character` (optional): Indicates if the character is a starting character.
- `releasedate` (optional): The release date of the character.
- `price` (optional): The price of the character.

**Response:**

```json
{
    "data": [
        {
            "id": 1,
            "name": "Charlie",
            "original_name": "Chowon",
            "thai_name": "โชวอน",
            "description": "Character Information Charlie, dubbed 'The Athlete'...",
            "appearance": "Charlie appearance as a young slim child...",
            "age": 11,
            "type": "human",
            "height": "4.7ft (140cm)",
            "weight": "77 lbs (35kg)",
            "bloodtype": "0",
            "birthdate": "May 2",
            "occupation": "Elementary School Athletic Team Member",
            "origin": "Korea",
            "wish": null,
            "speed": 3,
            "acceleration": 3,
            "force": 3,
            "control": 3,
            "special": false,
            "image_url": "https://static.wikia.nocookie.net/talesrunner-sg/images/c/c9/Charlie.png/revision/latest?cb=20140101024429",
            "price": 10000,
            "starting_character": true,
            "releasedate": "July 29, 2005"
        }
        // More character objects...
    ]
}
```

**Example Requests:**

1. **Retrieve all characters:**

   ```
   GET /character
   ```

2. **Retrieve character by ID:**

   ```
   GET /character?id=1
   ```

3. **Retrieve character by name:**

   ```
   GET /character?name=Charlie
   ```

4. **Retrieve character by original name:**

   ```
   GET /character?original_name=Chowon
   ```

5. **Retrieve character by other fields (e.g., age, height):**

   ```
   GET /character?age=11
   GET /character?height=4.7ft
   ```

**Note:** All parameters are optional. If no parameters are provided, all characters will be returned.

#### 3. Items Endpoint

- **URL**: `/items`
- **Method**: `GET`
- **Description**: Retrieves information about items. Supports filtering by `id`.

**Query Parameters:**

- `id` (optional): The ID of the item.

**Response:**

```json
{
    "data": [
        {
            "shirt": [
                {
                    "id": 2,
                    "desc": "ไอเทมวันสงกรานต์",
                    "stats": [
                        {
                            "TR": "+200%",
                            "EXP": "+220%",
                            "speed": "+1",
                            "accel": "+2",
                            "power": "+2",
                            "ability": "เปอร์เซ็นในการแปลงร่างเป็นกิ้งค่า ด้วยไอเทมระเบิดแปลงกาย + 75%",
                            "trigger_fury": "+18%",
                            "duration_fury": "+18%",
                            "reduce_duration_of_black_melon": "-12%",
                            "protecting_when_attacked_by_chicken_penguin": "+12%",
                            "protecting_from_lighting": "+25%",
                            "gain_max_dash_by": "+15%",
                            "gain_EXP_max_by": "+2200",
                            "TR_value": 200,
                            "TR_percent": true,
                            "EXP_value": 220,
                            "EXP_percent": true,
                            "gain_max_dash_by_value": 15,
                            "gain_max_dash_by_percent": true
                        }
                    ]
                }
            ]
        }
        // More item objects...
    ]
}
```

**Example Requests:**

1. **Retrieve all items:**

   ```
   GET /items
   ```

2. **Retrieve item by ID:**

   ```
   GET /items?id=2
   ```

**Note:** If no ID is provided, all items will be returned.
