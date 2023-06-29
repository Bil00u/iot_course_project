# Importing the Flask app instance from my application code
from my_flask_app import app

# This block makes sure the server only runs if the script is executed directly from the Python interpreter
# and not used as an imported module
if __name__ == "__main__":
    # Run the Flask development server. It's not meant to be used on production environments
    app.run()
