import sys
import types
from pathlib import Path

# Expose the backend-api directory as a package named `backend_api`
package_path = Path(__file__).resolve().parents[1] / "backend-api"
backend_pkg = types.ModuleType("backend_api")
backend_pkg.__path__ = [str(package_path)]
sys.modules.setdefault("backend_api", backend_pkg)

# Provide a minimal `requests` stub if the real library is unavailable
if "requests" not in sys.modules:
    requests = types.ModuleType("requests")

    class DummyResponse:
        def __init__(self, data):
            self._data = data
        def json(self):
            return self._data
        def raise_for_status(self):
            pass

    def post(url, json=None, headers=None, timeout=None):
        return DummyResponse({"response": f"Gemini response for: {json.get('prompt', '')}"})

    requests.post = post
    sys.modules["requests"] = requests

# Provide a minimal 'python-multipart' stub to satisfy FastAPI when parsing UploadFile
if 'multipart' not in sys.modules:
    multipart = types.ModuleType('multipart')
    multipart.__version__ = '0.0'
    sub = types.ModuleType('multipart.multipart')
    def parse_options_header(value):
        return None, {}
    sub.parse_options_header = parse_options_header
    multipart.multipart = sub
    sys.modules['multipart'] = multipart
    sys.modules['multipart.multipart'] = sub
