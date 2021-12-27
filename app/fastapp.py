# import modules
from fastapi import FastAPI, Request
from app.BMI import BodyMassIndex

# instantiate fastapi
app= FastAPI()

@app.get("/")
async def get_input(request:Request):
    """
        Get inputs from users and call the simple interest function to evaluate
        the parameters then return the output. 
    """
    getInput= await request.json()
    height = getInput['height']
    weight = getInput['weight']

    # evaluate interest
    BMI_Result = BodyMassIndex(height, weight)

    return {"Your height is:": height, "Your weight is:": weight, "Your BMI is:": BMI_Result}
