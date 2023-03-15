import requests


class MockTest:
    def __init__(self, url, request_params1):
        self.url = url
        self.request_params1 = request_params1
        self.request_headers = {}

    def MockPort1(self):
        result = requests.get(url=self.url, params=self.request_params1, headers=self.request_headers, verify=False).text

        return result


if __name__ == '__main__':
    # obj = MockTest("https://mockapi.eolink.com/PE7cd7e93684a74e31d09980ae8c1b1fe10512d7b9ed829/api/personal/dashboard/sales/ranking?orderBy=qty&date=2023-03",'')
    obj = MockTest("http://192.168.110.13:8088/shopping_cart", '')
    print(obj.MockPort1())
