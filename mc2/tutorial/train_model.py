from Utils import FederatedXGBoost

# Instantiate a FederatedXGBoost instance
fxgb = FederatedXGBoost()

# Get number of federating parties
print("Number of parties in federation: ", fxgb.get_num_parties())

# Load training data
# TODO: modify training data path
# For this part, you only need to add the path to the data without the party_id,
# e.g. /data/hospital/hospital_training.csv
training_data_path = "path/to/data"
fxgb.load_training_data(training_data_path)

# Train a model
# TODO: modify the `objective` parameter depending on which dataset you're using
# We recommend setting objective to binary:logistic for the insurance dataset
# and objective to multi:softmax for the hospital dataset
# If using the hospital dataset, you also need to set `num_classes` to 5 
params = {'max_depth': 3, 'min_child_weight': 1.0, 'lambda': 1.0}
num_rounds = 50
fxgb.train(params, num_rounds)

# Save the model
fxgb.save_model("ex3_model.model")

# Shutdown
fxgb.shutdown()
