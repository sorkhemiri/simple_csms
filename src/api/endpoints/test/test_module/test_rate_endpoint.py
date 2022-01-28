import json

from fastapi.testclient import TestClient

from app import app


class RateEndPointTestCase:
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
                headers={"Content-Type": "application/json"},
            )
            assert 200 == response.status_code
            assert response.json() == {
                "overall": 7.04,
                "components": {"energy": 3.277, "time": 2.767, "transaction": 1},
            }
