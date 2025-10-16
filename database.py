from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL= "mysql+mysqlconnector://bloguser:StrongPassword123!@localhost:3306/PERSON_DETAILS"
engine=create_engine(DATABASE_URL)
sessionlocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()
