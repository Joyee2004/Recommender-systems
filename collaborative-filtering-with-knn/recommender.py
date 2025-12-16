# contains 2 methods - knn and svd
import mlflow
from surprise import KNNWithMeans, SVD
from config import KNN_K, KNN_SIMILARITY,SVD_EPOCHS,SVD_FACTORS

def build_knn(user_based = True,k = 40):
    mlflow.log_param("k",KNN_K)
    mlflow.log_param("user_based",user_based)
    mlflow.log_param("similarity",KNN_SIMILARITY)


    sim = {
        "name" : KNN_SIMILARITY,
        "user_based" :user_based

    }
    return KNNWithMeans(k=KNN_K, sim_options = sim)

def build_svd(n_factors=SVD_FACTORS, n_epochs = SVD_FACTORS):
    mlflow.log_param("n_factors",SVD_FACTORS)
    mlflow.log_param("n_epochs", SVD_EPOCHS)
    return SVD(n_factors=SVD_FACTORS, n_epochs= SVD_EPOCHS)