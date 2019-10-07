from FederatedXGBoost import FederatedXGBoost

# Instantiate a FederatedXGBoost instance
fxgb = FederatedXGBoost()

# Get number of federating parties
print("Number of parties in federation: ", fxgb.get_num_parties())

# Load training data
fxgb.load_training_data('/data/hospital/hospital_training.csv')

# Train a model
params = {'max_depth': 3, 'min_child_weight': 1.0, 'lambda': 1.0}
num_rounds = 50
fxgb.train(params, num_rounds)

# Save the model
fxgb.save_model("ex3_model.model")

# Shutdown
fxgb.shutdown()
