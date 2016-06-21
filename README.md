# Honeycomb
--
Python Library which allows developers to avoid storing passwords in their database<br>
Users must memorize their password.<br>
Usage
```
h = Hive()
h.addKey('username', 'password')
assert h.checkAuth('username', 'password') == True
```
How does it work?<br>
--
When the user chooses a password of max length 32 characters<br>
it is converted into a AES key using passToAesKey(password).<br>
A pin is then encrypted, in this case '1337'. This CAN be changed.<br>
This encrypted pin is stored in the database instead of the password.<br>
When a user logs in you call checkAuth(username, password).<br>
This shifts the password into the corresponding AES key.<br>
This key is then used to decrypt the 'key' field in the database<br>
which stores the encrypted pin. If the decrypted pin matches '1337'<br>
the user has entered the correct username/password combination.<br>
