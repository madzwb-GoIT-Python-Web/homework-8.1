import os
# import configparser

from dotenv import load_dotenv
from mongoengine import connect


load_dotenv()
secret_file = os.environ.get("MONGODB_PASSWORD_FILE")
if secret_file and not os.path.exists(secret_file):
    secret_file = os.path.join(os.getcwd(), secret_file)
if secret_file:
    with open(secret_file, 'r') as fd:
        password = ''.join([line.strip() for line in fd.readlines()])
else:
    password  = os.environ.get("MONGODB_PASSWORD")

# config = configparser.ConfigParser()
# config.read('data/config.ini')

# mongo_user = config.get('DB', 'user')
# mongodb_pass = config.get('DB', 'pass')
# db_name = config.get('DB', 'db_name')
# domain = config.get('DB', 'domain')
user    = os.environ.get("MONGODB_USER")
name    = os.environ.get("MONGODB_NAME")
domain  = os.environ.get("MONGODB_DOMAIN")

connect(
    host=f"""mongodb+srv://{user}:{password}@{domain}/{name}?retryWrites=true&w=majority""",
    # alias="homework-8.1",
    ssl=True
)
