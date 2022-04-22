import requests

# Header for request
headers = {"Authorization": "Token 171b60e53c6d4aa5f5ca3c7d2c62dbf6503b8aff"}

# URL base
url_base_courses = "http://localhost:8000/api/v2/courses/"
url_base_evaluations = "http://localhost:8000/api/v2/evaluations/"


# Request GET
courses = requests.get(url_base_courses)
id_course = courses.json()["results"][-1]["id"]

# Request Courses
course = requests.delete(url=f"{url_base_courses}{id_course}/", headers=headers)

# Test Endpoint Courses DELETE
assert course.status_code == 204

assert len(course.text) == 0


evaluations = requests.get(url_base_evaluations, headers=headers)
id_evaluation = evaluations.json()["results"][-1]["id"]

# Request Evaluations
evaluation = requests.delete(url=f"{url_base_evaluations}{id_evaluation}/", headers=headers) # SuperUser

# Test Endpoint Evaluations PUT
assert evaluation.status_code == 204

assert len(evaluation.text) == 0