import requests
from decimal import Decimal

class convertor:
    x = Decimal(input('please write a count of hrn what would you like to convert to dollars'))

    pars_res_list = []
    response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
    response_text = response.text
    response_parse = response_text.split("<tr>")
    for parse_elem_1 in response_parse:
        if parse_elem_1.strip().startswith("<td class=\"hidden-sm\" data-label=\"Код цифровий\"><span class=\"value\">840</span></td>"):
            for parse_elem_2 in parse_elem_1.split("</td>"):
                if parse_elem_2.strip().startswith("<td data-label=\"Офіційний курс\">"):
                    parse_elem_3 = Decimal(parse_elem_2.strip().replace("<td data-label=\"Офіційний курс\">", "").replace(",", "."))
                    print("It will be")
                    print(x / parse_elem_3)