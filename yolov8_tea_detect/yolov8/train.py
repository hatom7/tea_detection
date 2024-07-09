from ultralytics import YOLO
import cv2
from cv2 import getTickCount, getTickFrequency
from multiprocessing import freeze_support
# Load a model
#model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("D:\百度网盘下载\yolov8\yolov8\\runs\detect\\train4\weights\\best.pt")  # load a pretrained model (recommended for training)

# Use the model
#model.train(data="E:/papercode/yolov8/ultralytics/cfg/datasets/tea.yaml", epochs=50, imgsz=640)  # train the model
#metrics = model.val()  # evaluate model performance on the validation set
#results = model("")  # predict on an image
#path = model.export(format="onnx")  # export the model to ONNX format
if __name__ == '__main__':
    freeze_support()
    # 获取摄像头内容，参数 0 表示使用默认的摄像头
    cap = cv2.VideoCapture(1)

    while cap.isOpened():
        loop_start = getTickCount()
        success, frame = cap.read()  # 读取摄像头的一帧图像

        if success:
            results = model.predict(source=frame)  # 对当前帧进行目标检测并显示结果
        annotated_frame = results[0].plot()

        # 中间放自己的显示程序
        loop_time = getTickCount() - loop_start
        total_time = loop_time / (getTickFrequency())
        FPS = int(1 / total_time)
        # 在图像左上角添加FPS文本
        fps_text = f"FPS: {FPS:.2f}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        font_thickness = 2
        text_color = (0, 0, 255)  # 红色
        text_position = (10, 30)  # 左上角位置

        cv2.putText(annotated_frame, fps_text, text_position, font, font_scale, text_color, font_thickness)
        cv2.imshow('img', annotated_frame)
        # 通过按下 'ESC' 键退出循环
        if cv2.waitKey(1) == 27:  # 按下 Esc退出
            break
    cap.release()  # 释放摄像头资源
    cv2.destroyAllWindows()  # 关闭OpenCV窗口
    # results = model.train(data="E:/papercode/yolov8/ultralytics/cfg/datasets/tea.yaml", epochs=50, imgsz=640)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set
    # results=model.predict(source=0)







