import os 
import shutil
import glob
os.chdir("C:\\Users\\shrey\\Downloads")
print(os.listdir())
documents=['*.txt*','*.pdf*','*.doc*','*.ppt*','*.rtf']
docs=[]
for filetype in documents:
    docst=glob.glob(filetype)
    if(len(docst)>0):
        docs.append(docst)

for docus in docs:
    for docis in docus:
        new_path='D:\\Documents\\' + docis
        shutil.move(docis, new_path)
images=['*.jpeg','*.jpg*','*.png*','*.bmp*']
imgs=[]
for filetype in images:
    imgst=glob.glob(filetype)
    if(len(imgst)>0):
        imgs.append(imgst)

for imgus in imgs:
    for imgis in imgus:
        new_path='D:\\Images\\' + imgis
        shutil.move(imgis, new_path)
videos=['*.mkv','*.webm','*.avi','*.m4p','*.amv','*.m4v']
vids=[]
for filetype in videos:
    vidst=glob.glob(filetype)
    if(len(vidst)>0):
        vids.append(vidst)

for vidus in vids:
    for vidis in vidus:
        new_path='D:\\Videos\\' + vidis
        shutil.move(vidis,new_path)
music=['*.flac','*.mp3','*.wav','*.mp4','*.wma']
musics=[]
for filetype in music:
    musict=glob.glob(filetype)
    if(len(musict)>0):
        musics.append(musict)

for musus in musics:
    for musis in musus:
        new_path='D:\\Music\\' + musis
        shutil.move(musis,new_path)
archives=['*.zip','*.rar','*.7z','*.tar*']
archs=[]
for filetype in archives:
    archst=glob.glob(filetype)
    if(len(archst)>0):
        archs.append(archst)

for archus in archs:
    for archis in archus:
        new_path='D:\\Archives\\'+ archis
        shutil.move(archis,new_path)

softwares=glob.glob('*.exe')

for softs in softwares:
    new_path='D:\\Softwares\\' + softs
    shutil.move(softs,new_path)