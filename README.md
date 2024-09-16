# Django_graphql_server

## Installation
- Clone the repo
  
  ```
  git clone https://github.com/KrishavRajSingh/Django_graphql_server.git
  cd Django_graphql_server
  ```
- Activate a virtual enviroment
  
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```
- Install Dependencies
  
  ```
  pip install -r requirements.txt
  ```

  ## Database
  - Start a postgres instance
  - Update DATABASES in bank_api/settings.py
    ![image](https://github.com/user-attachments/assets/9d447e55-81bb-433c-9988-5025144a3705)
  - Dump the sql data in postgres

## Server
- Start the server
  
  ```
  python manage.py runserver
  ```
  Now got to http://127.0.0.1:8000/gql
- Run these Queries
  ![image](https://github.com/user-attachments/assets/a42603b4-4d29-430a-9eb7-a8e4637ce1df)
  ![image](https://github.com/user-attachments/assets/cdfca3f3-389f-489f-bbe0-ab55850c6ee7)
  ![image](https://github.com/user-attachments/assets/5912b866-b8ec-43a4-b035-2a2345d8ee12)



  
