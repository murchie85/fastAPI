from fastapi import FastAPI
from typing  import List
from models  import User,Gender,Role
from uuid    import uuid4,UUID

app = FastAPI()


db: List[User] = [
	User(
		id= UUID("4142061b-3062-4206-9de6-28f9f516db29"),
		first_name="Adam",
		last_name='mcminge',
		gender = Gender.male,
		roles = [Role.admin,Role.user]
		),
	User(
		id=UUID("c1c2299e-4ebd-42bb-bd8c-99da5e0d8a24"),
		first_name="Naomi",
		last_name='chun',
		gender = Gender.female,
		roles = [Role.student]
		)
]


# get main
@app.get("/")
async def root():
	return{"Hello ":"Adam!"}


# get users
@app.get("/api/v1/users")
async def fetch_users():
	return db

# post
@app.get("/api/v1/users")
async def fetch_users():
	return db