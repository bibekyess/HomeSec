# HomeSec
Team Members: Manoj Pandey, Bibek KC, Timothy Manoj Methews, Breket Assefa

Work: This repository is our Service Computing(CS459) Final project called HomeSec(Home Security). We utilized Service computing methodolies like SOA, Goals Design, Workflow design and Service mashups. 
Work are divided into two parts:
1. Make Face-Recognition model
2. Integrate Face-Regonition with Node-red Workflow and other services mashups

1. For the Face-Recognition, We used OpenCv's Haar-Cascade Classifier. AS code workflow, We use github opensource code[Ref] as per our requirement. Code details can be found in
/HomeSec/Face-Recognition/ folder. There are there main python files: one for  Face-imges capturing called 01_face_dataset.py, two for training those captured images to our face-recognition Haar-Cascasde classifier called 
02_face_training.py and three for using those trained weight on our custom faces and for Face-Recognition called HomeSec_Algo.py. trainer.yml is the trained weight for our Face_Recognition model. haarcascade_frontalface_deafult.xml is
the classifier provided by the OpenCV. 

2. Node-Red Workflow: We use node-red for our main engine of the project Home_Sec. We used exec node in node-red to integrate our face-recognition code that is located in raspberrypi,
with the help of bash script called initiate_venv.sh . This bash script is called using exec node and the output will be whether the face-detected by Raspberrypi camera and analyzed by our Face-recognition AI model to 
be family members or not. If our AI model doesn't recognize the person detected, It will notify the homeowner through Telegram bot with the help of node-red telegram node. HomeOwner than have option to choose if she/he 
recognition that unregistered face. If the face is not recognized, Homeowner can notify the police through telegram, also send text and voice notification to the registered neighbors for immediate help. 
We used node-red mobile dashboard to make app for neighbors phone. As per the request of homeowner, Node-red on raspberry pi will notify neighbors through CloudMQTT broker. Homeowner can send both text and audio notificaiton to 
the neighbors. It is upto neighbors on how to react to that information.

Demo Video of our Project:  
https://youtu.be/YhccA0mm2YA 

Reference: 
1. https://github.com/kunalyelne/Face-Recognition-using-Raspberry-Pi 

