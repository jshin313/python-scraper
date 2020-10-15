#!/usr/bin/env python3
import requests

r = requests.get("https://temple-covid.herokuapp.com/")
print(r.text)
