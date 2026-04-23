import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Step 1: merge tables
    df = employee.merge(department, left_on="departmentId", right_on="id")
    
    # Step 2: find max salary per department
    max_salary = df.groupby("name_y")["salary"].transform("max")
    
    # Step 3: filter rows where salary is max
    result = df[df["salary"] == max_salary]
    
    # Step 4: format output
    result = result[["name_y", "name_x", "salary"]]
    result.columns = ["Department", "Employee", "Salary"]
    
    return result