import requests
def download_songs(URL,Name):
    res = requests.get(URL)
    # 发出请求，并把返回的结果放在变量res中
    photo = open(Name+".mp3",'wb')
    # 新建了一个文件Be careful.jpg，这里的文件没加路径，会被保存在程序运行的当前目录下。
    photo.write(res.content)
    # 将 Reponse 对象的内容以 [二进制数据] 的形式写入文件
    photo.close()
    # 关闭文档
def test():
    URL = 'http://m701.music.126.net/20230228173929/f939071b6aa8849a80d909f0eab28408/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/8937223526/6fc5/c88d/0969/8e5d43f28e30ac13e9ec60e3da828bd2.mp3'
    Name = "Beyong"
    download_songs(URL,Name)
