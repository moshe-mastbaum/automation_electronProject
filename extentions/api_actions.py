import allure
import requests

header = {'Content-Type': 'application/json'}
# key='239f970841ad8da42495c29e20a84517'
# url='http://api.exchangeratesapi.io/v1/latest'
boi_url='https://www.boi.org.il/currency.xml'

class ApiActions:
    @staticmethod
    @allure.step('get raquest')
    def get(path):
        response = requests.get(path)
        return response

    @staticmethod
    @allure.step('post raquest')
    def post(path, payload):
        response = requests.post(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('put raquest')
    def put(path, payload):
        response = requests.put(path, json=payload, headers=header)
        return response.status_code

    @staticmethod
    @allure.step('post raquest')
    def delete(path):
        response = requests.delete(path , headers=header)
        return response.status_code

    @staticmethod
    @allure.step('extract value from response')
    def extract_value_from_response(response, nodes):
        extract_value = None
        response_json = response.json()
        match len(nodes):
            case 1:
                extract_value=response_json[nodes[0]]
            case 2:
                extract_value=response_json[nodes[0]][nodes[1]]
            case 3:
                extract_value=response_json[nodes[0][1][2]]
        return extract_value

    @staticmethod
    @allure.step('dolar rate boi')
    def get_dollar_rate():
        response = requests.get(boi_url, 'curr:01')
        return response
