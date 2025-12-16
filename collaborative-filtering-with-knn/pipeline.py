import mlflow
from config import MLFLOW_EXPERIMENT
from loadData import load_data
from preprocess import split_data
from recommender import build_knn, build_svd
from trainer import train
from evaluator import eval

def run_pipe(model_type):
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    
    with mlflow.start_run(run_name = model_type):
        dataset = load_data()
        trainset, testset = split_data(dataset)


        if model_type == "user_knn":
            user_based = True
            model = build_knn(user_based=user_based)
        elif model_type == "item_knn":
            user_based = False
            model= build_knn(user_based=user_based)
        elif model_type == "svd":
            model = build_svd()
        else :
            raise ValueError("Invalid model type")
        
        model = train(model, trainset)
        metrics = eval(model, testset)
        return model, trainset, metrics
