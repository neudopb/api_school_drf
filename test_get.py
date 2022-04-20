import requests

# Header for request
headers = {"Authorization": "Token bdcff5089c1421c44e860ebd5a5ccefff6e07571"}

# URL base
url_base_courses = "http://localhost:8000/api/v2/courses/"
url_base_evaluations = "http://localhost:8000/api/v2/evaluations/"

# Request Courses
courses = requests.get(url_base_courses)

# Test Endpoint Courses GET
assert courses.status_code == 200


# Request Evaluations
evaluations = requests.get(url=url_base_evaluations, headers=headers)

# Test Endpoint Evaluations GET
assert evaluations.status_code == 200