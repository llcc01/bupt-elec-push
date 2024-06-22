# 北邮宿舍用电推送脚本

本项目使用 [electricity-monitor (buptelecmon)](https://github.com/jerrymakesjelly/electricity-monitor) 项目查询宿舍剩余电量，当小于设定阈值时，使用 [Server 酱](https://sct.ftqq.com/) 推送提醒并附带电费充值链接。

## 依赖

`buptelecmon` `python-dotenv`

`pypi` 中 `buptelecmon` 的版本较老，若您无法登录北邮身份认证系统，请到源仓库中下载源码安装。

## 配置说明

通过环境变量读取配置，支持 `.env` 配置。

| 环境变量名        | 备注                           |
| ----------------- | ------------------------------ |
| BUPT_USERNAME     | 用户名                         |
| BUPT_PASSWORD     | 密码                           |
| BUPT_DORMITORY    | 宿舍号，如 0-000               |
| SERVER_SENDKEY    | Server 酱 SendKey              |
| SURPLUS_THRESHOLD | 剩余电费阈值，小于该值触发推送 |

## 定时执行

脚本未提供定时任务功能，每次执行将会立即查询电费。Linux 用户可以使用 `crontab` 定时执行脚本。
