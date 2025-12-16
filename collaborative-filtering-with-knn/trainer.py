import mlflow
from mlflow import sklearn
def train(model, train_set):
    model.fit(train_set)
    sklearn.log_model(model,'model')
    return model