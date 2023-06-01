import cv2
import face_recognition
import pickle
import os
import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-e5a0f-default-rtdb.firebaseio.com/",
    'storageBucket':"faceattendancerealtime-e5a0f.appspot.com"

})




#importing student images
folderModePath = 'D:\Face Recognition System\Student-Image'
imgList= []
studentIds=[]
pathList= os.listdir(folderModePath)
print(pathList)
for path in pathList:
    imgList.append(cv2.imread(f'{folderModePath}/{path}'))
    studentIds.append(os.path.splitext(path)[0])

    
    fileName=f'{folderModePath}/{path}'
    bucket=storage.bucket()
    blob=bucket.blob(fileName)
    blob.upload_from_filename(fileName)




    
print(studentIds)


def findEncodings(imagList):
    encodeList=[]
    for img in imgList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Started...")
encodeListKnown=findEncodings(imgList)
encodeListKnownwithIds=[encodeListKnown,studentIds]
print(len(encodeListKnown))
print("Encoding completed")


# imgBackground = cv2.imread('Background-image\ground.png')

# #importing the mode images into a list
# folderModePath = 'D:\Face Recognition System\Background-image'
# modePathList= os.listdir(folderModePath)
# imgModeList= []
# for path in modePathList:
#     imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
# #print(len(imgModeList))

# cap=cv2.VideoCapture(0)

# while True:
#     success,img=cap.read()
    
#     imgS=cv2.resize(img,(0,0),None,0.25,0.25)
#     imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)


#     faceCurFrame=face_recognition.face_locations(imgS)
#     encodeCurframe=face_recognition.face_encodings(imgS,faceCurFrame)
    

#     modeType=0
    


#     imgBackground[162:162+480,55:55+640]=img
#     imgBackground[44:44+633,808:808+414]=imgModeList[modeType]

#     # if faceCurFrame:
#     for encodeFace,faceLoc in zip(encodeCurframe,faceCurFrame):
#             matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
#             faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
#             #print("matches",matches)
#             print(faceDis)


#             matchIndex=np.argmin(faceDis)
            
                 
     


file=open('EncodeFile.p','wb')
pickle.dump(encodeListKnownwithIds,file)
file.close()

print("File Saved")

