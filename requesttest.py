import requests

def main():
    url='https://api.a3rt.recruit-tech.co.jp/proofreading/v1/typo'
    payload = {'apikey':'TeZwLvpDPEqqyCfnU1nAkNEpxqWfxwwF','sentence':'明日は晴れです'}
    response=requests.get(url,params=payload)

    print(response)
    print(response.text)
    
if __name__ == '__main__':
    main()
