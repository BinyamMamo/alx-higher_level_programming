#!/usr/bin/env python3

if __name__ == "__main__":
  from urllib import request
  resp = request.urlopen("https://alx-intranet.hbtn.io/status")
  data = resp.read()
  print ("Body response:")
  print (f"\t - type: {type(data)}")
  print (f"\t - content: {data}")
  print (f"\t - utf8 content: {data.decode('UTF-8')}")
  