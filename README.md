## API Documentation
Hello! call me Satorn I'm an Web Developer!
![image](https://github.com/user-attachments/assets/d1d862f4-56be-4f02-9abc-682ba9de6c2e)

### Base URL
```
http://127.0.0.1:8000/tr_api
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
- **Description**: Retrieves information about characters. Supports filtering by `id`, `name`, `original_name`, and other fields.

**Query Parameters:**

- `id` (optional): The ID of the character.
- `name` (optional): The name of the character.
- `original_name` (optional): The original name of the character.

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
            "Occupation": "Elementary School Athletic Team Member",
            "Origin": "Korea",
            "Wish": null,
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

**Note:** All parameters are optional. If no parameters are provided, all characters will be returned.


