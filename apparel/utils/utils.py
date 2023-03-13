import base64

#Saving the data that I got from UI  
#Decoding the image
def decodeImage(imgstring, fileName):#imgstring-->base64 string
    imgdata = base64.b64decode(imgstring)#Decoding the data and saving it in variable imgdatas
    with open("./com_ineuron_apparel/predictor_yolo_detector/inference/images/" + fileName, 'wb') as f:#opening the file
        f.write(imgdata) #writing the data that I have received from base64.
        f.close()


#Encode the image
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
