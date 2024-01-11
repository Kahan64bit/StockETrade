"Temp file that is deleted after first execution"

def write_api(alpaca_api):
    f = open("api/config.py", "a")
    f.write(f"api_key_alpaca = \"{alpaca_api}\"\n" )
    f.write(f"secret_key = \"{secret_key}\"\n")


    
print("Paste your alpaca api key: ")
alpaca_api = str(input())
print("Paste your alpaca secret key")
secret_key = str(input())

write_api(alpaca_api)
