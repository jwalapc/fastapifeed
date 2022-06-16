
# AUTHENTICATED FEED SYSTEM USING FASTAPI


### Steps to run the API

1. Install Docker Engine [For Windows](https://docs.docker.com/desktop/windows/install/) , [For MacOSX](https://docs.docker.com/desktop/mac/install/) , [For Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

2. Install Docker Compose [For Ubuntu](https://docs.docker.com/compose/install/)


Note: Docker Compose Comes Default with Docker Desktop for Windows and MacOSX


3. Clone this Repository and cd /to/the/repository

4. Run `docker-compose up`

5. You should be able to see the Container getting build and once Built you should be able to see the container Logs
6. Username for MongoDB : root
7. Password for MongoDB : pass

### Feed System

1.visit http://127.0.0.1:8008. 

2.If you are a new user ,signup by visiting http://127.0.0.1:8008/docs 
and clicking on the post request with route  '/auth/Signup' and provide the username,email and password.

3.If you are an existing user,login with your email and password by visiting http://127.0.0.1:8008/docs 
and clicking on the post request with route '/auth/login'.

4.If you are logged in to your account visit http://127.0.0.1:8008/chat/<username> to view and post on your feed.

5.Without login you wont be authenticated to your feed but will be asked to login to view it.

6.To Logout and terminate your session http://127.0.0.1:8008/docs and click on Logout.
