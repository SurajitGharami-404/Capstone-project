
# Little Lemon - Restaurant website

Little lemon is a restaurant for which apis' are creted for functionality like get menu, book a restaurant seat

## API Reference

#### Create user

```http
  POST auth/users
```

#### Log in users

```http
  POST restaurant/api-token-auth
```

#### Get all menu items

```http
  GET /restaurant/menu
```

#### Get single menu item

```http
  GET /restaurant/menu/${id}
```
#### Get all bookings

```http
  GET /restaurant/booking
```



## Token Authentication

After sending post request to LOGIN route get authentication token as response. Send this token with every POST, GET, PUT, PATCH, DELETE request header like shown below : 

```bash
  Authorization: Token <response token>
```

