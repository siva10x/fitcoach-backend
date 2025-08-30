from .health import health_bp
from .workout import workout_bp
from .user import users_bp

# List of all blueprints to register
all_blueprints = [
    health_bp,
    workout_bp,
    users_bp
]