def filter_active_employees(employee_list):
    result = []
    for emp in employee_list:
        if emp.get('active') == True and emp.get('salary', 0) > 50000 and emp.get('email') is not None:
            result.append({
                'name': emp.get('name'),
                'email': emp.get('email'),
                'salary': emp.get('salary')
            })
    return result
