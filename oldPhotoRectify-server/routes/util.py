import pymysql
from fastapi import Depends, APIRouter
import psutil

util_router = APIRouter()

before = psutil.net_io_counters().bytes_recv




@util_router.get("/getComInfo")
def computer_info():
    now = psutil.net_io_counters().bytes_recv
    return {
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }


@util_router.get("/getMaskData")
def mask_data():
    db = pymysql.connect("localhost", "root", "password", "mask")
    cursor = db.cursor()
    cursor.execute(
        "SELECT SUM(mask), SUM(nomask), DATE_FORMAT(date,'%H') as time FROM `maskdata` WHERE DATE_FORMAT(date,'%Y-%m-%d') >= DATE_FORMAT(now(),'%Y-%m-%d') GROUP BY time ORDER BY time ")
    cursor.close()
    db.close()
    return {
        "mask_data": cursor.fetchall()
    }
