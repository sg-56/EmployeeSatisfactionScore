# 📂 Dataset Acquisition Guide  

This guide provides step-by-step instructions to download and prepare the dataset from Kaggle for use in your project.  

---

## 🗂 Dataset Information  

- **Name**:  Employee Performance and Productivity Data 
- **Description**: This dataset contains **100,000 rows of data** capturing key aspects of employee performance, productivity, and demographics in a corporate environment.  

### **Features**  

- **Employee_ID**: Unique identifier for each employee.  
- **Department**: The department in which the employee works (e.g., Sales, HR, IT).  
- **Gender**: Gender of the employee (Male, Female, Other).  
- **Age**: Employee's age (between 22 and 60).  
- **Job_Title**: The role held by the employee (e.g., Manager, Analyst, Developer).  
- **Hire_Date**: The date the employee was hired.  
- **Years_At_Company**: The number of years the employee has been working for the company.  
- **Education_Level**: Highest educational qualification (High School, Bachelor, Master, PhD).  
- **Performance_Score**: Employee's performance rating (1 to 5 scale).  
- **Monthly_Salary**: The employee's monthly salary in USD, correlated with job title and performance score.  
- **Work_Hours_Per_Week**: Number of hours worked per week.  
- **Projects_Handled**: Total number of projects handled by the employee.  
- **Overtime_Hours**: Total overtime hours worked in the last year.  
- **Sick_Days**: Number of sick days taken by the employee.  
- **Remote_Work_Frequency**: Percentage of time worked remotely (0%, 25%, 50%, 75%, 100%).  
- **Team_Size**: Number of people in the employee's team.  
- **Training_Hours**: Number of hours spent in training.  
- **Promotions**: Number of promotions received during their tenure.  
- **Employee_Satisfaction_Score**: Employee satisfaction rating (1.0 to 5.0 scale).  
- **Resigned**: Boolean value indicating if the employee has resigned.  

---

### **Potential Use Cases**  

1. **Churn Prediction**: Identifying patterns that lead to employee resignation.  
2. **Productivity Analysis**: Understanding the factors that drive productivity, such as remote work frequency, overtime, or training hours.  
3. **Performance Evaluation**: Analyzing how performance scores correlate with factors such as salary, team size, or education level.  
4. **HR Analytics**: Providing insights into workforce demographics and behavior for strategic decision-making.  

---

## 🔑 Prerequisites  

1. **Kaggle Account**  
   Ensure you have a registered account on [Kaggle](https://www.kaggle.com/).  

2. **Kaggle API Key**  
   - Log in to your Kaggle account.  
   - Navigate to your [Account Settings](https://www.kaggle.com/account).  
   - Scroll to the **API** section and click `Create New API Token`.  
   - A file named `kaggle.json` will be downloaded.  

---

## 📥 Steps to Download the Dataset  

### Step 1: Install Kaggle CLI  
Make sure you have Python installed. Then install the Kaggle Python package:  

```bash
pip install kaggle
```  

### Step 2: Configure the Kaggle API Key  
Move the downloaded `kaggle.json` file to the appropriate location:  

```bash
# On Linux/MacOS:
mkdir -p ~/.kaggle
mv kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

# On Windows:
mkdir %USERPROFILE%\.kaggle
move kaggle.json %USERPROFILE%\.kaggle\
```  

### Step 3: Download the Dataset  
Use the Kaggle CLI to download the dataset:  

```bash
kaggle datasets download -d [dataset-identifier]
```  
- Replace `[dataset-identifier]` with the dataset's unique identifier found in the URL (e.g., `username/dataset-name`).  

### Step 4: Unzip the Dataset  
Once downloaded, unzip the file:  

```bash
unzip dataset-name.zip -d data/
```  

---

## 🛠 Verifying the Dataset  

Check if the dataset has been downloaded and extracted correctly:  

```bash
ls data/
```  

Ensure all expected files (e.g., CSV, images, etc.) are present in the `data/` folder.  

---

## ⚠️ Troubleshooting  

- **Error: "403 - Forbidden"**  
   Ensure your `kaggle.json` is correctly configured and permissions are set properly.  

- **Command Not Found**  
   Verify that the `kaggle` package is installed and included in your system's PATH.  

---

🎉 **You’re all set!** Now you can start working with your dataset. Happy coding!