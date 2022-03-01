# Create your tests here.
from test_plus import APITestCase


class CreateProvinceDataTestCase(APITestCase):
    def test_province(self):
        
        province_code = "Asia"
        self.post("/province"
            ,data = dict(province_code = "Asia" )
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


        self.get("/producer/"+province_code)
        self.response_200()
        response_data =  len(self.last_response.json()["data"])
        self.assertEqual(response_data, 3)