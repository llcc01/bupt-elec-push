from buptelecmon import electricitymonitor
import dotenv
import os
import requests

dotenv.load_dotenv()

username = os.getenv("BUPT_USERNAME")
password = os.getenv("BUPT_PASSWORD")
dormitory = os.getenv("BUPT_DORMITORY")
sendkey = os.getenv("SERVER_SENDKEY")
surplus_threshold = int(os.getenv("SURPLUS_THRESHOLD", 0))

em = electricitymonitor.ElectricityMonitor()
em.login(username, password)
res = em.query([dormitory])
info = res[dormitory]
info_time = info["time"]
surplus = info["surplus"]

print(info_time, "电量剩余：", surplus)

if surplus < surplus_threshold:
    requests.get(
        "https://sctapi.ftqq.com/" + sendkey + ".send",
        params={
            "title": dormitory + "电量剩余" + str(surplus),
            "desp": "充值链接：\n" + em.get_recharge_link(dormitory),
        },
    )
