This is a simple motion detector by checking differences between consecutive frames and getting contours that are big enough to be recognized as a human which is then given as a motion detected shown on top and a green coloured rectangle around their body(the contours we detected are the rectangles drawn )

Requirements:
<br/>
opencv
<br/>
numpy

How to Run:
To use it on your own pc pip install the requirements (with pip install requirements.txt) and run motion_detector.py .


Note: you can use any file by changing "v_test.avi" with the file you want in motion_detector.py


Below is a 60 fps version gif of my code running on v_test.avi


![Demo uses gif](demo/demo.gif)