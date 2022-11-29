import uvicorn
from fastapi import FastAPI

from app.common.config import conf

def create_app():
    
    #  c = cconf()
    app = FastAPI()

    # 데이터베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터정의

    return app

app = create_app()

if __name__ == "__main__":
    # 서버에 올리는 정보들
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)