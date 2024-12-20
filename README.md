# 🛠️ Project Name: Employee Satisfaction score prediction

## 📖 Overview
Welcome to **Employee Satisfaction score predictor**, where we take on the exciting challenge of solving **This dataset contains **100,000 rows of data** capturing key aspects of employee performance, productivity, and demographics in a corporate environment.**. This repository is your one-stop guide to everything from data preparation to deploying a fully functional service.


### **Potential Use Cases**  

1. **Churn Prediction**: Identifying patterns that lead to employee resignation.  
2. **Productivity Analysis**: Understanding the factors that drive productivity, such as remote work frequency, overtime, or training hours.  
3. **Performance Evaluation**: Analyzing how performance scores correlate with factors such as salary, team size, or education level.  
4. **HR Analytics**: Providing insights into workforce demographics and behavior for strategic decision-making.  

### Here in our project we will be predicting the employee satisfaction score which ranges from 1 to 5 indicating whether the employee is happy with his job or not and this might help the HR team to focus on employees who might be unhappy and help them by taking actions which might reduce attrition thereby reducing company costs if in case they need to hire from scratch.

---

## 📂 Repository Structure  
Here's what you'll find inside:  

```
.
├── README.md           # You're reading it now!
├── Data/               # Dataset or instructions to obtain it  
├── Notebooks/          # Comprehensive notebooks  with EDA, model selection, etc.  
├── train.py            # Script to train and save the model  
├── app.py              # Script to load and serve the model  
├── requirements.txt    # Dependencies for the project  
├── Dockerfile          # For containerizing the service  
└── artifacts/          # Deployment artifacts or media
```

---

## 🧩 Components

### 1. **README.md**  
A fully documented guide (yep, this file!) that details the problem, how to run the project, and what you can achieve with it.  

### 2. **Data**  
- **Option 1:** The dataset is included in the `Data/` folder.  
- **Option 2:** Instructions for downloading the dataset are provided in `Data/README.md`.  

### 3. **Notebpooks**  
An Jupyter Notebooks that showcases:  
- 🧹 Data cleaning and preparation  
- 📊 Exploratory Data Analysis (EDA)  
- 🌟 Feature importance insights  
- 🤖 Model selection and hyperparameter tuning  

### 4. **train.py**  
Automates the process of:  
- Training the final model  
- Saving it to a file for future use  

### 5. **app.py**  
Seamlessly integrates:  
- Loading the trained model  
- Serving predictions via a web service using **Flask**  

### 6. **Dependencies**  
Included files to set up the environment:  
- `Pipfile` and `Pipfile.lock` for pipenv or  `requirements.txt` for pip-based setups   
- Alternatively: `conda.yml` or `pyproject.toml`  

### 7. **Dockerfile**  
A ready-to-use Dockerfile to containerize the project for deployment.

### 8. **Deployment**  
- **URL:** [Deployed here](https://pd-shiva-employeesa-e052ac49d33647c988966e33c4fbe596.community.saturnenterprise.io) 
- **Media:** Screenshots or video demo of the deployed service interaction.  

---

## 🚀 Quick Start  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/sg-56/EmployeeSatisfactionScore.git
   cd EmployeeSatisfactionScore
   ```  

2. **Set up the environment**:  
   ```bash
   pip install -r requirements.txt
   ```  
   or 

    ```bash
   pipenv install
   ```  

3. **Run the training script**:  
   ```bash
   python train.py
   ```  

4. **Serve predictions**:  
   ```bash
   python predict.py
   ```  

5. **Optional: Run in Docker**:  
   ```bash
   docker build -t employeesatisfaction .
   docker run -p 5000:5000 employeesatisfaction
   ```  

---

🎉 **Happy coding!** Make sure to star ⭐ this repo if you find it useful. Let’s build something amazing together! 


**Please feel free to cotaact me**

---

- If the deployment is not working it might be taken down due to limited alloted running time,
    I will be pausing it and would be happy to enable if you let me know.


