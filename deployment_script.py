from ultralytics import YOLO

model = YOLO(r'best.pt')

model.predict(source=r"v1_coins_no_3.jpg", classes=[0,1], show=True, save=True)