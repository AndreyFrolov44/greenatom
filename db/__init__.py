from .inbox import inbox
from .base import engine, metadata

metadata.create_all(bind=engine)
