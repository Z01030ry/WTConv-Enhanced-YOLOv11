import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
     model = YOLO(r"D:/project/WTConv-Enhanced YOLOv11 for Robust Blood Cell Cancer Detection/ultralytics-main/ultralytics/cfg/models/11/yolo11.yaml")
     model.train(data=r"cell_dataset/data.yaml",
                # 如果大家任务是其它的'ultralytics/cfg/default.yaml'找到这里修改task可以改成detect, segment, classify, pose
                task='detect',
                cache=False,
                imgsz=640,
                epochs=200,
                single_cls=False,  # 是否是单类别检测
                batch=16,
                close_mosaic=0,
                workers=4,
                device='0',
                optimizer='Adam', 
                resume=False, # 续训的话这里填写True
                amp=False,  # 如果出现训练损失为Nan可以关闭amp
                project='runs',
                name='runs/yolov11',
               )


