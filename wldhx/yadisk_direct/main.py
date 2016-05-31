from sys import argv
import requests

API_ENDPOINT = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={}'


def main():
    yad_url = argv[1]

    pk_request = requests.get(API_ENDPOINT.format(yad_url))

    print(pk_request.json()['href'])


if __name__ == '__main__':
    main()
