def load_my_keys():
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from util.LoadMyKeys import load_keys
    load_keys()