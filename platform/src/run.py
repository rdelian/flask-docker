import sys; sys.path.append("/platform/src")
from app import app, db, models

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
