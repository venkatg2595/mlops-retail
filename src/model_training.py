import mlflow
import xgboost as xgb

def train_model():
    mlflow.set_tracking_uri("http://your_mlflow_server")
    mlflow.xgboost.autolog()
    dtrain = xgb.DMatrix("gs://retail-mlops-bucket/processed_data.csv")
    model = xgb.train({}, dtrain, num_boost_round=10)
    mlflow.xgboost.log_model(model, "model")
    print("Model training completed.")

if __name__ == "__main__":
    train_model()
