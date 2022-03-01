# Create your tests here.
from test_plus import APITestCase


class CreateProvinceDataTestCase(APITestCase):
    def setUp(self):
        self.province_data = dict(
            code = "Asia"
            ,demand = 30
            ,price = 20
        )
        self.post("/province"
            ,data = self.province_data
        )
        self.response_201()
        response_data = self.last_response.json()["data"]["province_code"]
        self.assertEqual(response_data, "Asia")
        
        self.preduser_data_list = [
            dict(
                province_code = "Asia", name="Byzantium", cost=10, production=9
            ),dict(
                province_code = "Asia", name="Attalia", cost=12, production=10
            ),dict(
                province_code = "Asia", name="Sinope", cost=10, production=6
            )
        ]

        self.post("/producer"
            , data=self.preduser_data_list[0]
        )
        self.response_201()

        self.post("/producer"
            , data=self.preduser_data_list[1]
        )
        self.response_201()
        self.post("/producer"
            , data= self.preduser_data_list[2]
        )
        self.response_201()


        self.get("/producer/"+self.province_data["code"])
        self.response_200()
        response_data =  len(self.last_response.json()["data"])
        self.assertEqual(response_data, 3)


class GetSalesDataTestCase(CreateProvinceDataTestCase):

    def test_shortfall(self):
        self.get("/province/shortfall/"+self.province_data["code"])
        self.response_200()
        response_data = self.last_response.json()["data"]["shortfall"]
        self.assertEqual(response_data, 5)

    def test_profit(self):
        self.get("/province/profit/"+self.province_data["code"])
        self.response_200()
        response_data = self.last_response.json()["data"]["profit"]
        self.assertEqual(response_data, 230)
