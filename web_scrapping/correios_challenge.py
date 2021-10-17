from selenium import webdriver
from bs4 import BeautifulSoup
from decouple import config
from time import sleep


class Correios:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=config("CWB"))

    def execute(self, cep):
        self.driver.get(
            "https://buscacepinter.correios.com.br/app/endereco/index.php?t"
        )
        # inputa as informações digitadas acima na página e pesquisa
        self.driver.find_element_by_id("endereco").send_keys(cep)
        self.driver.find_element_by_id("btn_pesquisar").click()
        sleep(3)
        # Extração de dados do resultado encontrado
        html = self.driver.page_source
        parsed_html = BeautifulSoup(html, "lxml")
        tbody = parsed_html.find("tbody")
        td = tbody.find_all("td")
        street_name = td[0].text.strip()
        district = td[1].text.strip()
        city_state = td[2].text.strip()

        # Apresentação do resultado encontrado
        print(
            f"Segue abaixo resultado retornado para o CEP pesquisado:\n \nLogradouro/Nome: {street_name}\nBairro/Distrito: {district}\nLocalidade/UF: {city_state}"
        )


# Solicita ao usuário que digite o CEP desejado e executa o script.
cep = int(input("Digite seu CEP: "))
bot = Correios()
bot.execute(cep)