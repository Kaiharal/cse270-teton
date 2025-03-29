import requests

BASE_URL = "https://kaiharal.github.io/cse270-teton/users"

def test_invalid_credentials(mocker):
    """Test that using 'admin'/'admin' results in 401 Unauthorized with an empty response."""
    
    # Mock the requests.get to return a 401 response with an empty body
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mocker.patch('requests.get', return_value=mock_response)
    
    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(BASE_URL, params=params)

    # Assert HTTP status code is 401 (Unauthorized)
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Assert response body is empty
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"

def test_valid_credentials(mocker):
    """Test that using 'admin'/'qwerty' results in 200 OK with an empty response."""
    
    # Mock the requests.get to return a 200 response with an empty body
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mocker.patch('requests.get', return_value=mock_response)
    
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(BASE_URL, params=params)

    # Assert HTTP status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Assert response body is empty
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"
