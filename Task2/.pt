import pandas as pd

def analyze_employee_data():
    data = {
        "Employee": ["Anu", "Ravi", "Suresh", "Meena", "Kiran"],
        "Department": ["IT", "HR", "IT", "Finance", "IT"],
        "Salary": [45000, 38000, 52000, 47000, 60000]
    }

    df = pd.DataFrame(data)

    print(" Employee Data\n")
    print(df)

    avg_salary = df["Salary"].mean()
    max_salary = df["Salary"].max()

    print("\n Analysis")
    print("Average Salary:", avg_salary)
    print("Highest Salary:", max_salary)

    it_employees = df[df["Department"] == "IT"]

    print("\n IT Department Employees")
    print(it_employees)

    df.to_csv("employee_salary_report.csv", index=False)
    print("\n CSV file saved as employee_salary_report.csv")

if __name__ == "__main__":
    analyze_employee_data()
