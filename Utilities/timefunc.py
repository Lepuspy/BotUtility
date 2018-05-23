#-*-coding:utf-8-*-
import datetime
import time



def TimeCurrent():
	"""
	Retrun: datatime
		現在時刻のdatetimeオブジェクト
	"""
	now = datetime.datetime.now()
	return now

def DayCurrent():
	"""
	Retrun: str
		現在時刻の[年:月:日]を文字列
	"""
	now = datetime.datetime.now()
	day = now.strftime('%Y_%m_%d')
	return day

def HourCurrent():
	"""
	Retrun: str
		現在時刻の[時:分:秒]を文字列
	"""
	now = datetime.datetime.now()
	hour = now.strftime('%H:%M:%S')
	return hour

def UnixTimeCurrent():
	"""
	Retrun: float
		現在時刻のUnixTime
	"""
	unixime = time.time()
	return unixime