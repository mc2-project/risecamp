import xgboost as xgb
from numpy import genfromtxt
import logging
import pickle

class FederatedXGBoost:
    def __init__(self):
        xgb.rabit.init()
        self.dtrain = None
        self.dtest = None
        self.model = None

    def load_training_data(self, training_data_path):
        training_data_path = training_data_path[:-4] + "_" + str(xgb.rabit.get_rank() + 1) + ".csv"
        training_data = genfromtxt(training_data_path, delimiter=',')
        self.dtrain = xgb.DMatrix(training_data[:, 1:], label=training_data[:, 0])

    def load_test_data(self, test_data_path):
        test_data_path = test_data_path[:-4] + "_" + str(xgb.rabit.get_rank() + 1) + ".csv"
        test_data = genfromtxt(test_data_path, delimiter=',')
        self.dtest = xgb.DMatrix(test_data[:, 1:], label=test_data[:, 0])
    
    def train(self, params, num_rounds):
        if self.dtrain == None:
            print("Training data not yet loaded")
        self.model = xgb.train(params, self.dtrain, num_rounds)

    def predict(self):
        if self.dtest == None:
            print("Test data not yet loaded")
        return self.model.predict(self.dtest)

    def eval(self):
        if self.dtest == None:
            print("Test data not yet loaded")
        return self.model.eval(self.dtest)

    def get_num_parties(self):
        return xgb.rabit.get_world_size()

    def load_model(self, model_path):
        # self.model = xgb.Booster()
        # self.model.load_model(model_path)
        self.model = pickle.load(open(model_path, "rb"))

    def save_model(self, model_name):
        # self.model.save_model(model_name)
        pickle.dump(self.model, open(model_name, "wb"))
        print("Saved model to {}".format(model_name))

    def shutdown(self):
        print("Shutting down tracker")
        xgb.rabit.finalize()
