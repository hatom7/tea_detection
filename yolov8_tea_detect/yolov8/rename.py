import os

def rename():
    i = 832
    path = r"E:/teaproject/data/sunqidi/jpg"

    filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
    filelist.sort(key=lambda x: int(x[3:-5]))
    for files in filelist:   #遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)    #原来的文件路径
        print(Olddir)
        if os.path.isdir(Olddir):       #如果是文件夹则跳过
                continue
        filename = 'tea_'     #文件名
        filetype = '.jpg'        #文件扩展名
        Newdir = os.path.join(path, filename + str(i) + filetype)   #新的文件路径
        os.rename(Olddir, Newdir)    #重命名
    return True

if __name__ == '__main__':
    rename()