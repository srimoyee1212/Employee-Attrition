import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage1/Merged_data.xlsx', sheet_name='Merged')

print(df.info())

left = df.groupby('left')
print(left.mean())

labels1=('current employee','ex-employee')
left_count=df.groupby('left').count()
plt.bar(left_count.index.values, left_count['Emp ID'])
plt.xlabel('current status')
plt.xticks(left_count.index.values,labels1)
plt.ylabel('Number of Employees')
plt.savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/barplot.png')
plt.show()

print(df.left.value_counts())


plt.title("Employee plots")
sns.countplot(x="satisfaction_level", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/1-satisfaction_level.png')
plt.show()

sns.countplot(x="last_evaluation", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/2-last_evaluation.png')
plt.show()

sns.countplot(x="number_project", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/3-number_project.png')
plt.show()

sns.countplot(x="average_montly_hours", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/4-average_monthly_hours.png')
plt.show()

sns.countplot(x="time_spend_company", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/5-time_spend_company.png')
plt.show()

sns.countplot(x="Work_accident", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/6-work_accident.png')
plt.show()

sns.countplot(x="promotion_last_5years", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/7-promotion.png')
plt.show()

sns.countplot(x="dept", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/8-dept.png')
plt.show()

sns.countplot(x="salary", hue="left", data=df,palette='BuGn').get_figure().savefig('/home/srimoyee/Desktop/Srimoyee-PROJECT_REPORT/stage2/9-salary.png')
plt.show()


