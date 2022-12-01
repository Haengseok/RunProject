from dataclasses import dataclass, asdict
from os import path, environ
import json

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    # 기본 Configuration

    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True
   

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    # mysql+pymysql://[유저이름]:[비밀번호]@[호스트주소]:[포트번호]/[스키마이름]?charset=utf8
    DB_URL: str = "mysql+pymysql://root:root@localhost:3306/fastAPI?charset=utf8"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False



def conf():
    # 환경불러오기
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local")) #API_ENV가 없다면 local