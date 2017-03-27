'''
Create 3rd table for questionnaire - fields - date | high/med/low ques string | Y/N
Use list_proc as the list used for traversing.
Assumed calender_processed table has one field highcal/lowcal

'''


import pymysql
import time
from datetime import datetime
from datetime import timedelta

#Tree
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)
		
		
		
		
#creating all nodes

#samysoawesome

root=Node("root")

#level1 nodes
high_pulse=Node("highpulse")
low_pulse=Node("lowpulse")

# level 2 nodes
high_cal0=Node("highcal")
low_cal0=Node("lowcal")
high_cal1=Node("highcal")
low_cal1=Node("lowcal")

#level 3 nodes

for i in range(0,4):
	exec('high_ques'+str(i) + '= Node("highques' +'")')


for i in range(0,4):
	exec('medium_ques'+str(i) + '= Node("mediumques' +'")')
	

for i in range(0,4):
	exec('low_ques'+str(i) + '= Node("lowques' +'")')

#level 4 nodes


for i in range(0,12):
	exec('mov'+str(i) + '= Node("mov' +'")')
	

for i in range(0,24):
	exec('nmov'+str(i) + '= Node("nomove' +'")')

#level 5 nodes


for i in range(0,24):
	exec('low_temp'+str(i) + '= Node("lowtemp' +'")')

for i in range(0,24):
	exec('normal_temp'+str(i) + '= Node("normaltemp'+'")')

for i in range(0,24):
	exec('sweating'+str(i) + '= Node("sweating' +'")')

for i in range(0,24):
	exec('nosweating'+str(i) + '= Node("nosweating' +'")')

	
	
	#level6

low_temp24 = Node("lowtemp/vs")
low_temp25 = Node("lowtemp/s")
low_temp26 = Node("lowtemp/vs")
low_temp27 = Node("lowtemp/s")
low_temp28 = Node("lowtemp/s")
low_temp29 = Node("lowtemp/ms")
low_temp30 = Node("lowtemp/vs")
low_temp31 = Node("lowtemp/ms")
low_temp32 = Node("lowtemp/ms")
low_temp33 = Node("lowtemp/ms")
low_temp34 = Node("lowtemp/s")
low_temp35 = Node("lowtemp/ms")
low_temp36 = Node("lowtemp/s")
low_temp37 = Node("lowtemp/ms")
low_temp38 = Node("lowtemp/s")
low_temp39 = Node("lowtemp/ms")
low_temp40 = Node("lowtemp/s")
low_temp41 = Node("lowtemp/ms")
low_temp42 = Node("lowtemp/s")
low_temp43 = Node("lowtemp/ms")
low_temp44 = Node("lowtemp/ms")
low_temp45 = Node("lowtemp/ms")
low_temp46 = Node("lowtemp/s")
low_temp47 = Node("lowtemp/ms")
low_temp48 = Node("lowtemp/s")
low_temp49 = Node("lowtemp/ms")
low_temp50 = Node("lowtemp/s")
low_temp51 = Node("lowtemp/ms")
low_temp52 = Node("lowtemp/ms")
low_temp53 = Node("lowtemp/ss")
low_temp54 = Node("lowtemp/ms")
low_temp55 = Node("lowtemp/ss")
low_temp56 = Node("lowtemp/ss")
low_temp57 = Node("lowtemp/ss")
low_temp58 = Node("lowtemp/c")
low_temp59 = Node("lowtemp/c")
low_temp60 = Node("lowtemp/c")
low_temp61 = Node("lowtemp/ss")
low_temp62 = Node("lowtemp/ss")
low_temp63 = Node("lowtemp/c")
low_temp64 = Node("lowtemp/c")
low_temp65 = Node("lowtemp/c")
low_temp66 = Node("lowtemp/ss")
low_temp67 = Node("lowtemp/c")
low_temp68 = Node("lowtemp/c")
low_temp69 = Node("lowtemp/c")
low_temp70 = Node("lowtemp/c")
low_temp71 = Node("lowtemp/c")
	
