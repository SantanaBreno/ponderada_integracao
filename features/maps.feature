Feature: Consulta de localização pelo Google Maps API

  Scenario: Obter endereço válido pelo Google Maps
    Given que eu tenho a API em execução
    When eu envio a latitude "-23.55052" e longitude "-46.633308"
    Then eu recebo o endereço correspondente "São Paulo, SP, Brasil"

  Scenario: Latitude e longitude inválidas
    Given que eu tenho a API em execução
    When eu envio a latitude "999" e longitude "999"
    Then eu recebo um erro "Endereço não encontrado"
