# tasks API using django rest framework

## API Reference

#### Get task list

```http
  GET /api/task-list/
```
Headers :

| Parameter       | Value                   | Description                     |
|:----------------|:------------------------|:--------------------------------|
| `Authorization` | `Bearer <access_token>` | **Required**. user access token |

Response:
a list of tasks of a user in the following format:

```json
[
    {
        "id": 1,
        "title": "task 1",
        "description": "task 1 description",
        "deadline": "2021-10-10",
        "reminder_time": "2021-10-10T10:10:00Z",
        "completed": false,
        "priority": "low",
        "user": 1
    },
    {
        "id": 2,
        "title": "task 2",
        "description": "task 2 description",
        "deadline": "2021-10-10",
        "reminder_time": "2021-10-10T10:10:00Z",
        "completed": false,
        "priority": "low",
        "user": 1
    }
]
```

#### Get task detail

```http
  GET /api/task-detail/<str:pk>/
```
Headers :

| Parameter       | Value                   | Description                     |
|:----------------|:------------------------|:--------------------------------|
| `Authorization` | `Bearer <access_token>` | **Required**. user access token |

Response:
a task of a user in the following format:

```json
{
    "id": 1,
    "title": "task 1",
    "description": "task 1 description",
    "deadline": "2021-10-10",
    "reminder_time": "2021-10-10T10:10:00Z",
    "completed": false,
    "priority": "low",
    "user": 1
}
```

#### Create task

```http
  POST /api/task-create/
```
Headers :

| Parameter       | Value                   | Description                     |
|:----------------|:------------------------|:--------------------------------|
| `Authorization` | `Bearer <access_token>` | **Required**. user access token |

Body: 

| Parameter       | Type              | Description                              |
|:----------------|:------------------|:-----------------------------------------|
| `title`         | `string`          | **Required**. title of the task          |
| `description`   | `string`          | **Required**. description of the task    |
| `deadline`      | `date`            | **Required**. deadline date of the task  |
| `reminder_time` | `datetime`        | **Required**. reminder time for the task |
| `completed`     | `boolean`         | **default (false)**. is task completed   |
| `priority`      | `low/medium/high` | **default (low)**. priority of the task  |

Response:
returns the created task back in the following format:

```json
{
    "id": 1,
    "title": "task 1",
    "description": "task 1 description",
    "deadline": "2021-10-10",
    "reminder_time": "2021-10-10T10:10:00Z",
    "completed": false,
    "priority": "low",
    "user": 1
}
```

#### Update task

```http
  PUT /api/task-update/<str:pk>/
```
Headers :

| Parameter       | Value                   | Description                     |
|:----------------|:------------------------|:--------------------------------|
| `Authorization` | `Bearer <access_token>` | **Required**. user access token |

Body: 

| Parameter       | Type              | Description                              |
|:----------------|:------------------|:-----------------------------------------|
| `title`         | `string`          | **Required**. title of the task          |
| `description`   | `string`          | **Required**. description of the task    |
| `deadline`      | `date`            | **Required**. deadline date of the task  |
| `reminder_time` | `datetime`        | **Required**. reminder time for the task |
| `completed`     | `boolean`         | **default (false)**. is task completed   |
| `priority`      | `low/medium/high` | **default (low)**. priority of the task  |

Response:
returns the updated task back in the following format:

```json
{
    "id": 1,
    "title": "task 1",
    "description": "task 1 description",
    "deadline": "2021-10-10",
    "reminder_time": "2021-10-10T10:10:00Z",
    "completed": false,
    "priority": "low",
    "user": 1
}
```

#### Delete task

```http
  DELETE /api/task-delete/<str:pk>/
```
Headers :

| Parameter       | Value                   | Description                     |
|:----------------|:------------------------|:--------------------------------|
| `Authorization` | `Bearer <access_token>` | **Required**. user access token |

Response:
```
"Item successfully delete!"
```


#### Get access & refresh tokens