normal_temp24 = Node("normaltemp/vs")
normal_temp25 = Node("normaltemp/s")
normal_temp26 = Node("normaltemp/vs")
normal_temp27 = Node("normaltemp/s")
normal_temp28 = Node("normaltemp/ms")
normal_temp29 = Node("normaltemp/ss")
normal_temp30 = Node("normaltemp/ms")
normal_temp31 = Node("normaltemp/ss")
normal_temp32= Node("normaltemp/ms")
normal_temp33 = Node("normaltemp/ss")
normal_temp34 = Node("normaltemp/ms")
normal_temp35 = Node("normaltemp/ss")
normal_temp36 = Node("normaltemp/s")
normal_temp37 = Node("normaltemp/ss")
normal_temp38 = Node("normaltemp/s")
normal_temp39 = Node("normaltemp/ms")
normal_temp40 = Node("normaltemp/ms")
normal_temp41 = Node("normaltemp/ss") 
normal_temp42= Node("normaltemp/ms")
normal_temp43 = Node("normaltemp/ss")
normal_temp44 = Node("normaltemp/ms")
normal_temp45 = Node("normaltemp/ss")
normal_temp46 = Node("normaltemp/ms")
normal_temp47 = Node("normaltemp/ss")
normal_temp48 = Node("normaltemp/s")
normal_temp49 = Node("normaltemp/ms")
normal_temp50 = Node("normaltemp/s")
normal_temp51 = Node("normaltemp/ms")
normal_temp52= Node("normaltemp/ss")
normal_temp53 = Node("normaltemp/c")
normal_temp54 = Node("normaltemp/ss")
normal_temp55 = Node("normaltemp/c")
normal_temp56 = Node("normaltemp/ss")
normal_temp57 = Node("normaltemp/c")
normal_temp58 = Node("normaltemp/c")
normal_temp59 = Node("normaltemp/c")
normal_temp60 = Node("normaltemp/ss")
normal_temp61 = Node("normaltemp/c")
normal_temp62= Node("normaltemp/ss")
normal_temp63 = Node("normaltemp/c")
normal_temp64 = Node("normaltemp/c")
normal_temp65 = Node("normaltemp/c")
normal_temp66 = Node("normaltemp/c")
normal_temp67 = Node("normaltemp/ss")
normal_temp68 = Node("normaltemp/c")
normal_temp69 = Node("normaltemp/c")
normal_temp70 = Node("normaltemp/c")
normal_temp71 = Node("normaltemp/c")

sweating24 = Node("sweating/vs")
sweating25 = Node("sweating/vs")
sweating26 = Node("sweating/vs")
sweating27 = Node("sweating/vs")
sweating28 = Node("sweating/s")
sweating29 = Node("sweating/s")
sweating30 = Node("sweating/vs")
sweating31 = Node("sweating/vs")
sweating32 = Node("sweating/ms")
sweating33 = Node("sweating/ms")
sweating34 = Node("sweating/s")
sweating35 = Node("sweating/ms")
sweating36 = Node("sweating/s")
sweating37 = Node("sweating/ms")
sweating38 = Node("sweating/s")
sweating39 = Node("sweating/ms")
sweating40 = Node("sweating/s")
sweating41 = Node("sweating/s")
sweating42 = Node("sweating/vs")
sweating43 = Node("sweating/vs")
sweating44 = Node("sweating/ms")
sweating45 = Node("sweating/ms")
sweating46 = Node("sweating/ms")
sweating47 = Node("sweating/ms")
sweating48 = Node("sweating/s")
sweating49 = Node("sweating/s")
sweating50 = Node("sweating/s")
sweating51 = Node("sweating/s")
sweating52 = Node("sweating/ms")
sweating53 = Node("sweating/ms")
sweating54 = Node("sweating/ms")
sweating55 = Node("sweating/ms")
sweating56 = Node("sweating/ss")
sweating57 = Node("sweating/ss")
sweating58 = Node("sweating/ms")
sweating59 = Node("sweating/ss")
sweating60 = Node("sweating/ss")
sweating61 = Node("sweating/c")
sweating62 = Node("sweating/ss")
sweating63 = Node("sweating/c")
sweating64 = Node("sweating/c")
sweating65 = Node("sweating/c")
sweating66 = Node("sweating/ss")
sweating67 = Node("sweating/ss")
sweating68 = Node("sweating/c")
sweating69 = Node("sweating/c")
sweating70 = Node("sweating/c")
sweating71 = Node("sweating/c")


