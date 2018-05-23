#-*-coding:utf-8-*-
# Python => 3.4
from pathlib import Path
import sys
from .timefunc import DayCurrent,HourCurrent
# pip install pandas
import pandas as pd

"""Logファイル作成モジュール"""


__author__ = "Lepus <Twitter @lepus_py>"
__version__ = "1.0"
__date__    = "2018/05/23"



# ユーザー定義
MainName = "logs"
InfoName = "Info"
ErrorName = "Error"



class Logs:
	def __init__(self):
		# ファイルパスを設定
		self.TopPath = Path(Path.cwd())
		self.MainPath = self.TopPath / MainName
		self.InfoPath = self.MainPath / InfoName
		self.ErrorPath = self.MainPath / ErrorName

	def Info(self, message, mode="a"):
		"""
		Action:
			稼働状況のログファイル日付毎に管理

		Parameter:
			message: str
				Logに書き込むメッセージ
			mode: "a" or "w"  default "a"
				書き込みモード 上書き "w" 追記 "a"
		"""
		try:

			# ファイルネーム
			file_name = self.InfoPath / (DayCurrent() + "{}.log")
			# メッセージの設定
			message = "{} >>> Info:{}\t\n".format(HourCurrent(), message)
			# 書き込み
			text(file_name, message, mode)

		except Exception as e:
			self.Error("OutPut.Info >>> " + str(e))
			
	def Error(self, message, mode="a"):
		"""
		Action:
			エラー発生時のログファイル日付毎に管理

		Parameter:
			message: str
				Logに書き込むメッセージ
			mode: "a" or "w"  default "a"
				書き込みモード 上書き "w" 追記 "a"

		Raise:
			SystemExit:
				なんらかの理由でErrorログが書き込めなかった場合
		"""
		try:

			# ファイルネーム
			file_name = self.ErrorPath / (DayCurrent() + "{}.log")
			# メッセージの設定
			message = "{} >>> Error:{}\t\n".format(HourCurrent(), message)
			# 書き込み
			text(file_name, message, mode)

		except Exception as e:
			sys.exit("Exception >>> OutPut " + str(e))

	

def csv(FullPath, data, mode, index=None, columns=None, dtype=None, copy=False):
	"""
	Aciton:
		.csv ファイル書き込み関数
	
	Parameters:
		FullPath: os.path or pathlib オブジェクト
			書き込み先ファイルパス
		data～copy:
			pandas DataFrame準拠
		mode: str
			書き込みモード 上書き "w" 追記 "a"
	
	Raises:
		AttributeError:
			指定拡張子以外のファイルを書き込む場合
	"""
	# pathlibオブジェクト変換
	FullPath = Path(FullPath)
	if FullPath.suffix == ".csv":
		if mode in ["w","a"]:
			heders = True if mode == "w" else False

			FullPath.mkdir(parents=True, exist_ok=True)

			df = pd.DataFrame(data, index, columns, dtype, copy)
			df.to_csv(FullPath, mode, index=False, encoding="utf-8", header=heders)
		else:
			raise ValueError("規定外のmode指定です >>> a or w : " + mode)
	else:
		raise AttributeError("指定ファイルは CSVファイルではない為 書き込めません : " + FullPath.name)




def text(FullPath,message,mode):
	"""
	Action:
		.txt .log ファイル書き込み関数
		
	Parameter:
		FullPath: os.path or pathlib オブジェクト
			書き込み先ファイルパス
		message: str
			Logに書き込むメッセージ
		mode: "a" or "w"
			書き込みモード 上書き "w" 追記 "a"
	
	Raises:
		AttributeError:
			指定拡張子以外のファイルを書き込む場合
	"""
	# pathlibオブジェクト変換
	FullPath = Path(FullPath)

	if FullPath.suffix in [".log",".txt"]:

		FullPath.mkdir(parents=True, exist_ok=True)

		with open(FullPath, mode, encoding="utf-8") as f:
			f.write(str(message))
	else:
		raise AttributeError("このファイルには書き込めません : {}".format(FullPath.name))
	


if __name__ == '__main__':
	Logs = Logs()
	Logs.Info("a")
	Logs.Error("a")
