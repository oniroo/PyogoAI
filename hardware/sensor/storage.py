import base64
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

DATA_DIR = Path("data")
IMAGE_DIR = DATA_DIR / "images"
TS_DIR = DATA_DIR / "timeseries"

for directory in [DATA_DIR, IMAGE_DIR, TS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def _auto_write(path: Path, content: Any):
    temp = path.with_suffix('.tmp')
    with temp.open('w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)
    temp.rename(path)

def append_timeseries(sensor_type: str, record: Dict[str, Any]):
    file = TS_DIR / f"{sensor_type}.json"

    # noinspection PyBroadException
    try:
        data = json.loads(file.read_text(encoding='utf-8'))
    except Exception:
        # NoDataException
        data = []

    data.append(record)
    _auto_write(file, data)

def save_image(b64: str, prefix: str) -> str:
    filename = f"{prefix}_{datetime.utcnow().strftime('%Y%m%dT%H%M%S%f')}.png"
    save_path = IMAGE_DIR / filename

    img_data = base64.b64decode(b64)

    temp = save_path.with_suffix(".tmp")
    with temp.open("wb") as f:
        f.write(img_data)
    temp.replace(save_path)

    return str(save_path)