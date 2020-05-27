import pandas as pd
from pandas import ExcelWriter
from pandas import DataFrame


existing=pd.read_excel('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage1/Raw-Data.xlsx', sheet_name='Existing employees')
left= pd.read_excel('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage1/Raw-Data.xlsx', sheet_name='Employees who have left')

existing['left']=0

left['left']=1

print(existing.dtypes)
print(left.dtypes)

frames=[existing,left]
res=pd.concat(frames)


res=res.sort_values('Emp ID')
#print(res)

writer = ExcelWriter('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage1/Merged_data.xlsx')
res.to_excel(writer,'Merged',index=False)
writer.save()
