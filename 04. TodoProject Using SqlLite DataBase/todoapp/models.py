from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from todoapp.database import Base


# * **`index=True`** → search/query fast hoti hai us column pe.
# * **`unique=True`** → us column ki value har row mein alag honi chahiye (duplicate allowed nahi).



class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    complete = Column(Boolean, default=False)
    priority = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)