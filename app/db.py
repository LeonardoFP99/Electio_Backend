from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///electio.db', echo=True, connect_args={'check_same_thread': False})

connect_args={'check_same_thread':False}

Session = sessionmaker(bind=engine)