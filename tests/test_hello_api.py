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
        result = self.client.post("/api/v1/books", data=book,
        content_type="application/json")
        self.assertEqual(result.status_code, 201)

    def test_admin_delete_a_book(self):
        book = {"ISBN": "00001", "Title": "MacBeth", "Author": "Shakespear", "Date-Published": "12/10/2018",
            "category": "Good Reads"}
        result = self.client.delete(
            "/api/v1/books/<ISBN>", data=book,
            content_type="application/json")
        self.assertEqual(result.status_code, 204)

    def test_admin_can_edit_a_book(self):
        book = {"ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads"}
        response = self.client.put(
            "/api/v1/books/<bookid>", data=book,
            content_type="application/json")

        self.assertEqual(response.status_code, 201)

    def test_can_get_all_books(self):
        books = {"ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads",
                 "ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads",
                 "ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads",
                 "ISBN":"00001","Title":"MacBeth","Author":"Shakespear","Date-Published": "12/10/2018", "category": "Good Reads"}
        response = self.client.get(
            "/api/v1/book", data=books,
            content_type="application/json")
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()    