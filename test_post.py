import requests

# Header for request
headers = {"Authorization": "Token bdcff5089c1421c44e860ebd5a5ccefff6e07571"}

# URL base
url_base_courses = "http://localhost:8000/api/v2/courses/"
url_base_evaluations = "http://localhost:8000/api/v2/evaluations/"

# Json New Course
new_course = {
    "title": "Curso de Teste de software",
    "url": "http://www.google.com/testesoft"
}

# Request Courses
course = requests.post(url=url_base_courses, headers=headers,    data=new_course)

# Test Endpoint Courses POST
assert course.status_code == 201

assert course.json()["title"] == new_course["title"]


# Json New Evaluation
new_evaluation = {
    "course": course.json()["id"],
	"name": "Jose",
	"email": "jose@gmail.com",
	"comment": "Bom",
	"note": "5"
}

# Request Evaluations
evaluation = requests.post(url=url_base_evaluations, headers=headers, data=new_evaluation)

# Test Endpoint Evaluations GET
assert evaluation.status_code == 201

assert evaluation.json()["course"] == new_evaluation["course"]

assert evaluation.json()["name"] == new_evaluation["name"]