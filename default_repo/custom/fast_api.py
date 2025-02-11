if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

@custom
def transform_custom(best_model,*args, **kwargs):
    # Load your pre-trained model
    with open('best_model.pkl', 'rb') as f:
        best_model = pickle.load(f)

    # Initialize FastAPI
    app = FastAPI()

    # Define the input data model
    class PredictionRequest(BaseModel):
        feature_1: float
        feature_2: float
        feature_3: float
        feature_4: float
        feature_5: float
        feature_6: float
        feature_7: float
        feature_8: float
        feature_9: float
        feature_10: float
        feature_11: float
        feature_12: float
        feature_13: float
        feature_14: float

    # Prediction endpoint
    @app.post("/predict/")
    async def predict(request: PredictionRequest):
        # Collect input data from the request
        input_data = [
            request.feature_1, request.feature_2, request.feature_3,
            request.feature_4, request.feature_5, request.feature_6,
            request.feature_7, request.feature_8, request.feature_9,
            request.feature_10, request.feature_11, request.feature_12,
            request.feature_13, request.feature_14
        ]
        
        # Reshape the input data for prediction
        single_observation = np.array(input_data).reshape(1, -1)
        
        # Make the prediction
        prediction_probabilities = best_model.predict_proba(single_observation)
        
        # Return the prediction (probability of class 1)
        prediction = prediction_probabilities[0][1]
        
        return {"prediction_probability": prediction}

    # Main function to start the FastAPI app (if required)
def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
