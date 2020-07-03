from pixivpy3 import *
import json
from time import sleep
import os

api = PixivAPI()

f = open('./account.json', 'r')

account_info = json.load(f)

f.close()

# ログイン
api.login(account_info['pixiv_id'], account_info['password'])

artist_id = 1184799
# artist_name
user = api.users(artist_id).response[0].name

json_result = api.users_works(artist_id, per_page=300)
info = json_result.response[0]
score = info.stats.score

total_works = json_result.pagination.total
illust = json_result.response[0]

if not os.path.exists('./pixiv_images'):
    os.mkdir('./pixiv_images')
saving_directory_path = './pixiv_images/' + user

aapi = AppPixivAPI()

if not os.path.exists(saving_directory_path):
    os.mkdir(saving_directory_path)
for work_no in range(0, total_works):
    illust = json_result.response[work_no]
    print('Procedure: %d/%d' % (work_no + 1, total_works))
    print('Title: %s' % (illust.title))
    # file_name = str(work_no + 1) + '.png'
    aapi.download(illust.image_urls.large, saving_directory_path + '/')
    sleep(1)