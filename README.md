# EVENT MANAGEMENT APP
Simple event management application

Description
-----------

The developed APIs for the event management platform provide a comprehensive set of functionalities to allow users to 
create accounts, log in and out, view active event list, book & viewmtickets for the event, 
search events by category, title, description or event date, and provide an admin(**http://127.0.0.1:8000/admin/**) 
interface for create and manage events, and categories under **Event** table. also provided **personalized APIs** for **sensitive admin oprations**. 

NOTE - Developers: Basicaly we are not allowing creat admin automatically, so plese makse sure that have admin account or create one **Superuser**.

- The APIs are designed to be user-friendly, secure, and efficient. They handle various error scenarios and provide appropriate error responses to 
ensure data integrity and smooth user experience. The implementation includes unit tests to verify the correctness and functionality of the APIs.

- To facilitate API usage and integration, comprehensive API documentation is provided using Swagger. The documentation includes detailed descriptions, 
request and response examples, and clear instructions on how to interact with each API endpoint.

- In conclusion, the developed APIs for the social media platform offer a robust and scalable solution for building a social media application, 
enabling users to connect, share, and interact within the platform's ecosystem.

Authorize
---------

- please provide your AUTH-TOEN to Authorize swagger function (**format: Token {YOUR TOKEN}**) for further api access.

Dockerize
---------

- 1. **sudo docker-compose build** -> compose and build.

- 2. **docker-compose run web python3 manage.py migrate** -> migrate migrations.

- 3. **sudo docker-compose up** -> run container

DB - Connection
---------------

- Db configure in **.env** file

- Make sure to change host name to **localhost** while wrking with local db connection.

**Thankyou**