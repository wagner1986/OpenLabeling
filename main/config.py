#opencv flags https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html

input = {
    'file_name': 0,
    'camera_box_config': [
        {'id': 5, 'value': 15}, #cv2.CAP_PROP_FPS
        {'id': 28, 'value': 20}, #cv2.CAP_PROP_FOCUS campo altere em multiplos de 5
        {'id': 3, 'value': 1920},  #CV_CAP_PROP_FRAME_WIDTH width resolution
        {'id': 4, 'value': 1080},  #CV_CAP_PROP_FRAME_HEIGHT height resolution
    ],
    'resolution':[
        {'id': 3, 'value': 1920},#width
        {'id': 4, 'value': 1080},#height
    ],
    'camera_pistol_config':{
    }
}
