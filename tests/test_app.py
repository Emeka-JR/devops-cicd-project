
from app import app


def test_homepage_returns_expected_message():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == (
        "Hello from my DevOps CI/CD project!"
    )
