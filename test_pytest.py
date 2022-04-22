# >> pytest test_pytest.py
import requests


class TestCourses:
    headers = {"Authorization": "Token 171b60e53c6d4aa5f5ca3c7d2c62dbf6503b8aff"}
    url_base_courses = "http://localhost:8000/api/v2/courses/"

    def test_get_courses(self):
        response = requests.get(self.url_base_courses)

        assert response.status_code == 200

    def test_post_course(self):
        new = {
            "title": "Curso Pytest",
            "url": "http://www.google.com/course_pytest"
        }

        response = requests.post(url=self.url_base_courses, headers=self.headers, data=new)

        assert response.status_code == 201
        assert response.json()["title"] == new["title"]

    def test_get_course(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        response = requests.get(f"{self.url_base_courses}{id_course}/")

        assert response.status_code == 200

    def test_get_course_evaluations(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        response = requests.get(f"{self.url_base_courses}{id_course}/evaluations/")

        assert response.status_code == 200

    def test_put_course(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        update = {
            "title": "Curso Pytest 2",
            "url": "http://www.google.com/course_pytest2"
        }

        response = requests.put(url=f"{self.url_base_courses}{id_course}/", headers=self.headers, data=update)

        assert response.status_code == 200

    def test_put_course_title(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        update = {
            "title": "Curso Pytest 3",
            "url": "http://www.google.com/course_pytest3"
        }

        response = requests.put(url=f"{self.url_base_courses}{id_course}/", headers=self.headers, data=update)

        assert response.json()["title"] == update["title"]

    def test_patch_course(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        update = {
            "title": "Curso Pytest Patch"
        }

        response = requests.patch(url=f"{self.url_base_courses}{id_course}/", headers=self.headers, data=update)

        assert response.status_code == 200
        assert response.json()["title"] == update["title"]

    def test_delete_course(self):
        courses = requests.get(self.url_base_courses)
        id_course = courses.json()["results"][-1]["id"]

        response = requests.delete(url=f"{self.url_base_courses}{id_course}/", headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0


class TestEvaluations:
    headers = {"Authorization": "Token 171b60e53c6d4aa5f5ca3c7d2c62dbf6503b8aff"}
    url_base_evaluations = "http://localhost:8000/api/v2/evaluations/"
    url_base_courses = "http://localhost:8000/api/v2/courses/"

    def test_get_evaluations(self):
        response = requests.get(url=self.url_base_evaluations, headers=self.headers)

        assert response.status_code == 200
    
    def test_post_evaluation(self):
        evaluations = requests.get(url=self.url_base_courses, headers=self.headers)
        course = evaluations.json()["results"][-1]["id"]

        new = {
            "course": course,
            "name": "Jose",
            "email": "jose@gmail.com",
            "comment": "Bom",
            "note": "5"
        }

        response = requests.post(url=self.url_base_evaluations, headers=self.headers, data=new)

        assert response.status_code == 201
        assert response.json()['name'] == new["name"]
    
    def test_get_evaluation(self):
        evaluations = requests.get(url=self.url_base_evaluations, headers=self.headers)
        id_evaluation = evaluations.json()["results"][-1]["id"]

        response = requests.get(url=f"{self.url_base_evaluations}{id_evaluation}/", headers=self.headers)

        assert response.status_code == 200

    def test_put_evaluation(self):
        evaluations = requests.get(url=self.url_base_evaluations, headers=self.headers)
        course = evaluations.json()["results"][-1]["course"]
        id_evaluation = evaluations.json()["results"][-1]["id"]

        update = {
            "course": course,
            "name": "Jose Silva",
            "email": "jose@gmail.com",
            "comment": "Bom",
            "note": 3
        }

        response = requests.put(url=f"{self.url_base_evaluations}{id_evaluation}/", headers=self.headers, data=update)

        assert response.status_code == 200
    
    def test_put_evaluation_name(self):
        evaluations = requests.get(url=self.url_base_evaluations, headers=self.headers)
        course = evaluations.json()["results"][-1]["course"]
        id_evaluation = evaluations.json()["results"][-1]["id"]

        update = {
            "course": course,
            "name": "Jose Silva",
            "email": "jose@gmail.com",
            "comment": "Bom",
            "note": 3
        }

        response = requests.put(url=f"{self.url_base_evaluations}{id_evaluation}/", headers=self.headers, data=update)

        assert response.json()["name"] == update["name"]
    
    def test_patch_evaluation(self):
        evaluations = requests.get(url=self.url_base_evaluations, headers=self.headers)
        id_evaluation = evaluations.json()["results"][-1]["id"]

        update = {
            "comment": "Ótimo",
            "note": 5
        }

        response = requests.patch(url=f"{self.url_base_evaluations}{id_evaluation}/", headers=self.headers, data=update)

        assert response.status_code == 200
        assert response.json()["comment"] == update["comment"]

    def test_delete_evaluation(self):
        evaluations = requests.get(url=self.url_base_evaluations, headers=self.headers)
        id_evaluation = evaluations.json()["results"][-1]["id"]

        response = requests.delete(url=f"{self.url_base_evaluations}{id_evaluation}/", headers=self.headers)

        assert response.status_code == 204 and len(response.text) == 0