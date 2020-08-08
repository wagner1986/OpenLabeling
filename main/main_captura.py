import os
from datetime import datetime
from os.path import dirname

import cv2
import numpy as np

import config as cfg

class CameraCV:
    min_frame_std = 0

    def __init__(self):
        pass

    def rescale_frame(self, frame, percent=75):
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


    def grava_video(self, file_name=0,filename_out="output.avi"):
        if os.path.isfile(file_name) or file_name in (0, 1):
            cap = cv2.VideoCapture(file_name)

            for config in cfg.input['camera_box_config']:
                cap.set(config['id'], config['value'])

            ret, last_frame = cap.read()
            print('print 1 ', ret, last_frame.shape)
            if last_frame is None:
                print('last_frame ', last_frame)
                exit()

            filename_out='..{}{}'.format(os.sep,filename_out)

            frame_height = last_frame.shape[0]
            frame_width = last_frame.shape[1]
            out = cv2.VideoWriter(filename_out, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                                  (frame_width,frame_height))

            while cap.isOpened():
                ret, frame = cap.read()
                if frame is None:
                    break

                out.write(frame)

                fps = cap.get(cv2.CAP_PROP_FPS)
                cv2.putText(frame,
                            "Video: {} fps: {} H:{} X W:{}".format(filename_out, fps,frame_height,frame_width),
                            (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                cv2.imshow('original', frame)



                if cv2.waitKey(33) == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()
        else:
            print("video não existe")
        return 0


if __name__ == '__main__':

    util = CameraCV()
    # Nome do video de saida
    dateTimeObj = datetime.now()
    timeStr = dateTimeObj.strftime("%H%M%S")+".avi"

    util.grava_video(file_name=cfg.input['file_name'],filename_out=timeStr)
