import unittest
import run
import json
from app import app

class TestHelloBooksApi(unittest.TestCase):
    
    def setUp(self):
        self.client = run.app.test_client()

    def test_admin_add_a_book(self):
        book = {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
        response = self.client.post("/api/v1/books", data=book,
        content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_admin_delete_a_book(self):
        book = {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
        response = self.client.delete(
            "/api/v1/books/<ISBN>", data=book,
            content_type="application/json")
        self.assertEqual(response.status_code, 204)

    def test_admin_can_edit_a_book(self):
        #tests if a the api can get a book and edit it 
        res = self.client().post("/api/v1/books/<bookid>", data=book,content_type="application/json")
        self.assertEqual(res.status_code,201)

        #convert response into json so as to get the id
        result_in_json=json.loads(res.data.decode('utf-8').replace("'", "\""))

        #this edits the current book
        put_request=self.client().put('/api/v1/books/<bookid>{}'.format(result_in_json['id']), data={"ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads"})

        self.assertEqual(put_request.status_code,200)



if __name__ == "__main__":
    unittest.main()    