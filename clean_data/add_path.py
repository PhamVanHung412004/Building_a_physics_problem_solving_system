import sys
import os
# thêm path thủ công 
def add():
    return sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))