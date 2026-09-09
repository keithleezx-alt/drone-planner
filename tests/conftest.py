import os
import numpy as np
import pytest

MAPS = os.path.join(os.path.dirname(__file__), "..", "maps")


@pytest.fixture
def simple_map():
    from src.grid.grid import load_map
    return load_map(os.path.join(MAPS, "simple.txt"))


@pytest.fixture
def open_map():
    from src.grid.grid import load_map
    return load_map(os.path.join(MAPS, "open.txt"))
