# tests.py
from src.services import TrendsService
from src.responses import TrendItem
from unittest import mock
import pytest


@pytest.fixture
def trends_service_mock():
    trends_service = TrendsService()
    trends_service.api = mock.Mock()
    return trends_service


def test_get_trends_from_mongo(trends_service_mock):
    trends_service_mock.get_trends_from_mongo()  # This test can be implemented similarly to the one in your tests.py


def test_save_trends(trends_service_mock):
    trends_service_mock.save_trends()  # This test can be implemented similarly to the one in your tests.py

# Test the TrendsService methods using the mock
