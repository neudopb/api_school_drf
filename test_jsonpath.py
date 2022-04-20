import requests
import jsonpath


# GET Courses
courses = requests.get("http://localhost:8000/api/v2/courses/")

results = jsonpath.jsonpath(courses.json(), "results")
print(results)

first = jsonpath.jsonpath(courses.json(), "results[0]")
print(first)

title = jsonpath.jsonpath(courses.json(), "results[0].title")
print(title)

# All courses titles
titles = jsonpath.jsonpath(courses.json(), "results[*].title")
print(titles)