import requests
import json

link = 'https://loja-71e6a-default-rtdb.firebaseio.com/'

# dados = {
#     "produto":"teclado",
#     "preco": 100,
#     "quantiade": 10
# }
# req = requests.post(f'{link}Produtos/.json', data=json.dumps(dados))
# print(req)
# print(req.text)


dados = {
    "produto":"mouse",
    "preco": 100,
    "quantiade": 10
}
req = requests.patch(f'{link}Produtos/-OJz6qr1KkD2KhMpx-Av/.json', data=json.dumps(dados))
print(req)
print(req.text)