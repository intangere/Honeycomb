from _mysql import Mysql
import base64
import aes

class Hive():

	def __init__(self):
		self.mysql = Mysql()

	def checkAuth(self, username, pwd):
		aes_key = self.passToAesKey(pwd)
		sql = self.mysql.where('username', username).select('key').query()
		key = sql['key']
		try:
			pin = aes.decryptData(aes_key, base64.b64decode(key.strip()))
			if pin == '1337':
				return True
			else:
				return False
		except Exception as e:
			return False

	def addKey(self, username, pwd):
		pin = base64.b64encode(aes.encryptData(self.passToAesKey(pwd), '1337'))
		if not self.mysql.where('username', username).select('key').query():
			self.mysql.insert('username', username).query()
			self.mysql.where('username', username).update('key', pin).query()
			return True
		else:
			return False

	def passToAesKey(self, password):
		key = password
		i = 0
		temp_key = ""
		while len(temp_key) < 32:
			temp_key = "%s%s" % (temp_key, key[i])
			if i == len(key) - 1:
				i = 0
			else:
				i += 1
		return temp_key

h = Hive()
h.addKey('test', 'test1234')
assert h.checkAuth('test', 'test1234') == True


