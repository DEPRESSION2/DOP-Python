stud = {'Vlad_Kalchenko':{'shema':7, 'fb':8, 'fb+':8, 'prackt':10, 'string':0, 'dict':0, 'git1':8, 'praktick':10, 'modul':10}, 
'Godynov_Nikita':{'shema':4, 'fb':6, 'fb+':6, 'prackt':10, 'string':0, 'dict':0, 'git1':6, 'praktick':10, 'modul':10},
'Goptarev_Denis':{'shema':6, 'fb':10, 'fb+':0, 'prackt':10, 'string':0, 'dict':0, 'git1':0, 'praktick':10, 'modul':10},
'Dzadyh_Yura':{'shema':7, 'fb':8, 'fb+':8, 'prackt':10, 'string':0, 'dict':0, 'git1':8, 'praktick':10, 'modul':10},
'Lisitskiy_Vlodimer':{'shema':7, 'fb':10, 'fb+':8, 'prackt':10, 'string':8, 'dict':8, 'git1':8, 'praktick':10, 'modul':10},
'Savchenko_Volodimer':{'shema':8, 'fb':10, 'fb+':9, 'prackt':10, 'string':8, 'dict':8, 'git1':8, 'praktick':10, 'modul':10},
'Trofimchuk_Volodimer':{'shema':8, 'fb':10, 'fb+':10, 'prackt':10, 'string':9, 'dict':10, 'git1':8, 'praktick':10, 'modul':10},
'Korchunov_Dmitriy':{'shema':7, 'fb':10, 'fb+':10, 'prackt':10, 'string':10, 'dict':10, 'git1':10, 'praktick':10, 'modul':10}}

for student in stud:
    s = 0
    for dist in stud[student]:
        s += stud[student][dist]
    s = s / len(stud[student])
    if s < 6:
    	print(f"Плохой ученик : {student} Оценка: {int(s)}")
    print(f"Ученик: {student}. Средняя оценка: {int(s)}")
    for dist,values in stud[student].items():
    	if values < 5:
    		 print(f"У ученика: {student} Проблемная тебя это:{dist}")