nosweating24 = Node("nosweating/s")
nosweating25 = Node("nosweating/s")
nosweating26 = Node("nosweating/s")
nosweating27 = Node("nosweating/s")
nosweating28 = Node("nosweating/ms")
nosweating29 = Node("nosweating/ms")
nosweating30 = Node("nosweating/ms")
nosweating31 = Node("nosweating/ms")
nosweating32 = Node("nosweating/ms")
nosweating33 = Node("nosweating/ss")
nosweating34 = Node("nosweating/ms")
nosweating35 = Node("nosweating/ss")
nosweating36 = Node("nosweating/s")
nosweating37 = Node("nosweating/ms")
nosweating38 = Node("nosweating/s")
nosweating39 = Node("nosweating/ms")
nosweating40 = Node("nosweating/ms")
nosweating41 = Node("nosweating/ms")
nosweating42 = Node("nosweating/ms")
nosweating43 = Node("nosweating/ms")
nosweating44 = Node("nosweating/ms")
nosweating45 = Node("nosweating/ss")
nosweating46 = Node("nosweating/ms")
nosweating47 = Node("nosweating/ss")
nosweating48 = Node("nosweating/ms")
nosweating49 = Node("nosweating/ms")
nosweating50 = Node("nosweating/ms")
nosweating51 = Node("nosweating/ms")
nosweating52 = Node("nosweating/ss")
nosweating53 = Node("nosweating/ss")
nosweating54 = Node("nosweating/ss")
nosweating55 = Node("nosweating/ss")
nosweating56 = Node("nosweating/ss")
nosweating57 = Node("nosweating/c")
nosweating58 = Node("nosweating/ss")
nosweating59 = Node("nosweating/c")
nosweating60 = Node("nosweating/ss")
nosweating61 = Node("nosweating/c")
nosweating62 = Node("nosweating/ss")
nosweating63 = Node("nosweating/c")
nosweating64 = Node("nosweating/c")
nosweating65 = Node("nosweating/c")
nosweating66 = Node("nosweating/c")
nosweating67 = Node("nosweating/c")
nosweating68 = Node("nosweating/c")
nosweating69 = Node("nosweating/c")
nosweating70 = Node("nosweating/c")
nosweating71 = Node("nosweating/c")

'''
for i in range(24,72):
	exec('low_temp'+str(i) + '= Node("lowtemp' + '")')


for j in range(24,72):
	exec('normal_temp'+str(j) + '= Node("normaltemp' + '")')
	
	
for k in range(24,72):
	exec('sweating'+str(k) + '= Node("sweating' + '")')
	

for l in range(24,72):
	exec('nosweating'+str(l) + '= Node("nosweating' +'")')
'''

	
	
	
	
#first children high_pulse and low_pulse
#level 1
root.add_child(high_pulse)
root.add_child(low_pulse)

#level2
#children of low_pulse : high_cal and low_cal
low_pulse.add_child(high_cal1)
low_pulse.add_child(low_cal1)
#children of high_pulse : high_cal and low_cal
high_pulse.add_child(high_cal0)
high_pulse.add_child(low_cal0)


#level3
#children of high_cal : high,med,low quest
high_cal0.add_child(high_ques0)
high_cal0.add_child(medium_ques0)
high_cal0.add_child(low_ques0)
#children of low_cal : high,med,low quest
low_cal0.add_child(high_ques1)
low_cal0.add_child(medium_ques1)
low_cal0.add_child(low_ques1)


