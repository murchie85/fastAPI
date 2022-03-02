from typing  import List
from uuid    import UUID
from models  import User,Gender,Role,userUpdateRequest
from fastapi import FastAPI, HTTPException

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


# GET USER
@app.get("/api/v1/users")
async def fetch_users():
	return db

# POST
"""
takes user from request body
appends to db
returns it back to client

Has to have the same shape as User data object
"""
@app.post("/api/v1/users")
async def register_user(user: User):
	db.append(user)
	return {'id': user.id}


# PUT 
# {user_id} is path variale 
# userUpdateRequest is a class from model
@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: userUpdateRequest, user_id: UUID):
	
	for user in db:

		if(user.id==user_id):

			if(user_update.first_name is not None):
				user.first_name = user_update.first_name

			if(user_update.last_name is not None):
				user.last_name = user_update.last_name

			if(user_update.middle_name is not None):
				user.middle_name = user_update.middle_name

			if(user_update.roles is not None):
				user.roles = user_update.roles

			return
	raise HTTPException(
		status_code=404,
		detail = f"user with id: {user_id} does not exist"
	)


# DELETE 
# {user_id} is path variale 
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
	for user in db:
		if(user.id==user_id):
			db.remove(user)
			return
	raise HTTPException(
		status_code=404,
		detail = f"user with id: {user_id} does not exist"
	)
