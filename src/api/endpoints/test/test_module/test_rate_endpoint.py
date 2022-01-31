import json

from fastapi.testclient import TestClient

from app import app
from settings import env_config


class RateEndPointTestCase:
    @staticmethod
    def test_authorization():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={"Content-Type": "application/json"},
            )
            assert 403 == response.status_code
            assert {"detail": "Not authenticated"} == response.json()

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: "some-invalid-secret",
                },
            )
            assert 403 == response.status_code
            assert {"detail": "invalid credentials"} == response.json()

    @staticmethod
    def test_example_testcase():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 200 == response.status_code
            assert response.json() == {
                "overall": 7.04,
                "components": {"energy": 3.277, "time": 2.767, "transaction": 1},
            }

    @staticmethod
    def test_zero_state():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0, "time": 0, "transaction": 0},
                "cdr": {
                    "meterStart": 0,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 0,
                    "timestampStop": "2021-04-05T10:04:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 200 == response.status_code
            assert response.json() == {
                "overall": 0,
                "components": {"energy": 0, "time": 0, "transaction": 0},
            }

    @staticmethod
    def test_invalid_date():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0, "time": 0, "transaction": 0},
                "cdr": {
                    "meterStart": 0,
                    "timestampStart": "0000-00-00T00:00:00Z",
                    "meterStop": 0,
                    "timestampStop": "0000-00-00T00:00:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 422 == response.status_code

    @staticmethod
    def test_start_date_gt_end_date():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T11:27:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T10:04:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert response.json() == {
                "detail": "timestampStart must be less or equal to timestampStop"
            }

    @staticmethod
    def test_start_meter_gt_end_meter():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1215230,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1204307,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert response.json() == {
                "detail": "meterStart must be less or equal to meterStop"
            }

    @staticmethod
    def test_negative_values():
        with TestClient(app) as client:
            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": -1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert response.json() == {
                "detail": "meterStart and meterStop must be non-negative"
            }

            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": -1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert response.json() == {
                "detail": "meterStart and meterStop must be non-negative"
            }

            data = {
                "rate": {"energy": -0.3, "time": 2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert {
                "detail": "rating price values must be non-negative"
            } == response.json()

            data = {
                "rate": {"energy": 0.3, "time": -2, "transaction": 1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert {
                "detail": "rating price values must be non-negative"
            } == response.json()

            data = {
                "rate": {"energy": 0.3, "time": 2, "transaction": -1},
                "cdr": {
                    "meterStart": 1204307,
                    "timestampStart": "2021-04-05T10:04:00Z",
                    "meterStop": 1215230,
                    "timestampStop": "2021-04-05T11:27:00Z",
                },
            }

            response = client.post(
                "/rate",
                data=json.dumps(data),
                headers={
                    "Content-Type": "application/json",
                    env_config.api_key_name: env_config.api_key_secret,
                },
            )
            assert 400 == response.status_code
            assert {
                "detail": "rating price values must be non-negative"
            } == response.json()