#children of high_cal : high,med,low quest
high_cal1.add_child(high_ques2)
high_cal1.add_child(medium_ques2)
high_cal1.add_child(low_ques2)
#children of low_cal : high,med,low quest
low_cal1.add_child(high_ques3)
low_cal1.add_child(medium_ques3)
low_cal1.add_child(low_ques3)

#level4
#children of high_quest
high_ques0.add_child(mov0)
high_ques0.add_child(nmov0)

medium_ques0.add_child(mov1)
medium_ques0.add_child(nmov1)
low_ques0.add_child(mov2)
low_ques0.add_child(nmov2)

high_ques1.add_child(mov3)
high_ques1.add_child(nmov3)
medium_ques1.add_child(mov4)
medium_ques1.add_child(nmov4)
low_ques1.add_child(mov5)
low_ques1.add_child(nmov5)

high_ques2.add_child(mov6)
high_ques2.add_child(nmov6)
medium_ques2.add_child(mov7)
medium_ques2.add_child(nmov7)
low_ques2.add_child(mov8)
low_ques2.add_child(nmov8)

high_ques3.add_child(mov9)
high_ques3.add_child(nmov9)
medium_ques3.add_child(mov10)
medium_ques3.add_child(nmov10)
low_ques3.add_child(mov11)
low_ques3.add_child(nmov11)

#level 5
"""
j=0
for i in range(0,12):
	"mov"+str(i).add_child(low_temp+j)
	"mov"+str(i).add_child(normal_temp+j)
	"mov"+str(i).add_child(sweating+j)
	"mov"+str(i).add_child(nosweating+j)
	j=j+2
	
j=1
for i in range(0,12):
	"nmov"+str(i).add_child(low_temp+j)
	"nmov"+str(i).add_child(normal_temp+j)
	"nmov"+str(i).add_child(sweating+j)
	"nmov"+str(i).add_child(nosweating+j)
	j=j+2
"""

mov0.add_child(low_temp0)
mov0.add_child(normal_temp0)
mov0.add_child(sweating0)
mov0.add_child(nosweating0)


mov1.add_child(low_temp2)
mov1.add_child(normal_temp2)
mov1.add_child(sweating2)
mov1.add_child(nosweating2)


mov2.add_child(low_temp4)
mov2.add_child(normal_temp4)
mov2.add_child(sweating4)
mov2.add_child(nosweating4)


mov3.add_child(low_temp6)
mov3.add_child(normal_temp6)
mov3.add_child(sweating6)
mov3.add_child(nosweating6)

mov4.add_child(low_temp8)
mov4.add_child(normal_temp8)
mov4.add_child(sweating8)
mov4.add_child(nosweating8)


mov5.add_child(low_temp10)
mov5.add_child(normal_temp10)
mov5.add_child(sweating10)
mov5.add_child(nosweating10)


mov6.add_child(low_temp12)
mov6.add_child(normal_temp12)
mov6.add_child(sweating12)
mov6.add_child(nosweating12)

mov7.add_child(low_temp14)
mov7.add_child(normal_temp14)
mov7.add_child(sweating14)
mov7.add_child(nosweating14)

mov8.add_child(low_temp16)
mov8.add_child(normal_temp16)
mov8.add_child(sweating16)
mov8.add_child(nosweating16)


mov9.add_child(low_temp18)
mov9.add_child(normal_temp18)
mov9.add_child(sweating18)
mov9.add_child(nosweating18)


mov10.add_child(low_temp20)
mov10.add_child(normal_temp20)
mov10.add_child(sweating20)
mov10.add_child(nosweating20)
	

mov11.add_child(low_temp22)
mov11.add_child(normal_temp22)
mov11.add_child(sweating22)
mov11.add_child(nosweating22)


