
from django.conf import settings
import uuid

def generate_unique_id():
    """Generate a unique identifier."""
    return str(uuid.uuid4())

def get_file_path(instance, filename):
    """Generate a unique file path for uploads."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename
