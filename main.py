from pprint import pprint
import requests

# если токен ВК будет вводить не пользователь, можно прочитать из файла
# with open('VKtoken.txt','r') as file_object:
#     vk_token = file_object.read().strip()

vk_token_input = input(f'Введите токен  VK')
yd_token_input = input(f'Введите токен YD')


# создаю класс для записи из VK
class VkUser():
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    # функция получения фоток аватарок с VK
    def get_photos(self, user_id=None):
        get_photos_url = self.url + 'photos.get'
        get_photos_params = {
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
            'user_id': user_id
        }
        res = requests.get(get_photos_url, params={**self.params, **get_photos_params}).json()
        return res['response']

    # функция записи данных в файл json
    def write_data(self, file_name: str, mode: str = 'r', data: str = ''):
        with open(file_name, mode) as file:
            file.write(f'{data}\n')



# проверка
vk_client = VkUser(vk_token_input, '5.131')
# получить свои фотки
vk_client.get_photos()
# получить чьи-то фотки, указать id
vk_client.get_photos('1')

# записать данные в файл
JSON_FILE = 'json_photo.txt'
DATA = vk_client.get_photos()
pprint(DATA)
vk_client.write_data(JSON_FILE, 'w', DATA)



#шаблон кода из ДЗ по requests(не обработанный )
# from yadisk import Yadisk
#
# if __name__ == '__main__':
#     yadisk = Yadisk(yd_token_input)
#     res = yadisk._get_upload_link('/file.txt')
#     pprint(res)
#
#     yadisk.upload_file('/test.txt','file.txt')
#
#     res = yadisk._get_upload_link('/Tulips.jpg')
#     pprint(res)
#     yadisk.upload_file('/test_2.jpg', 'Tulips.jpg')
