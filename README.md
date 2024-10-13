# LittleLemon
## Setup
- Clone the code

  ```
  git clone https://github.com/jquirosz/LittleLemon.git
  ```

    add your credentials if prompted for them.
- Create a new virtual environment.

    ```
  python -m venv env
  source env/bin/activate
  ```
  
- Then to add al required dependencies run
  
  ```
  pip install -r requirements.txt
  ```

- Run migrations

  ```
  python manage.py makemigrations
  ```

  ``` 
  python manage.py makemigrations
  ```

- Remember to setup the superuser
    ```
  python manage.py createsuperuser
  ```

## Run
To run the application run:

```
python manage.py runserver
```

## Endpoints to test
### HTML
- Serving html, just go to `http://127.0.0.1:8000/restaurant/` in a browser

### Menu
- Adding menu items:

```
curl --location 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Content-Type: application/json' \
--data '{
    "id": 1,
    "title": "Cookies",
    "price": "2.90",
    "inventory": 25
  }'
  ```

```
curl --location 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Content-Type: application/json' \
--data '{
    "id": 2,
    "title": "Cake",
    "price": "11.90",
    "inventory": 8
  }'
  ```

```
curl --location 'http://127.0.0.1:8000/restaurant/menu/' \
--header 'Content-Type: application/json' \
--data '{
    "id": 3,
    "title": "Ice cream",
    "price": "14.90",
    "inventory": 30
  }'
  ```

- Get all menu items

```curl --location 'http://127.0.0.1:8000/restaurant/menu/'```

- Get a menu item by id
```
 curl --location 'http://127.0.0.1:8000/restaurant/menu/<id>'
 Example
 curl --location 'http://127.0.0.1:8000/restaurant/menu/1'
 ```

- Delete a menu item:
```
curl --location --request DELETE 'http://127.0.0.1:8000/restaurant/menu/<id>'
Example
curl --location --request DELETE 'http://127.0.0.1:8000/restaurant/menu/1'
```

### Bookings
In order to see and add bookings you need an authentication token to get it use the endpoint:
```
curl --location 'http://127.0.0.1:8000/restaurant/api-token-auth/' \
--header 'Content-Type: application/json' \
--data '{
  "username": "user",
  "password": "password"
}'
```

You will get a response containing your token.

- Create a new booking:
```
curl --location 'http://127.0.0.1:8000/restaurant/booking/' \
--header 'Authorization: Token 64ef26e312f845778f64012ae4e76b42571edeb0' \
--header 'Content-Type: application/json' \
--data '{
    "id": 1,
    "name": "User 1",
    "no_of_guests": 4,
    "bookingDate": "2024-10-24T10:00"
}'
```

```
curl --location 'http://127.0.0.1:8000/restaurant/booking/' \
--header 'Authorization: Token 64ef26e312f845778f64012ae4e76b42571edeb0' \
--header 'Content-Type: application/json' \
--data '{
    "id": 2,
    "name": "User 2",
    "no_of_guests": 2,
    "bookingDate": "2024-10-24T11:00"
}'
```

- Get all bookings
```
curl --location 'http://127.0.0.1:8000/restaurant/booking/' \
--header 'Authorization: Token 64ef26e312f845778f64012ae4e76b42571edeb0'
```
