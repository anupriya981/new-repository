# EXCEPTION ERROR

#  index error
# x=[1,2,3]
# print(x[3])




#                                                               key error
# staff={1:'geetha',2:'swapna',3:'mahesh'}
# print(staff[4])

# employe_dict={'name':'arya','age':20,'ID':75893469473870}
# emp_id=employe_dict['ID']
# emp_cate=employe_dict['category']
# print(emp_id)
# print(emp_cate)

            #  key error exception handling

emp_dict={'name':'arya','age':20,'ID':75893469473870}

try:
    emp_id=emp_dict['ID']
    print(emp_id)
    emp_cate=emp_dict['category']
    print(emp_cate)

Except KeyError as ke:
    print('not found',ke)
    


