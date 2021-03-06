# GEO REST API

### Author: James Byrne
### Date: 1/17/2022
### For: Maxar code challenge

---

## Problem:
Create a REST API, with a single resource, that accepts an HTTP POST method request with two GeoJSON polygon objects.
This should returns a Boolean value indicating whether the provided objects spatially intersect one another.

## Requirements:
- All requests and responses must be valid JSON
- The completed challenge must be pushed to GitHub (github.com) for review during onsite interview in a private repository (give access to me, please)
- Include relevant documentation for the running and testing of the application

- **Note:** Try and write the application in Python if possible and use open source libraries to your advantage!

- It's ok if you are unable to complete the challenge, but at minimum be prepared to discuss possible implementation steps during onsite interview.

## Guidance:
- This should take less than 4 hrs to complete (although, you can take up to a week to send back your solution)

- We're not looking for perfection, but rather a framework to hold a discussion about your thoughts on design, implementation, library selection, etc...

- If you're taking more time than expected: add skeleton code, comments, etc... to support that discussion.

## Libraries
- Flask

- ArcGIS API (Python)

- Docker

## Running Dev Environment
- Clone this repo with `git clone https://github.com/jbyrne6/geo-rest-api.git` to your computer

- Build and run this project with `docker-compose up --build`

- Go to the url [localhost:5000](https://localhost:5000) once the project is built to test that the api is running

## Endpoints
| Endpoints           | Method | Input                     | Ouput | 
| ------------------- | ------ | ------------------------- | --------------------------- |
| /                   | GET    | N/A                       | Greeting message (json)     |
| /polygons-intersect | POST   | 2 GeoJSON polygon objects | Intersection boolean (json) |
