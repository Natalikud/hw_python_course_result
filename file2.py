from pprint import pprint
import requests


class Yadisk:
    host = 'https://cloud-api.yandex.net:443'
    def __init__(self, token):
        self.token = token
        # self.host = 'https://cloud-api.yandex.net:443'
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth {self.token}'
                        }
#метод получения ссылки для записи моих файлов
    def _get_upload_link(self, path):
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = self.headers
        params = {'path': path, 'overwrite': True}
        response = requests.get(url, params=params, headers=headers)
        return response.json().get('href')

#метод, загружающий фотки на ЯндексДиск
    def upload_file(self, path, file_name):
        upload_link = self._get_upload_link(path)
        headers = self.headers
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=headers)

        response.raise_for_status()
        if response.status_code == 201:
            print('Sucsess')