```http
  POST /api/token/
```
Body :

| Parameter  | Type     | Description             |
|:-----------|:---------|:------------------------|
| `username` | `string` | **Required**. user name |
| `password` | `string` | **Required**. password  |

Response: 
returns an access token and a refresh token in the following format
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTA4NjU5MywiaWF0IjoxNjk3MzEwNTkzLCJqdGkiOiIzZGFmMzIzNDdlYjU0MTQyYTlkMTljMmQ5YTZlOTE5MyIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoidGVzdFVzZXIifQ.VyLd9IW49rz5X-8q6SMUj3iExCRapsCPx0W3Ekr2ph4",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MzEyOTkzLCJpYXQiOjE2OTczMTA1OTMsImp0aSI6IjJmYWE0Nzc4YzI2MDQyNWRiNjdkODVmMTU0ZjQ4MTgzIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ0ZXN0VXNlciJ9.AzT3Nl_da4xgDHaAy7M2E_15CvhZ1Vcrj73GMMhnzV8"
}
```

Note:
- access token expires in 30 minutes
- refresh token expires in 90 days

#### Refresh tokens

```http
  POST /api/token/refresh/
```
Body :

| Parameter | Type     | Description                 |
|:----------|:---------|:----------------------------|
| `refresh` | `string` | **Required**. refresh token |

Response:
Returns an access token with a new refresh token and the 90 days limit is reset.

```json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MzEyNjgyLCJpYXQiOjE2OTczMTA1OTMsImp0aSI6IjRiYjkxZThkMGIzODRlMTI4ZTg4MGU4NDFlZTBmZTEzIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJ0ZXN0VXNlciJ9.68jy8fr8y0n04y_WQxFygyt7u5JGzEfIxI31jKNOEo4",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTA4Njg4MiwiaWF0IjoxNjk3MzEwODgyLCJqdGkiOiI5ZjkyZmFiZmQyNzU0ZWM3ODU0YmJhZjUyNzg5Nzk0NyIsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoidGVzdFVzZXIifQ.yVxgC0v-6-2AESGl_RTzKgsi0lVGme_Cekhvr4MNJgg"
}
```
Note:
- all the previous refresh tokens are blacklisted

#### Create user

```http
  POST /api/user/create/
```
Body :

| Parameter   | Type       | Description                                 |
|:------------|:-----------|:--------------------------------------------|
| `username`  | `string`   | **Required**. user name (should be unique)  |
| `email`     | `email`    | **Required**. user email (should be unique) |
| `password`  | `password` | **Required**. password                      |
| `password2` | `password` | **Required**. password confirmation         |

Response:
returns the tokens for the created user.

```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNTA4NzAzOCwiaWF0IjoxNjk3MzExMDM4LCJqdGkiOiJjMDQyN2I0OTYzNGU0MmRmODg5ZjdiMjJhODQxYTUxOSIsInVzZXJfaWQiOjh9.uadpB_kZZBuItM8j_EKMQnmAL-Z0tUx8L2jVBLXKfVY",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MzEyODM4LCJpYXQiOjE2OTczMTEwMzgsImp0aSI6IjgzN2E2MjZhZDBiYzQ1NWI5ZTg2NzY0ZDU0ZTlkY2E4IiwidXNlcl9pZCI6OH0.7FHVrpEuOWtPbBRxt2ibL7_7cHjLKHiyRNKf2bPO-uU"
}
```

if username already exists:
```json
{
  "username": [
    "A user with that username already exists."
  ]
}
```

if email already exists:
```json
{
  "email": [
    "This field must be unique."
  ]
}
```

if password and password2 don't match:
```json
{
  "password": [
    "Password fields didn't match."
  ]
}
```

## Installation

```bash
  pip install -r requirements.txt
```

### Run migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```
### Create superuser

```bash
  python manage.py createsuperuser
```

### Run server

```bash
  python manage.py runserver
```

## Authors

- [@Siddid Soni](https://github.com/Siddid-Soni/)


