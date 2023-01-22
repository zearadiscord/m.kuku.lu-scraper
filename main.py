import tls_client,random
print("Domainnameはipの国ごとに違う場合があります\n日本ではeripo.comやna-cat.comが使えます")

def randstr(x):
  randoms = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
  return "".join(random.choice(randoms) for i in range(x))

domainname = input("Domainname > ")
session = tls_client.Session(client_identifier="chrome_108")
headers = {}
setupcontent = session.get("https://m.kuku.lu/index.php")
headers["cookie"] = setupcontent.headers["Set-Cookie"]
print(session.get(f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&csrf_token_check={str(str(headers['cookie']).split('cookie_csrf_token=')[1]).split(';')[0]}&newdomain={domainname}&newuser=alpha{randstr(6)}",headers=headers).text.replace("OK:",""))
