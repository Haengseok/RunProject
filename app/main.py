from dataclasses import asdict

import uvicorn
from fastapi import FastAPI
from app.database.conn import db
from app.common.config import conf
from app.routes import index

from app.common.config import conf

def create_app():
    
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 데이터베이스 이니셜라이즈

    # 레디스 이니셜라이즈

    # 미들웨어 정의

    # 라우터정의

    app.include_router(index.router)
    return app

app = create_app()

if __name__ == "__main__":
    # 서버에 올리는 정보들
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)