from FederatedXGBoost import FederatedXGBoost

# Instantiate a FederatedXGBoost instance
fxgb = FederatedXGBoost()

# Get number of federating parties
print(fxgb.get_num_parties())

# Load training data
fxgb.load_training_data('/data/msd_test_data_split.csv')

# Train a model
params = {'max_depth': 3, 'min_child_weight': 1.0, 'lambda': 1.0}
num_rounds = 50
fxgb.train(params, num_rounds)

# Save the model
fxgb.save_model("tutorial_model.txt")

# Shutdown
fxgb.shutdown()
