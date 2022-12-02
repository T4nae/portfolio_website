from app.main import app
from app.db import create_user_db, create_navigation_db
import os

if __name__ == '__main__':
    if os.path.exists('DB/user.db') == False:
        create_user_db()
    if os.path.exists('DB/navigation.db') == False:
        create_navigation_db()
               
    app.run(debug=True)