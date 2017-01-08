
process_queue = []
def main():
	
	total_wtime = 0
	total_processes = int(raw_input('Enter the total no of processes: '))
	for count in xrange(total_processes):
    		process_queue.append([])#append a list object to the list 
    		process_queue[count].append(raw_input('Enter p_name: '))
    		process_queue[count].append(int(raw_input('Enter p_arrival: ')))
    		total_wtime += process_queue[count][1]
    		process_queue[count].append(int(raw_input('Enter p_bust: ')))
    		print ''
	
	display(total_processes)
	avgWTime(total_wtime,total_processes)
	logic(total_processes)
	
	
	return 0

def display(total_processes):
	print 'ProcessName\tArrivalTime\tBurstTime'
	for count in xrange(total_processes):
        	print process_queue[count][0],'\t\t',process_queue[count][1],'\t\t',process_queue[count][2]

def logic(total_processes):
	from operator import itemgetter
	#for count in xrange(1, total_processes, 1):
	print "###gantt chart###"
	print sorted(process_queue , key = itemgetter(1))
		#count = count+1 
			
def avgWTime(total_wtime,total_processes):
	print "total waiting time :" , total_wtime
	print "average waiting time :" , (total_wtime/total_processes)

if __name__== "__main__":main()					


