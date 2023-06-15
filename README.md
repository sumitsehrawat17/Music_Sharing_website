# music_sharing_website

# Music Sharing Website

This is a web application that allows users to upload and share music files with each other. Users can register on the platform using their email and log in using their email and password. The website provides various options for uploading and accessing music files, including public, private, and protected files.

## Features

The website offers the following key features:

1. User Registration:
   - Users can create an account on the platform by providing their email address.
   - Passwords are securely stored using industry-standard encryption techniques.

2. User Login:
   - Registered users can log in to the platform using their email and password.

3. Music File Upload:
   - Users can upload music files to the website.
   - Music files can be uploaded as public, private, or protected.

4. Public Music Files:
   - Public music files are visible to all users of the platform.
   - These files can be searched, played, and downloaded by any user.

5. Private Music Files:
   - Private music files are only visible to the user who uploaded them.
   - Users can access their private files from their personal profile or dashboard.

6. Protected Music Files:
   - Users can upload music files as protected and provide a list of email addresses for access.
   - The system checks if the provided email addresses belong to registered users on the platform.
   - If a match is found, the corresponding user can access the protected file.

7. Homepage:
   - After logging in, users are presented with a homepage displaying relevant music files.
   - The homepage includes music files uploaded by the logged-in user, public files from other users, and protected files the user has access to.

## Setup Instructions

To set up the music sharing website locally, please follow these steps:

1. Clone the repository from GitHub:

   ```
   git clone <repository_url>
   ```

2. Install the required dependencies:

   ```
   cd music-sharing-website
   pip install -r requirements.txt
   ```

3. Set up the SQLite Database:
   - The project uses SQLite as the backend database, which is included by default in Python.
   - No additional setup is required for the database.

4. Start the Application:
   - Run the following command to start the Django development server:

   ```
   python manage.py runserver
   ```

   - The website will be accessible at `http://localhost:8000`.

## Technologies Used

The music sharing website is built using the following technologies:

- Django: A Python-based web framework for rapid development.
- SQLite: A lightweight, file-based database used for data storage.
- HTML and CSS: Used for the frontend interface and styling.

## Conclusion

With this music sharing website, users can easily upload, share, and access music files. The platform allows for public, private, and protected files, providing different levels of visibility and accessibility. Users can register, log in, and manage their music files conveniently. The website can be further customized and expanded based on specific requirements.
