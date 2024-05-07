import math
import pathlib
import random
import sys

from typing import Dict, Union


import numpy as np
import pytest

RESULT = Dict[str, Union[float, np.ndarray]]


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(0, str(proj_folder))


import main


random.seed()


@pytest.fixture
def x1_deg() -> float:
    return random.randint(0, 90)


@pytest.fixture
def x2_deg() -> float:
    return random.randint(270, 360)


@pytest.fixture
def delta_x() -> float:
    return random.uniform(0.1, 1.9)


@pytest.fixture
def x_deg_array(x1_deg:int, x2_deg:int, delta_x:float) -> np.ndarray:
    return np.arange(x1_deg, x2_deg, delta_x)


@pytest.fixture
def x_rad_array(x_deg_array:np.ndarray) -> np.ndarray:
    return np.deg2rad(x_deg_array)


@pytest.fixture
def result_dict(x_rad_array) -> RESULT:
    return main.int_sin(x_rad_array)


@pytest.fixture
def result_a_array(result_dict:RESULT) -> nd.ndarray:
    return result_dict['a_array']


@pytest.fixture
def result_area(result_dict:RESULT) -> float:
    return result_dict['area']


def test_result_type(result_dict:RESULT):
    assert isinstance(result_dict, dict), "returned result is not a `dict`\n반환된 결과가 `dict`가 아님"

    assert 'a_array' in result_dict, "returned result does not have `a_array`\n반환값에 `a_array`가 없음"
    assert 'area' in result_dict, "returned result does not have `area`\n반환값에 `area`가 없음"


def test_rect_type(result_a_array:nd.ndarray):
    assert isinstance(result_a_array, nd.ndarray), "returned result is not a `nd.ndarray`\n반환된 결과가 `nd.ndarray`가 아님"


def test_area_type(result_area:float):
    assert isinstance(result_area, float), "returned result is not a `float`\n반환된 결과가 `float`가 아님"


if "__main__" == __name__:
    pytest.main([__file__])
