from ultralytics import YOLO

model = YOLO('best.pt')

image_path = input()

model.predict(source=image_path, show=True, save=True)


