import sys
import os
from pathlib import Path

# Add the app directory to Python path for testing
root_dir = Path(__file__).parent.parent
app_dir = root_dir / "app"
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(app_dir))

# not entirely sure what this does or why its needed,
# had to use ai to tell me what to do here