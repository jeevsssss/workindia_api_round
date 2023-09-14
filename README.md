# Cricbuzz-Like Cricket Platform

## Description

This project aims to create a platform similar to Cricbuzz, where users can browse multiple cricket matches and view match details. The platform supports role-based access, with two types of users: Admin and Guest.

## Endpoints

### Register Admin

- **Endpoint:** `/api/admin/signup`
- **Method:** `POST`
- **Description:** Register a new admin user.
- **Request Data:**
  - "username": "example_user"
  - "password": "example_password"
  - "email": "user@example.com"
- **Response Data:**
  - "status": "Admin Account successfully created"
  - "status_code": 200
  - "user_id": "123445"

### Login User

- **Endpoint:** `/api/admin/login`
- **Method:** `POST`
- **Description:** Log in as a registered user.
- **Request Data:**
  - "username": "example_user"
  - "password": "example_password"
- **Response Data:**
  - "status": "Login successful"
  - "status_code": 200
  - "user_id": "12345"
  - "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"

### Create Match

- **Endpoint:** `/api/matches`
- **Method:** `POST`
- **Headers:** 
  - "Authorization": "Bearer {token}"
- **Description:** Create a new cricket match.
- **Request Data:**
  - "team_1": "India"
  - "team_2": "Australia"
  - "date": "2023-07-12"
  - "venue": "Sydney Cricket Ground"
- **Response Data:**
  - "message": "Match created successfully"
  - "match_id": "3"

### Get Match Schedules

- **Endpoint:** `/api/matches`
- **Method:** `GET`
- **Description:** Get a list of all cricket match schedules.
- **Request Data:** None
- **Response Data:**
  - "matches": [
    - {
      - "match_id": "1"
      - "team_1": "India"
      - "team_2": "England"
      - "date": "2023-07-10"
      - "venue": "Lord's Cricket Ground"
    - },
    - {
      - "match_id": "2"
      - "team_1": "Australia"
      - "team_2": "New Zealand"
      - "date": "2023-07-11"
      - "venue": "Melbourne Cricket Ground"
    - },
    - ...
  - ]

### Get Match Details

- **Endpoint:** `/api/matches/{match_id}`
- **Method:** `GET`
- **Description:** Get detailed information about a specific cricket match.
- **Request Data:** None
- **Response Data:**
  - "match_id": "1"
  - "team_1": "India"
  - "team_2": "England"
  - "date": "2023-07-10"
  - "venue": "Lord's Cricket Ground"
  - "status": "upcoming"
  - "squads": {
    - "team_1": [
      - {
        - "player_id": "123"
        - "name": "Virat Kohli"
      - },
      - {
        - "player_id": "456"
        - "name": "Jasprit Bumrah"
      - },
      - ...
    - ],
    - "team_2": [
      - ...
    - ]
  - }

### Add a Team Member to a Squad

- **Endpoint:** `/api/teams/{team_id}/squad`
- **Method:** `POST`
- **Description:** Add a player to a team's squad.
- **Request Data:**
  - "name": "Rishabh Pant"
  - "role": "Wicket-Keeper"
- **Response Data:**
  - "message": "Player added to squad successfully"
  - "player_id": "789"

### Get Player Statistics

- **Endpoint:** `/api/players/{player_id}/stats`
- **Method:** `GET`
- **Description:** Get statistics for a specific cricket player.
- **Request Data:** None
- **Response Data:** (You can add dummy data of your own for this use case)
