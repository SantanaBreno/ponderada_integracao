import requests
from behave import given, when, then

BASE_URL = "http://localhost:8000/maps/location"

@given("que eu tenho a API em execução")
def step_api_running(context):
    context.base_url = BASE_URL

@when('eu envio a latitude "{lat}" e longitude "{lon}"')
def step_send_coordinates(context, lat, lon):
    params = {"lat": lat, "lon": lon}
    context.response = requests.get(context.base_url, params=params)

@then('eu recebo o endereço correspondente "{expected_address}"')
def step_verify_address(context, expected_address):
    assert context.response.status_code == 200
    data = context.response.json()
    assert data["address"] == expected_address, f"Esperado: {expected_address}, Obtido: {data['address']}"

@then('eu recebo um erro "{error_message}"')
def step_verify_error(context, error_message):
    assert context.response.status_code == 404
    data = context.response.json()
    assert data["detail"] == error_message, f"Esperado: {error_message}, Obtido: {data['detail']}"
