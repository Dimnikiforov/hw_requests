import requests


def test_requests():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api'
    command = '/all.json'
    response = requests.get(url=url + command)
    super_heroes = {'Hulk': '', 'Captain_America': '', 'Thanos': ''}
    super_heroes['Hulk'] = int(*[i['powerstats']['intelligence'] for i in response.json() if i['name'] in ['Hulk']])
    super_heroes['Captain_America'] = int(*[i['powerstats']['intelligence'] for i in response.json() if i['name'] in ['Captain America']])
    super_heroes['Thanos'] = int(*[i['powerstats']['intelligence'] for i in response.json() if i['name'] in ['Thanos']])
    print(f'Самый умный супергерой {max((super_heroes))}, его интеллект {max(super_heroes.values())}')


test_requests()

token = ''


class YaUploader:
    base_host = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def get_link(self, file_name):
        uri = 'v1/disk/resources/upload/'
        param = {'path': file_name, "overwrite": "true"}
        response = requests.get(url=self.base_host + uri, headers=self.get_headers(), params=param)
        return response.json()['href']

    def upload_file(self, path_to_file, file_name):
        href = self.get_link(file_name)
        response = requests.put(href, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print(f'файл {file_name} загружен успешно')
        return response.json()


ya = YaUploader(token)
ya.upload_file('\ew.txt', '\ew.txt')
