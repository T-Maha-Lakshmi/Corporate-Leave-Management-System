def test_home(client):
    res = client.get("/")
    assert res.status_code == 200


def test_register_employee(client):
    res = client.post(
        "/register",
        json={
            "username": "employee_test_1",
            "password": "Strong@123",
            "role": "employee"
        }
    )
    assert res.status_code == 200


def test_login_employee(client):
    # Ensure user exists
    client.post(
        "/register",
        json={
            "username": "employee1",
            "password": "Strong@123",
            "role": "employee"
        }
    )

    res = client.post(
        "/login",
        json={
            "username": "employee1",
            "password": "Strong@123"
        }
    )

    assert res.status_code == 200
    assert "role" in res.json()

