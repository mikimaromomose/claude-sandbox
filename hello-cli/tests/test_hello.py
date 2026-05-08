import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hello import greet

def test_greet_world():
    assert greet("World") == "Hello, World!"

def test_greet_claude():
    assert greet("Claude") == "Hello, Claude!"
