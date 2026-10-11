from ultralytics import YOLO

model = YOLO(r"runs/detect/train-5/weights/best.pt")
results = model.predict(r"pies_test.jpg", save=True, show = True)

for box in results[0].boxes:
    name = results[0].names[int(box.cls)]
    print(name, float(box.conf))