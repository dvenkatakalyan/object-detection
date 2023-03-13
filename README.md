
# object detection web app

object detection using yolov5 and deploying it using Flask framework.


## Flow chart
## Appendix

1) Using the upload button on webpage the user uploads the image in which objects need to be detected.

2) Code for encoding and decoding is written in utils.py 

3) Image is converted to Base64 format using decoding function.

4) Passing it for prediction through yolov5.yolov5 detects the objects in the image.

5) We will encode the output image using encoding function. 

6) The predicted image is displayed on the webpage.


Note: Encoding of the user uploaded image and prediction happens on the flask server.



## Deployment
#### Testing app via postman

Run
```bash
  python clientApp.py
```
1) click on Ip of your system.

2) Open postman application. By default request will be GET change it to POST. 

3) Add IP/name_of_route. 

4) Click on body for posting the request.select raw,json. write down the key(image). Using this key information is extracted from UI. Paste the encoded image string here. Click send. 

5) you get the decoded predicted image in base 64 format. Use base 64 guru site to check the decoded image. 

#### Debug your app
Run 
```bash
  python clientApp.py
```
1) upload image using the upload button on UI.

2) predict button is used to display the predicted output.