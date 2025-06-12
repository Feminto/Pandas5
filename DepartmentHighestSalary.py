# Method 1
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # creating a dictionary with department ID and it's max salary
    dept_sal = {}
    for i in range(len(employee)):
        d = employee['departmentId'][i]
        s = employee['salary'][i]

        if d in dept_sal.keys():
            if dept_sal[d] < s:
                dept_sal[d] = s
        else:
            dept_sal[d] = s
        
    # print(dept_sal)

    # Checking which emloyees have max salary for each department
    result = []
    for i in range(len(employee)):
        d = employee['departmentId'][i]
        s = employee['salary'][i]
        n = employee['name'][i]

        if s == dept_sal[d]:
            result.append([d,n,s])
    
    # print(result)

    # Capturing the department name from department table
    final_result = []
    for i in range(len(department)):
        id = department['id'][i]
        name = department['name'][i]

        for e in result:
            if id == e[0]:
                final_result.append([name,e[1],e[2]])

    print(final_result)

    return pd.DataFrame(final_result, columns = ['department','employee','salary'])

# Method 2
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', how = 'inner')
    max_sal = df.groupby('departmentId')['salary'].transform('max') # SELECT MAX(salary) FROM df GROUP BY departmentId

    # print(max_sal)

    condition = df['salary'] == max_sal
    df = df[condition]

    return df[['name_y','name_x','salary']].rename(columns = {'name_y':'department','name_x':'employee','salary':'salary'})