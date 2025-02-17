import mlflow

def register_model():
    client = mlflow.tracking.MlflowClient()
    model_uri = "runs:/your_run_id/model"
    client.create_registered_model("RetailModel")
    client.create_model_version(name="RetailModel", source=model_uri, run_id="your_run_id")
    print("Model registered successfully.")

if __name__ == "__main__":
    register_model()
