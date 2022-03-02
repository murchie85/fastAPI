# Fast API Basics 

![](resources/image2.png)

- install fastapi [Fastapi Website](https://fastapi.tiangolo.com/)
- install uvicorn [uvicorn Website](https://www.uvicorn.org/)
- Pydantic for Model (datatype) validation [pydantic](https://pydantic-docs.helpmanual.io/)

## Install 

```
pip install fastapi "uvicorn[standard"
pip install uvicorn
```


## Notes


Fast API is production ready. 

**FAST API IS JUST A FRAMEWORK**  

you also need a Uvicorn server which is a `ASGI` server (asynchronous service gateway)  

Uvicorn is similar to `express js`


## Build and run.

- Make a main.py
- create a root
- run below:
  
```shell
uvicorn main:app --reload
```
  
- main is module name
- app is the instance of our application





## HTTP Methods   
  
**Head** Request Resource representation  

**Head** Same as Get but does not return body
  
**Post** Submits an entity to a specified resource , often changing state in server

**Put** Put replaces all representations of target resource with current payload.  

**Delete** Delete a specified resource  
  
**Connect** Establishes a connection or tunnel to server.  



## Using Async

use async lets us use `await` 

```python
@app.get('/')
async def read_results():
    results = await some_library()
    return results
```


## Pydantic and Models 

- Use typing, pydantic (basemodel) and others in the models.py

## Flow 

![](resources/flow.png)
