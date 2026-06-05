# YA FILE QA.ENV FILE KO LOAD KARNY KALIYE HY

from dotenv import load_dotenv
import os

env_path=os.path.join(os.path.dirname(__file__),"../config/qa.env")

load_dotenv(env_path)

class ConfigReader:
    QA_URL=os.getenv("QA_URL")
    username=os.getenv("APP_USERNAME")
    PASSWORD = os.getenv("APP_PASSWORD")