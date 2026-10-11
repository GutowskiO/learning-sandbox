from ultralytics import YOLO

model = YOLO('yolo26n.pt')

#results = model.predict("bc.jpg", save = True)
#results = model("pies.jpg", show=True, save = True)

#for box in results[0].boxes:
 #   cls = model.names[int(box.cls)]
  #  conf = float(box.conf)
   # x1, y1, x2, y2 = box.xyxy[0].tolist()
    #print(f"{cls} ({conf:.2f}): ({x1:.0f},{y1:.0f}) → ({x2:.0f},{y2:.0f})")



#model.train(data = "bc-data-set.ndjson", epochs = 2, imgsz = 640, batch = 8)

if __name__ == "__main__":
    model = YOLO("yolo11n.pt")   # use whatever checkpoint name you had
    model.train(data="bc-data-set.ndjson", epochs=50, imgsz=640, batch=8)