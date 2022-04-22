import requests

# Header for request
headers = {"Authorization": "Token bdcff5089c1421c44e860ebd5a5ccefff6e07571"}

# URL base
url_base_courses = "http://localhost:8000/api/v2/courses/"
url_base_evaluations = "http://localhost:8000/api/v2/evaluations/"

# Json Update Course
update_course = {
    "title": "Curso teste put",
    "url": "http://www.google.com/testeput"
}

# Request GET
courses = requests.get(url_base_courses)
id_course = courses.json()["results"][-1]["id"]

# Request Courses
course = requests.put(url=f"{url_base_courses}{id_course}/", headers=headers, data=update_course)

# Test Endpoint Courses PUT
assert course.status_code == 200

assert course.json()["title"] == update_course["title"]


# Json Update Evaluation
update_evaluation = {
    "course": course.json()["id"],
	"name": "Joao",
	"email": "joao@gmail.com",
	"comment": "Bom",
	"note": "5"
}

evaluations = requests.get(url_base_evaluations, headers=headers)
id_evaluation = evaluations.json()["results"][-1]["id"]

# Request Evaluations
evaluation = requests.put(url=f"{url_base_evaluations}{id_evaluation}/", headers=headers, data=update_evaluation)

# Test Endpoint Evaluations PUT
assert evaluation.status_code == 200

assert evaluation.json()["course"] == update_evaluation["course"]

assert evaluation.json()["name"] == update_evaluation["name"]