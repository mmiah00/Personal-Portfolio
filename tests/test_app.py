import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

# test_db = SqliteDatabase(':memory:')

class AppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<li><a href="/">Home</a></li>' in html
        assert '<li><a href="/experience">Experience</a></li>' in html
        assert '<li><a href="/education">Education</a></li>' in html
        assert '<li><a href="/hobbies">Hobbies</a></li>' in html
        assert '<li><a href="/myMap">Map</a></li>' in html
        assert '<link lang="sass" rel="stylesheet" href="./static/styles/main.css" />' in html
        assert '<img src="static/img/Maisha Headshot.jpg" alt="profile picture" width = 75% height = 75% aling="center" border-radius=50%>' in html
        assert '<h1> Maisha Miah </h1>' in html
        response2 = self.client.get("/static/styles/main.css")
        assert response2.status_code == 200 or 304
        response2.close()
        response3 = self.client.get("/static/img/Maisha%20Headshot.jpg")
        assert response3.status_code == 200 or 304
        response3.close()
        #Add more tests relating to the home page

    def test_experience(self):
        response = self.client.get("/experience")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        response2 = self.client.get("/static/styles/main.css")
        assert response2.status_code == 200 or 304
        response2.close()
        assert '<div class="experience">' in html
        assert "<h1> Work Experience </h1>" in html
        assert '<p style="font-size:25px"> Quadruped Robot | Boston University </p>' in html
        assert '<p style="font-size:25px"> Citi Early ID Leadership Program | Citi Bank </p>' in html
        assert '<p style="font-size:25px"> Hack4Impact | Boston University </p>' in html
        assert '<p style="font-size:25px"> JP Morgan Chase Software Engineering Virtual Experience | JP Morgan Chase </p>' in html
        assert '<p style="font-size:25px"> Archaeology Office | Boston University </p>' in html
        assert '<p style="font-size:25px"> Macy’s Fine Jewelry Department | Macy’s </p>' in html
        #Add more tests relating to the home page

    def test_education(self):
        response = self.client.get("/education")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        response2 = self.client.get("/static/styles/main.css")
        assert response2.status_code == 200 or 304
        response2.close()
        response3 = self.client.get("/static/img/portfolio-stuy.png")
        assert response3.status_code == 200 or 304
        response3.close()
        response4 = self.client.get("/static/img/portfolio-bu.png")
        assert response4.status_code == 200 or 304
        response4.close()
        assert ' <h4><b>Stuyvesant High School</b></h4>' in html
        assert '<h4><b>Boston University</b></h4>' in html

    def test_hobbies(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        response2 = self.client.get("/static/styles/main.css")
        assert response2.status_code == 200 or 304
        response2.close()
        response3 = self.client.get("/static/img/portfolio-baking.jpg")
        assert response3.status_code == 200 or 304
        response3.close()
        response4 = self.client.get("/static/img/portfolio-fishing.jpg")
        assert response4.status_code == 200 or 304
        response4.close()
        response5 = self.client.get("/static/img/portfolio-watchingsoccer.jpg")
        assert response5.status_code == 200 or 304
        response5.close()
        response6 = self.client.get("/static/img/portfolio-city.jpg")
        assert response6.status_code == 200 or 304
        response6.close()
        assert '<h1> Hobbies </h1>' in html
        assert '<h4><b>Baking</b></h4>' in html
        assert '<h4><b>Fishing</b></h4>' in html
        assert '<h4><b>Watching Soccer</b></h4>' in html
        assert '<h4><b>Exploring the City</b></h4>' in html

    def test_map(self):
        response = self.client.get("/myMap")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        response2 = self.client.get("/static/styles/main.css")
        assert response2.status_code == 200 or 304
        response2.close()
        assert '<iframe src="https://www.google.com/maps/d/u/0/embed?mid=1_HkTMicJL1EgApHiWbjd6fpw27vy_Jg&ehbc=2E312F" width="640" height="480"></iframe>' in html
        assert '<li class="card"> New York City </li>' in html
        assert '<li class="card"> Boston </li>' in html
        assert '<li class="card"> Washington DC </li>' in html 
        assert '<li class="card"> Connecticut </li>' in html 
        assert '<li class="card"> New Jersey </li>' in html 
        assert '<li class="card"> Pocono Mountains, Pennsylvania </li>' in html 
        assert '<li class="card"> Newport, Rhode Island </li>' in html 
        assert '<li class="card"> Philadelphia, Pennsylvania </li>' in html 
        assert '<li class="card"> Hershey Park, Pennsylvania </li>' in html 
        assert '<li class="card"> London, UK </li>' in html 
        assert '<li class="card"> Dubai, UAE </li>' in html 
        assert '<li class="card"> Dhaka, Bangladesh </li>' in html 

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        # if len(json["timeline_posts"]) ==1:
        #     nid1 = json["timeline_posts"][0]["id"]
        #     nid1 = str(nid1)
        #     respD2 = self.client.delete("/api/timeline_post/" + nid1)
        #     assert respD2.status_code == 200
        response1 = self.client.get("/api/timeline_post")
        assert response1.status_code == 200
        assert response1.is_json
        json1 = response1.get_json()
        assert len(json1["timeline_posts"]) == 0
        test_post = {"name": "John", "email": "odjncdc@gmail.com", "content": "dnovnw"}
        resp = self.client.post("/api/timeline_post", data=test_post)
        assert resp.status_code == 200
        response2 = self.client.get("/api/timeline_post")
        assert response2.status_code == 200
        assert response2.is_json
        json2 = response2.get_json()
        assert "timeline_posts" in json2
        assert len(json2["timeline_posts"]) == 1
        nid = json2["timeline_posts"][0]["id"]
        nid = str(nid)
        # respD = self.client.delete("/api/timeline_post/" + nid)
        # assert respD.status_code == 200
        response3 = self.client.get("/api/timeline_post")
        assert response3.status_code == 200
        assert response3.is_json
        json3 = response3.get_json()
        assert "timeline_posts" in json3
        # assert len(json3["timeline_posts"]) == 0
        
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert '<label for="name"> Name </label>' in html
        # assert '<input name="name" type="text" id="name">' in html
        assert '<label for="email"> Email </label>' in html
        # assert '<input name="email" type="text" id="email">' in html
        assert '<label for="content"> Content </label>' in html
        # assert '<input name="content" type="text" id="content">' in html 
        assert '<button type="submit">Submit</button>' in html
        
    def test_malformed_timeline_post(self):
        #POST request missing name
        response = self.client.post("/api/timeline_post", data= {"email": "john@example.com", "content": "Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        #POST request with empty content
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe","email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        #POST request with malformed email
        response = self.client.post("/api/timeline_post", data= {"name": "John Doe","email": "not-an-email", "content": "Hello World, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html