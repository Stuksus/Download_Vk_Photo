import vk_api
import requests
import os
import math
import time
step =0
count = 0
flag = True
idBegin = int(input('Введите ваш ID: '))
login = input('Введите ваш login: ')
password = input('Введите ваш password: ')
vkSession = vk_api.VkApi('+'+login,password,scope=4)
vkSession.auth()
vk = vkSession.get_api()
photos = vk.photos.getAll(owner_id =idBegin)
info = vk.users.get(user_id = idBegin)
def uploadFile (ids):
    os.mkdir(str(ids))
    realCount = photos['count']
    if photos['count']>200:
        step = math.ceil(photos['count']/200)
        flag=False
    else:
        step = 1
        count = photos['count']
        flag = True
    massForPhoto = []
    while step > 0:
        if flag == False:
            if realCount > 200:
                count = 200
                realCount = photos['count']-200
            else:
                count = realCount
        photosInDef = vk.photos.getAll(owner_id=ids,count = count)
        for ph in photosInDef['items']:
            if 'photo_2560'in ph:
                massForPhoto.append(ph['photo_2560'])
            elif 'photo_1280'in ph:
                massForPhoto.append(ph['photo_1280'])
            elif 'photo_807' in ph:
                massForPhoto.append(ph['photo_807'])
            elif 'photo_604' in ph:
                massForPhoto.append(ph['photo_604'])
            elif 'photo130' in ph:
                massForPhoto.append(ph['photo_130'])
            elif 'photo_75' in ph:
                massForPhoto.append(ph['photo_75'])
        step-=1
    start = time.time()
    for img in range(0,len(massForPhoto)):
        p = requests.get(massForPhoto[img])
        out = open(str(ids) + "/" + str(img) + ".jpg", "wb")
        out.write(p.content)
        out.close()
    print(time.time()-start)
    flag=True

uploadFile(idBegin)
os.system("pause")