# Text-extraction-using-Opencv
In this project i took a screenshot from random program which i have done and by using this opencv. 
i extract text from the screenshot and those text is saved in the format of txt file.
and the below steps must be followed while doing this project
and also you need to install "pytesseract"
for linux users you can follow this commands for install the requirements of this project:
1)sudo apt-get update
2)sudo apt-get install tesseract-ocr
3)sudo apt-get install tesseract-ocr-eng
4)sudo apt-get install libicu-dev
5)tesseract --version

After installing,you can follow these steps:
Step 1:- Pre-processing the image
         Before passing the image into OCR engine you need to preprocess the image like 
         converting image to grayscale,applying thresholding or morpological operations to remove noise.
Step 2:- Adjusting the OCR engine parameters
         1.Threshold value,which you need to ooptimise that for better results.
Step 3:- Resize the image
         Screenshots are actually bigger in resolution resizing the image will give us
         the better results
Step 4:- Output in txt file
