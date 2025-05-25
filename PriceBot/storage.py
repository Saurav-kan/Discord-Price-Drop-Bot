import json
from pathlib import Path
from typing import Dict, List

from config import TRACKED_FILE

def load_tracked() -> Dict[str, List[Dict]]:
    path = Path(TRACKED_FILE)
    if not path.exists():
        return {}
    return json.loads(path.read_text())

def save_tracked(data: Dict[str, List[Dict]]):
    Path(TRACKED_FILE).write_text(json.dumps(data, indent=2))
