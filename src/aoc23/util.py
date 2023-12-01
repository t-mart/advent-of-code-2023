from aocd import get_data as aocd_get_data
from dotenv import load_dotenv

def get_data(day: int, year: int) -> str:
    load_dotenv()
    return aocd_get_data(day=day, year=year)
