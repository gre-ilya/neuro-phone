# БИЛД ЗАГРУЗИЛ НА https://disk.yandex.ru/d/XECxyHdP5XkUEw

# -*- coding: utf-8 -*-
import cv2, time, zipfile, os

stream = cv2.VideoCapture(0)
stream.set(cv2.CAP_PROP_FPS, 24) 
stream.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 768) 

prepare = int(input('Выбери, сколько секунд тебе нужно, чтобы подготовиться к фото (например «5» или «10»): '))
print(f'\nУ тебя будет {prepare} секунд на то, чтобы принять нужную позу. \nВнимание! Чтобы фотографии сохранились, обязательно заверши программу командой «2»\n')
key = input('\nЧтобы сделать фото, введи «1».\n')
if not(os.path.exists('Фотосессия')):
    os.mkdir('Фотосессия')
os.chdir('Фотосессия')
n = len(os.listdir())
if n <= 1:
    n=0
else:
    n=(n-1)//2
zip = zipfile.ZipFile('Фотосессия.zip', 'w')
for old_file in os.listdir():
    if old_file != 'Фотосессия.zip':
        zip.write(old_file)

while (stream.isOpened()):

    if key == '1':
        print('\nПредставь, что ты фотомодель — приготовься.')
        for i in range(prepare):
            time.sleep(1)
            print(f'{prepare-i}...')
        status, photo = stream.read()
        print('Попался, красавчик!')
        cv2.imshow(f'{n}.jpg', photo)
        if cv2.waitKey(10) == 27:
            break
        key = input('Чтобы сохранить фотографию, введи  «1». Если не хочешь ее сохранять, введи «2».\n') 
        if key == '1':            
            cv2.imwrite(f'{n}.jpg', photo)
            json = open(f'{n}.json', 'w+')
            json.write('[1, [0, 0, 0, 0]]')
            json.close()
            zip.write(f'{n}.jpg')       
            zip.write(f'{n}.json')     
            n+=1
            print('\nА у тебя есть вкус <3\n')
        else:
             print('\nТы чево наделол..\n')    

        key = input('\n- Снова нажми «1», чтобы сделать ещё фото; \n- Нажми «2», чтобы закончить и сохранить фотосессию.\n')             
        
    elif key == '2':
        zip.close()    
        print(f'\nСохранено!\nИщи свои фото по адресу {os.getcwd()}\Фотосессия.zip\n')
        os.startfile('Фотосессия.zip')
        break

    else:
        key = input('\nНе-а, только «1» или «2»\n')       
        
stream.release()
cv2.destroyAllWindows()        

input()
