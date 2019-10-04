from FederatedXGBoost import FederatedXGBoost

# Instantiate a FederatedXGBoost instance
fxgb = FederatedXGBoost()

# Get number of federating parties
print("Number of parties in federation: ", fxgb.get_num_parties())

# Load model
fxgb.load_model("tutorial_model.model")

# Load the test data
fxgb.load_test_data('/data/msd_test_data_split.csv')

# Evaluate the model
print(fxgb.eval())

# Get predictions
ypred = fxgb.predict()

# Shutdown
fxgb.shutdown()
