#import urllib.request
#opener=urllib.request.build_opener()
#response=opener.open("https://httpbin.org/get")
#print(response.read())



#import requests
#response=requests.get("https://coinmarketcap.com/")
#response_text=response.text
#response_parse=response_text.split("<span>")
#for parse_elem_1 in response_parse:
    #if parse_elem_1.startswith("$"):
        #print(parse_elem_1)


import requests
pars_res_list=[]
response=requests.get("https://coinmarketcap.com/")
response_text=response.text
response_parse=response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in response_parse.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)
                pars_res_list.append(parse_elem_2)
bitcoin=pars_res_list[0]
print(f"bitcoin - {bitcoin}")

Ethereum=pars_res_list[1]
print(f"Ethereum - {Ethereum}")

BNB=pars_res_list[3]
print(f"BNB - {BNB}")

Solana=pars_res_list[4]
print(f"Solana - {Solana}")

XRP=pars_res_list[5]
print(f"XRP - {XRP}")
