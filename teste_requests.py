import requests


# Header for request
token = "bdcff5089c1421c44e860ebd5a5ccefff6e07571"
headers = {"Authorization": f"Token {token}"}


# GET Courses
courses = requests.get("http://localhost:8000/api/v2/courses/")
print(courses.status_code)
"""
print(courses)
print(courses.json())
print(courses.json()["results"])
"""


# GET Course
course = requests.get("http://localhost:8000/api/v2/courses/1/")
print(course.status_code)
"""
print(course)
print(course.json())
"""


# GET Evaluations
evaluations = requests.get(url="http://localhost:8000/api/v2/evaluations/", headers=headers)
print(evaluations.status_code)
"""
print(evaluations)
print(evaluations.json())
print(evaluations.json()["results"])
"""


# GET Evaluations
evaluation = requests.get(url="http://localhost:8000/api/v2/evaluations/3/", headers=headers)
print(evaluation.status_code)
"""
print(evaluation)
print(evaluation.json())
"""