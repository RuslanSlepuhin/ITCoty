# This contains variables that will be called
# as relative paths to different project files

from pathlib import Path

_this_file = Path(__file__).resolve()

DIR_ROOT = _this_file.parent.parent.resolve()
DIR_EXCEL = (DIR_ROOT / "excel").resolve()
DIR_LOGS = (DIR_ROOT / "logs").resolve()
DIR_UTILS = (DIR_ROOT / "utils" / "additional_data").resolve()
