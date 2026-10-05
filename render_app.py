import os
import sys
from unittest.mock import MagicMock

# Mock out 'spaces' so it doesn't crash on import
sys.modules['spaces'] = MagicMock()

if __name__ == '__main__':
    from demo.app import demo
    port = int(os.environ.get('PORT', 7860))
    # Launch binding to 0.0.0.0 and the correct port
    demo.launch(server_name='0.0.0.0', server_port=port)
    