#************************************************************#
nmov0.add_child(low_temp1)
nmov0.add_child(normal_temp1)
nmov0.add_child(sweating1)
nmov0.add_child(nosweating1)


nmov1.add_child(low_temp3)
nmov1.add_child(normal_temp3)
nmov1.add_child(sweating3)
nmov1.add_child(nosweating3)


nmov2.add_child(low_temp5)
nmov2.add_child(normal_temp5)
nmov2.add_child(sweating5)
nmov2.add_child(nosweating5)


nmov3.add_child(low_temp7)
nmov3.add_child(normal_temp7)
nmov3.add_child(sweating7)
nmov3.add_child(nosweating7)

nmov4.add_child(low_temp9)
nmov4.add_child(normal_temp9)
nmov4.add_child(sweating9)
nmov4.add_child(nosweating9)


nmov5.add_child(low_temp11)
nmov5.add_child(normal_temp11)
nmov5.add_child(sweating11)
nmov5.add_child(nosweating11)


nmov6.add_child(low_temp13)
nmov6.add_child(normal_temp13)
nmov6.add_child(sweating13)
nmov6.add_child(nosweating13)

nmov7.add_child(low_temp15)
nmov7.add_child(normal_temp15)
nmov7.add_child(sweating15)
nmov7.add_child(nosweating15)

nmov8.add_child(low_temp17)
nmov8.add_child(normal_temp17)
nmov8.add_child(sweating17)
nmov8.add_child(nosweating17)


nmov9.add_child(low_temp19)
nmov9.add_child(normal_temp19)
nmov9.add_child(sweating19)
nmov9.add_child(nosweating19)

nmov10.add_child(low_temp21)
nmov10.add_child(normal_temp21)
nmov10.add_child(sweating21)
nmov10.add_child(nosweating21)

	
nmov11.add_child(low_temp23)
nmov11.add_child(normal_temp23)
nmov11.add_child(sweating23)
nmov11.add_child(nosweating23)



#level 6
#set0
'''
sweating00=Node("sweating")
nosweating00=Node("no sweating")
sweating01=Node("sweating")
nosweating01=Node("no sweating")
low_temp00=Node("low temp")
normal_temp00=Node("normal temp")
low_temp01=Node("low temp")
normal_temp01=Node("normal temp")
'''

low_temp0.add_child(sweating24)
low_temp0.add_child(nosweating24)

normal_temp0.add_child(sweating25)
normal_temp0.add_child(nosweating25)

sweating0.add_child(low_temp24)
sweating0.add_child(normal_temp24)
nosweating0.add_child(low_temp25)
nosweating0.add_child(normal_temp25)
'''
#set1
sweating10=Node("sweating")
nosweating10=Node("no sweating")
sweating11=Node("sweating")
nosweating11=Node("no sweating")
low_temp10=Node("low temp")
normal_temp10=Node("normal temp")
low_temp11=Node("low temp")
normal_temp11=Node("normal temp")
'''

low_temp1.add_child(sweating26)
low_temp1.add_child(nosweating26)
normal_temp1.add_child(sweating27)
normal_temp1.add_child(nosweating27)

sweating1.add_child(low_temp26)
sweating1.add_child(normal_temp26)
nosweating1.add_child(low_temp27)
nosweating1.add_child(normal_temp27)
'''
#set2
sweating20=Node("sweating")
nosweating20=Node("no sweating")
sweating21=Node("sweating")
nosweating21=Node("no sweating")
low_temp20=Node("low temp")
normal_temp20=Node("normal temp")
low_temp21=Node("low temp")
normal_temp21=Node("normal temp")
'''

low_temp2.add_child(sweating28)
low_temp2.add_child(nosweating28)
normal_temp2.add_child(sweating29)
normal_temp2.add_child(nosweating29)

sweating2.add_child(low_temp28)
sweating2.add_child(normal_temp28)
nosweating2.add_child(low_temp29)
nosweating2.add_child(normal_temp29)

