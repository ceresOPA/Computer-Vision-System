from sqlalchemy import create_engine, Column, String, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR

DATABASE_URL = "mysql+pymysql://root:password@localhost/mask?charset=utf8"

# 开启预加载连接池
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
# 关闭自动提交与自动刷新并加载数据库，绑定数据库引擎
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 创建基类
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER(64), primary_key=True,
                autoincrement=True, comment='主键')
    username = Column(String(100), comment="用户名")
    password = Column(String(100), comment="密码")
    gender = Column(VARCHAR(10), server_default=text("''"), comment='性别')
    mark = Column(String(255), comment="个性签名")
    avatarUrl = Column(String(255), comment="头像地址")


Base.metadata.create_all(engine)  # 创建表结构
