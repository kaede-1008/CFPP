from pixivpy3 import *
import json
from time import sleep
import os

api = PixivAPI()

# ???????????????
f = open('./json/account.json', 'r')
account_info = json.load(f)
f.close()

# ???????????????????
f = open('./json/artist.json')
artist_info = json.load(f)
f.close()

# pixiv??????
api.login(account_info['pixiv_id'], account_info['password'])

# artist_id = 1184799
# print(len(artist_info))

# artist_name
# user = api.users(artist_id).response[0]
# print(user)

for artist_num in range(len(artist_info)):

    json_result = api.users_works(artist_info[str(artist_num)], per_page=300)
    info = json_result.response[0]
    score = info.stats.score

    total_works = json_result.pagination.total
    illust = json_result.response[0]

    if not os.path.exists('./pixiv_images'):
        os.mkdir('./pixiv_images')
    saving_directory_path = './pixiv_images/' + str(artist_num)

    aapi = AppPixivAPI()

    if not os.path.exists(saving_directory_path):
        os.mkdir(saving_directory_path)
        for work_no in range(0, total_works):
            illust = json_result.response[work_no]
            # print('Procedure: %d/%d' % (work_no + 1, total_works))
            # print('Title: %s' % (illust.title))

            file_name = str(work_no) + '.' + illust.image_urls.large.split('.')[-1]
            # print(file_name)
            aapi.download(illust.image_urls.large, saving_directory_path + '/', fname=file_name)
            sleep(1)