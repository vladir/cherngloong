# cherngloong
To solve this Stackoverflow question http://stackoverflow.com/questions/36510620/cant-view-thumbnail-created-in-django-admin

# Clone the repo
`$ git clone git@github.com:vladir/cherngloong.git .`

# Make a Python virtual environment
`$ virtualenv venv`

# Activate the virtualenv
`$ virtualenv venv/bin/activate`

# Install the dependencies
`$ pip install -r requirements.txt`

# Create a superuser
`$ python manage.py createsuperuser`

# Run the Django dev server
`python manage.py runserver`

Go to http://127.0.0.1:8000/admin/, login with you superuser credentials, add files, and you will see the thumbnails.
