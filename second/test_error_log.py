# -*-coding:utf8-*-
# from . import logger  # 这样import方法是失败的
import logger


try:
    a = 1 / 0
except:
    logger.error('something went wrong')





