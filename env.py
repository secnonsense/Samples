import os
from dotenv import load_dotenv

home=os.path.expanduser('~')
mypath=home+'/.myfile.env'

print(mypath)

load_dotenv(mypath)

access=os.environ.get("ACCESS_KEY")
secret=os.environ.get("SECRET_KEY")

print(f"My Access Key is {access} and my secret key is {secret}")
