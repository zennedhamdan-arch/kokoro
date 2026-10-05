import sys
from unittest.mock import MagicMock

# Mock out the 'spaces' module so demo/app.py can import it without crashing
sys.modules['spaces'] = MagicMock()

# Now import and run the original demo app
if __name__ == '__main__':
    from demo.app import demo
    # Launch with Render's required host and port bindings
    demo.launch(server_name='0.0.0.0', server_port=int(os.environ.get('PORT', 7860)))
