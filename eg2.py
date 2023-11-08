emp_dict ={ 'name':'arya','age':20,'ID':75893469473870}

try:
    emp_id = emp_dict['ID']
    print(emp_id)
    emp_cate=emp_dict['category']
    print(emp_cate)

except KeyError as ke:
    print('key not found in employee dict:',ke)
    