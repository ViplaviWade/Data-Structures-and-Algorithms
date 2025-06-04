def filter_active_employees(employee_list):
    return [
        {
            'name': emp.get('name'),
            'email': emp.get('email'),
            'salary': emp.get('salary')
        }
        for emp in employee_list
        if emp.get('active')  and emp.get('salary', 0) > 50000 and emp.get('email')
    ]
