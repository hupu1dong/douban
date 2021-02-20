import xlwt


# worksheet.write(0,0,'hello')    #写入数据，第一个参数行，第二个参数列，第三个内容
# workbook.save('students.xls')   #保存数据表
# for item in range(0,9):
#     for st in range(0,9):
#         sum = (st+1)*(item+1)
#         worksheet.write(item,st,str(st+1)+'*'+str(item+1)+'='+str(sum))
#         workbook.save('students4.xls',)
workbook = xlwt.Workbook(encoding="utf-8")  #创建workbook对象
worksheet = workbook.add_sheet('sheet1')    #创建工作表

for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save('student.xls')