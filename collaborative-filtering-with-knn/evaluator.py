import mlflow
from surprise import accuracy
def eval(model, test_set):
    predictions = model.test(test_set)
    rmse = accuracy.rmse(predictions,verbose = False)
    mae = accuracy.mae(predictions, verbose = False)
    mlflow.log_metric("RMSE",rmse)
    mlflow.log_metric("MAE",mae)
    return {
        "RMSE": rmse,
        "MAE": mae
    }