import hashlib
import shutil
import tempfile
from urllib.parse import quote_plus
from pathlib import Path
import os

def compute_sha256(filepath):
    """Compute SHA-256 hash of the file (same as Gradio)."""
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def copy_to_gradio_cache(original_path, sha256_hash):
    """Copy the file into /tmp/gradio/<hash>/ and return full cached path."""
    cache_dir = Path(tempfile.gettempdir()) / "gradio" / sha256_hash
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / os.path.basename(original_path)
    shutil.copy2(original_path, dest)
    return dest
