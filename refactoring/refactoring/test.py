from test_plus import APITestCase


class CreateProvinceDataTestCase(APITestCase):
    def setUP(self):
        
        province_data = "Asis"
        self.post("/province"
            ,data = province_data
        )
        self.response_201()

        producer_data = list(
            dict(
                name="Byzantium", cost=10, production=9
            ),
            dict(
                name="Attalia", cost=12, production=10
            ),
            dict(
                name="Sinope", cost=10, production=6
            )
        )
        self.post("producer"
            , data=producer_data
        )
        self.response_201()

        self.get("/province/1")
        response_data = self.last_response.json()
        self.assertEqual(response_data, producer_data)