'''
#set 3
sweating30=Node("sweating")
nosweating30=Node("no sweating")
sweating31=Node("sweating")
nosweating31=Node("no sweating")
low_temp30=Node("low temp")
normal_temp30=Node("normal temp")
low_temp31=Node("low temp")
normal_temp31=Node("normal temp")
'''

low_temp3.add_child(sweating30)
low_temp3.add_child(nosweating30)
normal_temp3.add_child(sweating31)
normal_temp3.add_child(nosweating31)

sweating3.add_child(low_temp30)
sweating3.add_child(normal_temp30)
nosweating3.add_child(low_temp31)
nosweating3.add_child(normal_temp31)



# set4

low_temp4.add_child(sweating32)
low_temp4.add_child(nosweating32)
normal_temp4.add_child(sweating33)
normal_temp4.add_child(nosweating33)

sweating4.add_child(low_temp32)
sweating4.add_child(normal_temp32)
nosweating4.add_child(low_temp33)
nosweating4.add_child(normal_temp33)

#set 5

low_temp5.add_child(sweating34)
low_temp5.add_child(nosweating34)
normal_temp5.add_child(sweating35)
normal_temp5.add_child(nosweating35)

sweating5.add_child(low_temp34)
sweating5.add_child(normal_temp34)
nosweating5.add_child(low_temp35)
nosweating5.add_child(normal_temp35)

#set6
low_temp6.add_child(sweating36)
low_temp6.add_child(nosweating36)
normal_temp6.add_child(sweating37)
normal_temp6.add_child(nosweating37)

sweating6.add_child(low_temp36)
sweating6.add_child(normal_temp36)
nosweating6.add_child(low_temp37)
nosweating6.add_child(normal_temp37)

#set7
low_temp7.add_child(sweating38)
low_temp7.add_child(nosweating38)
normal_temp7.add_child(sweating39)
normal_temp7.add_child(nosweating39)

sweating7.add_child(low_temp38)
sweating7.add_child(normal_temp38)
nosweating7.add_child(low_temp39)
nosweating7.add_child(normal_temp39)

#set8
low_temp8.add_child(sweating40)
low_temp8.add_child(nosweating40)
normal_temp8.add_child(sweating41)
normal_temp8.add_child(nosweating41)

sweating8.add_child(low_temp40)
sweating8.add_child(normal_temp40)
nosweating8.add_child(low_temp41)
nosweating8.add_child(normal_temp41)

#set9

low_temp9.add_child(sweating42)
low_temp9.add_child(nosweating42)
normal_temp9.add_child(sweating43)
normal_temp9.add_child(nosweating43)

sweating9.add_child(low_temp42)
sweating9.add_child(normal_temp42)
nosweating9.add_child(low_temp43)
nosweating9.add_child(normal_temp43)

#set10

low_temp10.add_child(sweating44)
low_temp10.add_child(nosweating4)
normal_temp10.add_child(sweating45)
normal_temp10.add_child(nosweating45)

sweating10.add_child(low_temp44)
sweating10.add_child(normal_temp44)
nosweating10.add_child(low_temp45)
nosweating10.add_child(normal_temp45)

#set11
low_temp11.add_child(sweating46)
low_temp11.add_child(nosweating46)
normal_temp11.add_child(sweating47)
normal_temp11.add_child(nosweating47)

sweating11.add_child(low_temp46)
sweating11.add_child(normal_temp46)
nosweating11.add_child(low_temp47)
nosweating11.add_child(normal_temp47)


#set12
low_temp12.add_child(sweating48)
low_temp12.add_child(nosweating48)
normal_temp12.add_child(sweating49)
normal_temp12.add_child(nosweating49)

sweating12.add_child(low_temp48)
sweating12.add_child(normal_temp48)
nosweating12.add_child(low_temp49)
nosweating12.add_child(normal_temp49)

#set13
low_temp13.add_child(sweating50)
low_temp13.add_child(nosweating50)
normal_temp13.add_child(sweating51)
normal_temp13.add_child(nosweating51)

