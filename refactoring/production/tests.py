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
            ,data = province_data
        )
        self.response_201()
        response_data = self.last_response.json()["data"]["province_code"]
        self.assertEqual(response_data, "Asia")
        
        preduser_data_1 = dict(
                province_code = "Asia", name="Byzantium", cost=10, production=9
            )
        preduser_data_2 = dict(
                province_code = "Asia", name="Attalia", cost=12, production=10
            )
        preduser_data_3 = dict(
                province_code = "Asia", name="Sinope", cost=10, production=6
            )

        self.post("/producer"
            , data=preduser_data_1
        )
        self.response_201()

        self.post("/producer"
            , data=preduser_data_2
        )
        self.response_201()
        self.post("/producer"
            , data= preduser_data_3
        )
        self.response_201()


        self.get("/producer/"+self.province_data.code)
        self.response_200()
        response_data =  len(self.last_response.json()["data"])
        self.assertEqual(response_data, 3)


class GetShortFallDataTestCase(CreateProvinceDataTestCase):
    def short_fall_test(self):
        self.get("/producer/shortfall/"+self.province_data.code)
        self.response_200()
        response_data = self.last_response.json()["data"]["shorfall"]
        self.assertEqual(response_data, 5)