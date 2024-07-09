import os
import cv2


def main():
	# 总的检测根目录
    path_root_labels = 'E:/teaproject/data/tea/labels/'
    # 总的检测根目录
    path_root_imgs ='E:/teaproject/data/tea/images/'
    type_object = '.txt'

    # 设定两个文件夹路径
    # img_folder = 'E:/teaproject/data/sunqidi/jpg'
    # txt_folder = 'E:/teaproject/data/sunqidi/txt'
    #
    # # 获取两个文件夹的文件列表
    # img_files = set(os.listdir(img_folder))
    # txt_files = set(os.listdir(txt_folder))
    #
    # # 将图片列表中的每个文件名转为.txt文件名，用于比较
    # img_files_txt = {file.replace('.jpg', '.txt') for file in img_files}
    #
    # # 找出txt文件夹中存在但图片文件夹中缺失的文件
    # missing_files = txt_files - img_files_txt
    #
    # print(f'Missing files: {missing_files}')
    #
    for ii in os.walk(path_root_imgs):
        for j in ii[2]:
            type = j.split(".")[1]
            if type != 'jpg':
                continue
            path_img = os.path.join(path_root_imgs, j)
            print(path_img)
            label_name = j[:-4]+type_object
            path_label = os.path.join(path_root_labels, label_name)
            # print(path_label)
            f = open(path_label, 'r+', encoding='utf-8')
            if os.path.exists(path_label) == True:

                img = cv2.imread(path_img)
                w = img.shape[1]
                h = img.shape[0]
                new_lines = []
                img_tmp = img.copy()
                while True:
                    line = f.readline()
                    if line:
                        msg = line.split(" ")
                        # print(x_center,",",y_center,",",width,",",height)
                        x1 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center - width/2
                        y1 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # y_center - height/2
                        x2 = int((float(msg[1]) + float(msg[3]) / 2) * w)  # x_center + width/2
                        y2 = int((float(msg[2]) + float(msg[4]) / 2) * h)  # y_center + height/2
                        print(x1,",",y1,",",x2,",",y2)
                        cv2.rectangle(img_tmp,(x1,y1),(x2,y2),(0,0,255),5)
                    else :
                        break
            cv2.imshow("show", img_tmp)
            c = cv2.waitKey(0)

    #path_img = os.path.join(path_root_imgs, j)
    # print(path_root_imgs)
    # # print(path_label)
    # f = open(path_root_labels, 'r+', encoding='utf-8')
    # if os.path.exists(path_root_labels) == True:
    #
    #     img = cv2.imread(path_root_imgs)
    #     w = img.shape[1]
    #     h = img.shape[0]
    #     new_lines = []
    #     img_tmp = img.copy()
    #     while True:
    #         line = f.readline()
    #         if line:
    #             msg = line.split(" ")
    #             # print(x_center,",",y_center,",",width,",",height)
    #             x1 = int((float(msg[1]) - float(msg[3]) / 2) * w)  # x_center - width/2
    #             y1 = int((float(msg[2]) - float(msg[4]) / 2) * h)  # y_center - height/2
    #             x2 = int((float(msg[1]) + float(msg[3]) / 2) * w)  # x_center + width/2
    #             y2 = int((float(msg[2]) + float(msg[4]) / 2) * h)  # y_center + height/2
    #             print(x1, ",", y1, ",", x2, ",", y2)
    #             cv2.rectangle(img_tmp, (x1, y1), (x2, y2), (0, 0, 255), 5)
    #         else:
    #             break
    # cv2.namedWindow("show", 0);
    # cv2.resizeWindow("show", 640, 480);
    # cv2.imshow("show", img_tmp)
    # c = cv2.waitKey(0)

if __name__ == '__main__':
    main()


