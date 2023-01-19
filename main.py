import tls_client,random


class breakflare():
  def __init__(self,session = tls_client.Session(client_identifier="chrome_108")):
    self.session = session
  def Session(self):
    self.session = tls_client.Session(client_identifier="chrome_108")
    return self.session
  
  def options(self,url,**kwargs):
    return self.session.options(url,**kwargs)
    
  def get(self,url,**kwargs):
    return self.session.get(url,**kwargs)
  
  def post(self,url,data=None,json=None,**kwargs):
    return self.session.post(url,json=json,data=data,**kwargs)

  def patch(self,url,data=None, json=None, **kwargs):
    return self.session.patch(url,json=json,data=data,**kwargs)
  
  def put(self,url,data=None,json=None,**kwargs):
    return self.session.put(url,json=json,data=data,**kwargs)
  
  def delete(self,url,**kwargs):
    return self.session.delete(url,**kwargs)

def randstr(x):
  randoms = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
  return "".join(random.choice(randoms) for i in range(x))

headers = {}
session = breakflare()
setupcontent = session.get("https://m.kuku.lu/index.php")
headers["cookie"] = setupcontent.headers["Set-Cookie"]
print(breakflare().get(f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t=1674135384&csrf_token_check={str(str(headers['cookie']).split('cookie_csrf_token=')[1]).split(';')[0]}&newdomain=sika3.com&newuser=alpha{randstr(6)}",headers=headers).text.replace("OK:",""))
