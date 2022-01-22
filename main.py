## gunicorn -c config.py --reload --preload app:app
from app import app
import config


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG_MODE)
