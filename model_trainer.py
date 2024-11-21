import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from sklearn.feature_extraction import DictVectorizer


def save_artifacts(model_object,filename):
    model_path = f"./artifacts/{filename}.bin"
    with open(model_path,'wb') as file:
        pickle.dump(model,file)



def train_and_select_best_model(X, y, test_size=0.2, random_state=42):
    """
    Train multiple regression models, evaluate them, and select the best one.
    Finetune the selected model using GridSearchCV.

    Parameters:
    - X: Features (numpy array or pandas DataFrame)
    - y: Target (numpy array or pandas Series)
    - test_size: Proportion of the dataset for testing
    - random_state: Random state for reproducibility

    Returns:
    - best_model: The fine-tuned best model
    - best_params: Parameters of the fine-tuned model
    - best_score: Evaluation score of the fine-tuned model
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    vectorizer = DictVectorizer(sparse=True)
    vectorizer.fit(X_train.to_dict(orient='records'))
    X_train_tr = vectorizer.transform(X_train.to_dict(orient='records'))
    X_test_tr = vectorizer.transform(X_test.to_dict(orient='records'))

    # Define regression models
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(random_state=random_state),
        "XGBoost": XGBRegressor(random_state=random_state, use_label_encoder=False, eval_metric='rmsle',n_jobs=-1),
        "SVR": SVR()
    }

    # Hyperparameter grids for fine-tuning
    param_grids = {
        "LinearRegression": {},  # No hyperparameters to tune for LinearRegression
        "RandomForest": {
            "n_estimators": [50, 100, 200],
            "max_depth": [None, 10, 20]
        },
        "XGBoost": {
            "n_estimators": [50, 100, 200],
            "learning_rate": [0.01, 0.1, 0.2],
            "max_depth": [3, 5, 10]
        },
        "SVR": {
            "C": [0.1, 1, 10],
            "kernel": ["linear", "rbf"]
        }
    }

    # Evaluate models
    scores = {}
    for name, model in models.items():
        print(f"Training model : {name}")
        model.fit(X_train_tr, y_train)
        predictions = model.predict(X_test_tr)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        scores[name] = {"model": model, "mse": mse, "r2": r2}

    # Select the best model based on R^2 score
    best_model_name = max(scores, key=lambda x: scores[x]["r2"])
    best_model = models[best_model_name]

    print(f"Best Model: {best_model_name}")

    # Fine-tune the best model
    if param_grids[best_model_name]:  # Skip if no parameters to tune
        grid_search = GridSearchCV(best_model, param_grids[best_model_name], cv=5, scoring='r2',n_jobs=-1)
        grid_search.fit(X_train_tr, y_train)
        best_model = grid_search.best_estimator_
        best_params = grid_search.best_params_
    else:
        best_params = "No parameters to tune"

    # Evaluate the fine-tuned model
    final_predictions = best_model.predict(X_test)
    final_score = r2_score(y_test, final_predictions)

    return vectorizer,best_model, best_params, final_score




FILE_PATH = './Data/Employee_data.csv'

df = pd.read_csv(FILE_PATH)
features_not_required = [
    'Employee_ID',
    'Hire_Date',
    'Resigned'
]


df.drop(columns=features_not_required,inplace=True)

TARGET_COLUMN = 'Employee_Satisfaction_Score'


X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]

vectrizer,model,best_params,score = train_and_select_best_model(X,y,0.2)

save_artifacts(model,'model')
save_artifacts(vectrizer,'vectorizer')