sweating13.add_child(low_temp50)
sweating13.add_child(normal_temp50)
nosweating13.add_child(low_temp51)
nosweating13.add_child(normal_temp51)


#set14
low_temp14.add_child(sweating52)
low_temp14.add_child(nosweating52)
normal_temp14.add_child(sweating53)
normal_temp14.add_child(nosweating53)

sweating14.add_child(low_temp52)
sweating14.add_child(normal_temp52)
nosweating14.add_child(low_temp53)
nosweating14.add_child(normal_temp53)



#set15
low_temp15.add_child(sweating54)
low_temp15.add_child(nosweating54)
normal_temp15.add_child(sweating55)
normal_temp15.add_child(nosweating55)

sweating15.add_child(low_temp54)
sweating15.add_child(normal_temp54)
nosweating15.add_child(low_temp55)
nosweating15.add_child(normal_temp55)


#set16
low_temp16.add_child(sweating56)
low_temp16.add_child(nosweating56)
normal_temp16.add_child(sweating57)
normal_temp16.add_child(nosweating57)

sweating16.add_child(low_temp56)
sweating16.add_child(normal_temp56)
nosweating16.add_child(low_temp57)
nosweating16.add_child(normal_temp57)


#set17
low_temp17.add_child(sweating58)
low_temp17.add_child(nosweating58)
normal_temp17.add_child(sweating59)
normal_temp17.add_child(nosweating59)

sweating17.add_child(low_temp58)
sweating17.add_child(normal_temp58)
nosweating17.add_child(low_temp59)
nosweating17.add_child(normal_temp59)

#set18
low_temp18.add_child(sweating60)
low_temp18.add_child(nosweating60)
normal_temp18.add_child(sweating61)
normal_temp18.add_child(nosweating61)

sweating18.add_child(low_temp60)
sweating18.add_child(normal_temp60)
nosweating18.add_child(low_temp61)
nosweating18.add_child(normal_temp61)

#set19
low_temp19.add_child(sweating62)
low_temp19.add_child(nosweating62)
normal_temp19.add_child(sweating63)
normal_temp19.add_child(nosweating63)

sweating19.add_child(low_temp62)
sweating19.add_child(normal_temp62)
nosweating19.add_child(low_temp63)
nosweating19.add_child(normal_temp63)

#set20
low_temp20.add_child(sweating64)
low_temp20.add_child(nosweating64)
normal_temp20.add_child(sweating65)
normal_temp20.add_child(nosweating65)

sweating20.add_child(low_temp64)
sweating20.add_child(normal_temp64)
nosweating20.add_child(low_temp65)
nosweating20.add_child(normal_temp65)

#set21
low_temp21.add_child(sweating66)
low_temp21.add_child(nosweating66)
normal_temp21.add_child(sweating67)
normal_temp21.add_child(nosweating67)

sweating21.add_child(low_temp66)
sweating21.add_child(normal_temp66)
nosweating21.add_child(low_temp67)
nosweating21.add_child(normal_temp67)

#set22
low_temp22.add_child(sweating68)
low_temp22.add_child(nosweating68)
normal_temp22.add_child(sweating69)
normal_temp22.add_child(nosweating69)

sweating22.add_child(low_temp68)
sweating22.add_child(normal_temp68)
nosweating22.add_child(low_temp69)
nosweating22.add_child(normal_temp69)

#set23
low_temp23.add_child(sweating70)
low_temp23.add_child(nosweating70)
normal_temp23.add_child(sweating71)
normal_temp23.add_child(nosweating71)

sweating23.add_child(low_temp70)
sweating23.add_child(normal_temp70)
nosweating23.add_child(low_temp71)
nosweating23.add_child(normal_temp71)




conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
cur_q = conn.cursor()
q_q = """SELECT * FROM quest"""
r_q = cur_q.execute(q_q)
rows_q = cur_q.fetchall()
for i in rows_q:
	ques =	i[0]
	if("Y" in i[1]):
		sweat=1
	else:
		sweat=0

