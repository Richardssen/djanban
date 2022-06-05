
import uuid


# Custom uuid used for some elements
def custom_uuid():
    return uuid.uuid1().bytes.encode('base64').rstrip('=\n').replace('/', '_')