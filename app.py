from app.main import app
from app.db import create_user_db
import os

if __name__ == '__main__':
    if os.path.exists('user.db') == False:
        create_user_db()
        
    app.run(debug=True)