cal=0	
cur_c = conn.cursor()
now = datetime.now()
str_now = now.date().isoformat()
q_c = """SELECT * FROM calendar_processed where eventDate = %s"""
r_c = cur_c.execute(q_c, (str_now))
rows_c = cur_c.fetchall()
for i in rows_c:
	cal =	i[2];
print(cal)
old_heart = "highpulse"
while(1):
	conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
	cur = conn.cursor()
	t1 = datetime.now()
	t2 = datetime.now() - timedelta(seconds=12)
	
	q1 = """SELECT * FROM temperature WHERE time BETWEEN %s AND %s"""
	q2 = """SELECT * FROM pulse"""
	q3 = """SELECT * FROM gsr WHERE time BETWEEN %s AND %s"""
	q4 = """SELECT * FROM accel WHERE time BETWEEN %s AND %s"""
	
	#temperature
	r1 = cur.execute(q1, (t2,t1))
	rows1 = cur.fetchall()
	for i in rows1:
		temp = i[3]
	#pulse
	r2 = cur.execute(q2)
	'''
	#print('///////////////',r2)
	rows2 = cur.fetchall()
	if(r2):
		for i in rows2:
			print('****------',i)
			new_heart = i
			old_heart = new_heart
	else:
		new_heart=old_heart
	'''
	rows2 = cur.fetchall()
	if(rows2):
		for i in rows2:
			new_heart = i[3]
	else:
		new_heart ="lowpulse"
	
	#gsr
	r3 = cur.execute(q3, (t2,t1))
	rows3 = cur.fetchall()
	for i in rows3:
		gsr = i[2]
	
	#accel
	r4 = cur.execute(q4, (t2,t1))
	rows4 = cur.fetchall()
	for i in rows4:
		accel = i[2]
	
	
	list_proc = []
	list_proc.append(new_heart)
	list_proc.append(cal)
	list_proc.append(ques)
	list_proc.append(accel)
	if(sweat==0):
		list_proc.append(temp)
		list_proc.append(gsr)
	else:
		list_proc.append(gsr)
		list_proc.append(temp)
		
	print(list_proc)
	print()
	print()
	#PUT RECURSION CODE HERE

	list_index = 0

	def traverse(root,list_index):
		list_str = list_proc[list_index]
		children_number= len(root.children)
		if(children_number>0):
			for i in range(children_number):
				if(len(root.children[i].children)>0):
					if(list_str == root.children[i].data):
						print(root.children[i].data)
						list_index = list_index+1
						traverse(root.children[i],list_index)
				else:
					text = root.children[i].data
					print_list = text.split("/")
					if(list_str == print_list[0]):
						print(print_list[0])
						print(print_list[1])
					
						if(print_list[1]=="vs"):
							str_level = "VeryStressed"
							level="10"
						elif(print_list[1]=="s"):
							str_level = "Stressed"
							level="7";
						elif(print_list[1]=="ms"):
							str_level = "MildlyStressed"
							level="5";
						elif(print_list[1]=="ss"):
							str_level = "SlightlyStressed"
							level="3";
						elif(print_list[1]=="c"):
							str_level = "Calm";
							level="1";
							
						print(str_level)
						print(level)
						conn = pymysql.connect(host='localhost', db='smartjacket_sensors', user='root')
						cur_s = conn.cursor()
						query = """INSERT INTO graph VALUES(%s,%s,%s)"""
						now_s = datetime.now()
						cur_s.execute(query,(now_s,str_level,level))
						conn.commit()
						return	
			
						
	traverse(root,list_index)
	time.sleep(12)

#for i in low_cal1.children:
	#print(i.data)

	
#samysoawesome
"""

for i in root.children:
	print(i.data)
	if(hb="high_pulse"):
		for j in  high_pulse.children:
			if(cal=="high_cal"):
					
"""			
		

	