import os
backend_url = os.environ.get('backend_url')
if backend_url is None:
    backend_url = 'http://127.0.0.1:8081/'