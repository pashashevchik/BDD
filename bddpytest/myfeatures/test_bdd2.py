import pytest

from pytest_bdd import scenario, scenarios, given, when, then
from pages.login_page import LoginPage
from base.base_class import BasePage
from pathlib import Path

featureFileDir = "myfeatures"
featureFile = 'login_valid_data.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

