from flask import Flask, request, jsonify, render_template,Response
import os
from flask_cors import CORS, cross_origin
from apparel.utils.utils import decodeImage
from apparel.predictor_yolo_detector.detector_test import Detector


app = Flask(__name__)
CORS(app)


# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.objectDetection = Detector(self.filename)


@app.route("/")
def home():
    return render_template("index.html")

#Here we are sending data and receiving data from flask server via API(i.e postman)
@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        #In the image variable we have extracted base64 string of original image.
        #the request.json attribute is used to extract the image field from the JSON payload sent to the Flask server.
        image = request.json['image'] #Uploaded image is received here.
        #Functions  decodeImage() and clApp.objectDetection.detect_action() are being runned on Flask server.
        decodeImage(image, clApp.filename)#Decoding that particular image using decodeImage function.
        #At the end of the decodeImage function we are saving the image at a particular path.
        result = clApp.objectDetection.detect_action()#Pass it for prediction.
        #Detection happens. we get predicted image. we will encode it using encodeImageIntoBase64 function and return a dictionary of encoded image.
    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)#Result which is a dictionary is jasonified



if __name__ == "__main__":
    clApp = ClientApp()
    port = 9500
    app.run(host='0.0.0.0', port=port)