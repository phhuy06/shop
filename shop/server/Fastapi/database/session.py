from sqlmodel import Session, select
from .engine import engine

def SQL(action: str, tables: list, condition : bool = True, data=None):
    with Session(engine) as session:
        if action == "create":
            session.add(data)
            session.commit()
            session.refresh(data)
            return data
        elif action == "delete":
            statement = select(*tables).where(condition)
            result = session.exec(statement).first()
            if result is None:
                return("Delete none")   
            session.delete(result)
            session.commit()
            return(f"{result} deleted")
        elif action == "read":
            statement = select(*tables).where(condition)
            result = session.exec(statement).all()
            return result
        elif action == "update":
            statement = select(*tables).where(condition)
            result = session.exec(statement).first()
            if result is None: 
                return("Update none")
            session.delete(result)
            session.add(data)
            session.commit()
            session.refresh(data)
            return data

