import cv2
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as f
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.c1 = nn.Conv2d(1, 8, 5, padding=1)
        self.mp1 = nn.MaxPool2d(2, 2)
        self.c2 = nn.Conv2d(8, 16, 5, padding=1)
        # self.mp2=nn.MaxPool2d(2,2)
        self.c3 = nn.Conv2d(16, 28, 3, padding=1)
        self.c4 = nn.Conv2d(28, 48, 3, padding=1)
        self.l1 = nn.Linear(48 * 5 * 5, 500)
        self.do = nn.Dropout(0.25)
        self.l2 = nn.Linear(500, 250)
        self.l3 = nn.Linear(250, 20)

    def forward(self, x):
        x = self.mp1(f.relu(self.c1(x)))
        x = self.mp1(f.relu(self.c2(x)))
        x = f.relu(self.c3(x))
        x = f.relu(self.c4(x))
        x = x.view(-1, 48 * 5 * 5)
        x = (f.relu(self.l1(x)))
        x = (f.relu(self.l2(x)))
        x = self.l3(x)
        return x

cl=["airplane","ant","banana","baseball","bird","bucket","butterfly","cat","coffee","dolplin","donut","duck","fish","leaf",'mountain','pecil','simely face','snake','umbrella','wine bottle']
Doodle=Net()
file="<.pth file path>" #paste your .pth file path here 
dev=torch.device('cpu')
Doodle.load_state_dict(torch.load(file,map_location=dev))# loading the .pth file in the Model

#drawing pad
drawing = False
ptx , pty = None , None

def line_drawing(event,x,y,flags,param):
    global ptx,pty,drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ptx,pty=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.line(img,(ptx,pty),(x,y),color=(255,255,255),thickness=5)
            ptx,pty=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.line(img,(ptx,pty),(x,y),color=(255,255,255),thickness=5)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('Doodle')
cv2.setMouseCallback('Doodle',line_drawing)
a=None
while True:
    cv2.imshow('Doodle',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    resize =cv2.resize(img, (28, 28), interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)
    inp = torch.tensor(gray.reshape(1, 1, 28, 28))
    out = Doodle(inp.float())
    n = torch.argmax(out)
    if n!=a:
        print("I think it's a ", cl[n])
        a=n

cv2.destroyAllWindows()




