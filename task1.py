'''
input : log_file
output : memory and cpu utilization graph
'''


import re
import matplotlib.pyplot as plt
from datetime import datetime

#open and read the contents of the file
infile=open('alpha_board_router_stats.txt','r')
lines=infile.readlines()
memfile=open("mem.txt",'w+')
cpufile=open("cpu.txt",'w+')

memused=[]
cpuused=[]
memtime=[]
cputime=[]
memtotal=[]

#slice lines to extract memory utilization values and cpu utilization values
for line in lines:
    line=line.strip()
    if "Mem:   " in line:
    #if re.match(r"Mem:      *",line):
        memfile.write(line+"\n")
        memused.append(line[23:29])
        memtime.append(line[74:101])
        memtotal.append(line[12:19])
        
    if "Average: " in line and "all"  in line:
        cpufile.write(line+"\n")
        cpuused.append(line[74:79])
        cputime.append(line[80:107])

        
        

print("$$$ MEMORY stats  $$$")        
print("total entries ", len(memused))
memused = [int(i) for i in memused]
memtotal=[int(i) for i in memtotal]
memused=[(i/j)*100 for i,j in zip(memused,memtotal)] #resultant memused -> percentage utilization ie memused/total memory
print("max : ",max(memused))
print("min : ",min(memused))
print("average : ",sum(memused)/len(memused),"\n\n")


print("$$$ CPU stats  $$$")
print("total entries : ",len(cpuused))
#print("check :" ,cputime[2])
cpuused = [100-float(i) for i in cpuused]   #cpuused -> percentage utilization
print("max : ",max(cpuused))
print("min : ",min(cpuused))
print("average : ",sum(cpuused)/len(cpuused))


memtime=[datetime.strptime(i,"%Y-%m-%d %H:%M:%S.%f") for i in memtime]
#print(memtime[1])

#plot graph for memory and cpu utilization 
plt.plot(memtime,memused)
plt.xlabel('time')
plt.ylabel('percentage utilization')
plt.title('Router memory utilization ')
plt.ylim(0,100)
#plt.legend()
plt.savefig('mem.png', bbox_inches='tight')
plt.show()



cputime=[datetime.strptime(i,"%Y-%m-%d %H:%M:%S.%f") for i in cputime]
plt.plot(cputime,cpuused)
plt.xlabel('time')
plt.ylim(0,100)
plt.ylabel('percentage utilization')
plt.title('Router CPU utilization ')
#plt.legend()
plt.savefig('cpu.png', bbox_inches='tight')
plt.show()




infile.close()
memfile.close()
cpufile.close()

