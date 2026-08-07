import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/media/sf_inspection_bot_ws/src/install/inspection_bot_nav'
