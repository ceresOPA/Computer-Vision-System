import os
import shutil
import random
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

import cv2
from fastapi import APIRouter, Depends, File, UploadFile

from yolov3 import detect

file_router = APIRouter()


@file_router.post("/photo", summary="上传图片")
async def upload_image(
        file: UploadFile = File(...)
):
    print(f"上传文件:{file.filename}")

    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = "C:/Users/YL/Desktop/mask/mask/server/assets"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print("无文件夹")
    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return {"imageUrl": f"http://127.0.0.1:81/api/assets/{tmp_file_name}",
            "imageName": f"{tmp_file_name}",
            "appImgUrl":f"http://127.0.0.1:8080/assets/{tmp_file_name}"}

@file_router.post("/video", summary="上传视频")
async def upload_video(
        file: UploadFile = File(...)
):
    print(f"上传视频:{file.filename}")

    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = "C:/Users/YL/Desktop/mask/mask/server/assets"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print("无文件夹")
    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return {"videoUrl": f"http://127.0.0.1:81/api/assets/{tmp_file_name}",
            "videoName": f"{tmp_file_name}",
            "appvideoUrl": f"/assets/{tmp_file_name}"}


@file_router.get("/checkphoto")
def check_image(model: str,imageName: str):
    model_cfg = "/assets/"+model+".cfg"
    server_dir = 'C:/Users/YL/Desktop/mask/mask/server/'
    print("model",model)
    print("imageName",imageName)
    if model=='mask-yolov5s' or model == 'mask-yolov5m' or model == 'smoke-yolov5s':
        os.system(f"python {server_dir}/yolov5/detect.py --weights {server_dir}/yolov5/weights/{model}.pt  --source {server_dir}/assets/{imageName} --output {server_dir}/output")
    else:
        Data = detect.myDetect(inputSource=f"C:/Users/y2554/Desktop/mask/server/assets/{imageName}",outputPath="C:/Users/y2554/Desktop/mask/server//output",opt_cfg=f"C:/Users/y2554/Desktop/mask/server/yolov3/cfg/{model}.cfg",currentWeights=f"C:/Users/y2554/Desktop/mask/server/yolov3/models/{model}.pt",opt_names="C:/Users/y2554/Desktop/mask/server/yolov3/mask.names")
        print(Data)
    return {"masg":"ok",
            "imageUrl":f"http://127.0.0.1:81/api/output/{imageName}?random={random.randrange(1, 1000)}",
            "appImgUrl":f"/output/{imageName}?random={random.randrange(1, 1000)}"}


@file_router.get("/checkvideo")
def check_video(model: str,videoName: str):
    model_cfg = "/assets/"+model+".cfg"
    server_dir = 'C:/Users/YL/Desktop/mask/mask/server/'
    print("model",model)
    print("videoName",videoName)
    if model == 'mask-yolov5s' or model == 'mask-yolov5m' or model == 'smoke-yolov5s':
        os.system(f"python {server_dir}/yolov5/detect.py --weights {server_dir}/yolov5/weights/{model}.pt  --source {server_dir}/assets/{videoName} --output {server_dir}/output")
    else:
        Data = detect.myDetect(inputSource=f"C:/Users/y2554/Desktop/mask/server/assets/{videoName}",outputPath="C:/Users/y2554/Desktop/mask/server/output",opt_cfg=f"C:/Users/y2554/Desktop/mask/server/yolov3/cfg/{model}.cfg",currentWeights=f"C:/Users/y2554/Desktop/mask/server/yolov3/models/{model}.pt",opt_names="C:/Users/y2554/Desktop/mask/server/yolov3/mask.names")
        print(Data)
    # return {"masg":"ok",
    #         "videoUrl":f"http://127.0.0.1:81/api/output/{videoName}?random={random.randrange(1, 1000)}",
    #         "appVideoUrl":f"/output/{videoName}?random={random.randrange(1, 1000)}"}
    return {"masg": "ok",
            "videoUrl": f"http://127.0.0.1:81/api/output/{videoName}?random={random.randrange(1, 1000)}",
            "appVideoUrl": f"/output/{videoName}?random={random.randrange(1, 1000)}"}

@file_router.get("/checkvideoNo")
def check_video(model: str,videoName: str):

    return {"masg": "ok",
            "videoUrl": f"http://127.0.0.1:81/api/output/{videoName}?random={random.randrange(1, 1000)}",
            "appVideoUrl": "https://static-1259365379.cos.ap-chengdu.myqcloud.com/tmpcyvrw84b.mp4"}

@file_router.get("/camera")
def check_camera(model: str):
    server_dir = 'C:/Users/YL/Desktop/mask/mask/server/'
    if model == 'mask-yolov5s' or model == 'mask-yolov5m' or model == 'smoke-yolov5s':
        os.system(f"python {server_dir}/yolov5/detect.py --weights {server_dir}/yolov5/weights/{model}.pt  --source 0 ")
    else:
        detect.myDetect(inputSource="0", opt_cfg=f"C:/Users/y2554/Desktop/mask/server/yolov3/cfg/{model}.cfg",currentWeights=f"C:/Users/y2554/Desktop/mask/server/yolov3/models/{model}.pt",opt_names="C:/Users/y2554/Desktop/mask/server/yolov3/mask.names")
    return {"msg":"ok"}

@file_router.get("/offcamera")
def check_camera():
    sys.exit()
    print("111111111111111111111")
    return {"msg":"ok"}

@file_router.post("/avatar", summary="上传图片")
async def upload_image(
        file: UploadFile = File(...)
):
    print(f"上传文件:{file.filename}")

    # 本地存储临时方案，一般生产都是使用第三方云存储OSS(如七牛云, 阿里云)
    save_dir = "C:/Users/YL/Desktop/mask/mask/server/assets"
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print("无文件夹")
    try:
        suffix = Path(file.filename).suffix

        with NamedTemporaryFile(delete=False, suffix=suffix, dir=save_dir) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_file_name = Path(tmp.name).name
    finally:
        file.file.close()

    return {"imageUrl": f"http://127.0.0.1:81/api/assets/{tmp_file_name}",
            "imageName": f"{tmp_file_name}",
            "appImgUrl":f"/assets/{tmp_file_name}"}