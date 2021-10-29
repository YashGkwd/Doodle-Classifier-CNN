# Doodle-Classifier-CNN
The Doodle classifier is based on a Convolutional Neural Network which classifies the doodle input given by the user in 20 different classes.

![87329602-73404680-c54c-11ea-9e82-06057b6a873f](https://user-images.githubusercontent.com/73688295/137089923-7a92a14e-2d14-45e1-a495-05bc7bd72cc4.gif)
## Dataset
The Neural Network Model was trained on a dataset consisting of 2807037 images containing images of 20 differnt classes.Each image is of the size 28 x 28.

![data (1)](https://user-images.githubusercontent.com/73688295/137096046-372afdbc-a076-4c2f-ba7a-adc4fb8d9696.png)

## Libraries required
- Pytorch (For implementing Neural Network and its training)
- OpenCV (For creating drawing pad)
- Matplotlib (for plotting graphs and images)
- Numpy
- PySimpleGUI
## CNN Model
### Architecture 
Convolutional Layer
|Layer|Kernel size| Filters|Maxpool|Padding|
|---|--|--|--|--|
|Conv1| (5,5)|8|(2,2)|1|
|Conv2| (5,5)|16|(2,2)|1|
|Conv3|(3,3)|28|None|1|
|Conv4|(3,3)|48|None|1|


Fully Connected Layer
|Layer|Size|
|--|--|
|Fc layer1|(48 x 5 x 5,500)|
|Fc layer2|(500,250)|
|Fc layer3|(250,20)|

### Hyper parameters
|Parameters| Values|
|------|---|
| Learning rate|0.01|
|Epochs|100|
|Batch size|1200|
|Beta|0.9|
|Optimizer|SGD|
|Loss function|BCE Loss|

## Output of Model
The Loss Vs number of Epochs
![Screenshot (138)](https://user-images.githubusercontent.com/73688295/137258580-a812e140-cc36-4c8a-b44f-63c26c1a7600.png)


|Dataset|Accuracy | 
|----|----|
|Training dataset| 95.77 %|
| Testing dataset|  95.74 %|

## Final result

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/73688295/139380623-b9614ad1-14ed-44f1-aa3b-c47591bf37df.gif)


![ezgif com-gif-maker](https://user-images.githubusercontent.com/73688295/139380411-fe981d78-9a1d-481b-a26e-c0e9bb768ec3.gif)








