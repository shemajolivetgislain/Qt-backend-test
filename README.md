# Blog APP 


Welcome to the backend of the Blog Application! This platform provides robust features for managing your blog posts with ease. With this application, you can seamlessly create, update, and delete blog posts. It also includes user authentication, enabling authors to register and log in to manage their content. Start exploring the Blog Application backend to share your stories and articles with the world!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Follow these steps to set up your local development environment.

### Prerequisites

To run this project locally, you'll need to have Node.js and npm installed on your machine. The project was built using Node.js [Version 21.0.0] or abover - It's recommended to use a similar version to avoid compatibility issues.

### Installation

1. **Clone the repository and install the dependencies:**

   Clone the GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/shemajolivetgislain/Qt-backend-test.git
   cd Qt-backend-test
   npm install

   ```

### Running the Project

  1. **Create Environment**

   Then, do:

   ```bash
   python -m venv env
  ```

  To Run the app in the dev mode

  2. **Activate Environment**

   You can do:

   ```bash
   source ./env/scripts/activate

  ```

  to create env app.
  3. **Packages installation**

   You can do:

   ```bash
   pip install -r requirements.txt

  ```

  to install the app packages.

 4. **Configure Enviromnent Variable**

   You can do:

   ```bash
   touch .env

  ```
   to create env variable file.
 5. **Running Migrations**

   You can do:

   ```bash
   python manage.py migrate

  ```
   running migration.
 6. **Running server**

   You can do:

   ```bash
   python manage.py runserver

  ```
   to run server .

### Before running Application remember to add Db Environment variables

### Db Environment

- DATABASE_NAME=
- DATABASE_USER=
- DATABASE_PASSWORD=
- DATABASE_HOST=
- DATABASE_PORT='5432'
- DEBUG=True


### License

- Distributed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

### Acknowledgments

Tools used to build the projects: 

- Python Django
- Django Restframework
- PostgreSQL
- Jwt authentication


