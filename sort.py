#coding=utf-8
######################################
#author: suzhilong
#data: 2020/3/16
#github: https://github.com/suzhilong
######################################
import math

#插入排序=直接插入排序+希尔排序
def insertion_sort(origin_data, trend=0):
	'''
	遍历元素，把每个待排序元素插入到前面有序列表里
	trand=0是递增
	trand=1是递减
	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	counter = 0 #记录比较了几次
	for i in range(1,len(data)):
		target = data[i]
		j = i
		if trend==0:#递增
			while j>0 and data[j-1]>target:
				counter += 1
				data[j] = data[j-1]
				j -= 1
				if j==0:
					counter -= 1 #下次不进入while循环，但是还是在下面语句+1
			counter += 1 #没有进入while循环的比较
			data[j] = target
		if trend==1:#递减
			while j>0 and data[j-1]<target:
				data[j] = data[j-1]
				j -= 1
			data[j] = target
	# print 'Comparation times of insertion sort:',counter
	return data

def shell_sort(origin_data):
	'''
	将待排序数组按照步长step进行分组，然后将每组的元素利用直接插入排序的方法进行排序；
	step初始一般为列表长度的一半；
	每次将step折半减小，循环上述操作；
	当step=1时，用直接插入排序完成排序

	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	step = int(len(data)/2)
	counter = 0 #记录比较次数
	while step>0: #控制步长
		for i in range(0,step): #控制组数
			for j in range(i+step,len(data),step): #组内直接插入排序
				target = data[j]
				while j>i and data[j-step]>target:
					counter += 1
					data[j] = data[j-step]
					j -= step
					if j==i:
						counter -= 1 #下次不进入while循环，但是还是在下面语句+1
				data[j] = target
				counter += 1
		step /= 2
	
	# print 'Comparation times of shell sort:',counter
	return data

#选择排序=简单选择排序+堆排序
def selection_sort(origin_data):
	'''
	从第一个遍历序列，遍历指针右边（含指针所指元素）为待排序序列；
	从待排序序列中，找到关键字最小的元素；
	如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
	这样就能保证指针左边为排好序的
	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	for i in range(len(data)):
		min_index = i
		for j in range(i+1,len(data)):
			if data[j]<data[min_index]:
				min_index = j
		# 互换元素可写成
		# tmp = data[i]
		# data[i] = data[min_index]
		# data[min_index] = tmp
		(data[min_index],data[i]) = (data[i],data[min_index])
	return data

def heap_sort(origin_data):
	'''
	大根堆：每个节点的值都大于或等于其子节点的值，用于升序排列；
	小根堆：每个节点的值都小于或等于其子节点的值，用于降序排列
	1. 将序列建立成大顶堆
	2. 取根节点（最大值）与末尾元素交换
	3. 将交换后的n-1和序列调整成大顶堆
	一直重复2、3步骤
	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	#调整为大根堆
	def adjustHeap(data,parents,end):
		'''
		将以parents为根节点的子树调整为大根堆，
		因为每调整一次，就有一个最大值到位，
		end是data中待排堆d的尾序号;
		可以用递归和循环实现
		但是递归容易栈溢出
		'''
		#非叶子结点parents的两个子节点（假设都存在）
		lchild = 2*parents+1
		rchild = 2*parents+2
		biggest = parents
		if lchild <= end and data[lchild]>data[biggest]:
			biggest = lchild
		if rchild <= end and data[rchild]>data[biggest]:
			biggest = rchild
		if biggest != parents:
			(data[parents],data[biggest]) = (data[biggest],data[parents])
			#交换之后，biggest的索引应该是较小的元素，所以应该向下继续调整
			adjustHeap(data,biggest,end)
	#建堆
	def buildHeap(data):
		for i in range((len(data)//2)-1,-1,-1):
			#从倒数第一个非叶子结点开始调整
			adjustHeap(data,i,len(data)-1)
	#排序
	buildHeap(data)
	for i in range(len(data)-1,0,-1):
		#从最后一个索引往前遍历，依次把大根堆的最大元素与指针交换
		(data[i],data[0]) = (data[0],data[i])
		#交换之后待排序序列中的最大值放到指针处，调整堆时待排序列最后索引要减1
		adjustHeap(data,0,i-1)
	return data

#交换排序=冒泡排序+快速排序
def bubble_sort(origin_data):
	'''
	重复地遍历要排序的数列，一次比较两个元素（指针 和 指针+1），如果他们的顺序错误就把他们交换过来;
	走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成
	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	for i in range(len(data)):
		swap = False #这一遍有没有交换的标志
		for j in range(len(data)-i-1):#i个最大值已经在最后面 不用比较
			if data[j]>data[j+1]:
				swap = True #只要有交换 就设为True
				data[j],data[j+1] = data[j+1],data[j]
		if not swap: #没有任何交换 说明已经是有序的了
			return data
	return data

def quick_sort(origin_data, normal=False):
	'''
	https://zh.wikipedia.org/wiki/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F
	普通的快排（需要额外的存储空间）：normal==True
	选定一个基准值pivot，遍历序列把比pivot小的放在一个序列less，比pivot大的放在另一个序列greater，
	再连起来(less,pivot,greater)，递归处理less和greater

	'''
	data = origin_data[:]
	if len(data)<2:
		return data
	#####普通的快排######################################################
	if normal == True:
		print 'normal quick'
		pivot = data[0]
		lessData = [x for x in data[1:] if x < pivot]
		greaterData = [x for x in data[1:] if x >= pivot]
		return quick_sort(lessData,True) + [pivot] + quick_sort(greaterData,True)
	###################################################################
	def quickSort(data,low,high):
		left = low
		right = high
		if left >= right:
			return
		pivot = data[left]
		while left < right:
			while left<right and data[right]>=pivot:
				right -= 1
			data[left] = data[right]
			while left<right and data[left]<pivot:
				left += 1
			data[right] = data[left]
		data[right] = pivot
		quickSort(data,low,right-1)
		quickSort(data,right+1,high)
	quickSort(data,0,len(data)-1)
	return data

#归并排序
def merge_sort(origin_data):
	'''
	采用分治法：
	分割：递归地把当前序列平均分割成两半。
	集成：在保持元素顺序的同时将上一步得到的子序列集成到一起（归并）。
	'''
	data = origin_data[:]
	if len(data)<2:
		return data

	#用pop实现
	def merge2ordered(data1,data2):		
		data = []
		while data1 and data2:
			if data1[0]<=data2[0]:
				data.append(data1.pop(0))
			else:
				data.append(data2.pop(0))
		if data1:
			data += data1
		if data2:
			data += data2
		return data

	mid = len(data)//2
	left = data[:mid]
	right = data[mid:]
	left = merge_sort(left)
	right = merge_sort(right)
	return merge2ordered(left,right)

	'''
	#用索引实现
	def merge2ordered(data1,data2):
		if len(data1)>1:
			data1 = merge2ordered(data1[:len(data1)//2],data1[len(data1)//2:])
		if len(data2)>1:
			data2 = merge2ordered(data2[:len(data2)//2],data2[len(data2)//2:])
		i1 = i2 = 0
		data = []
		while i1<len(data1) and i2<len(data2):
			if data1[i1]<=data2[i2]:
				data.append(data1[i1])
				i1 += 1
			else:
				data.append(data2[i2])
				i2 += 1
		if i1==len(data1):
			data.extend(data2[i2:]) # data += data2[i2:]也可以
		elif i2==len(data2):
			data.extend(data1[i1:])
		return data
		
	return merge2ordered(data[:len(data)//2],data[len(data)//2:])
	'''

#基数排序
def redix_sort(origin_data,radix=10):
	'''
	将数按位数切割成不同的数字，然后按每个位数分别比较
	基数排序有两种方法：
	MSD（主位优先法）：从高位开始进行排序，再逐个对各分组按次高位进行子排序
	LSD（次位优先法）：从低位开始进行排序
	ridix是基数，可以为任意进制，缺省10
	此方法为LSD
	此方法不能处理负数，序列有负数还需进一步改进
	'''
	data = origin_data[:]
	if len(data)<2:
		return data

	K = int(math.ceil(math.log(max(data)+1, radix))) #求出最大数的位数
	for i in range(1,K+1):
		buckets = [[] for j in range(radix)]
		for val in data:
			buckets[val%(radix)**i // (radix)**(i-1)].append(val)
		del data[:]
		for nums in buckets: #桶合并
			data.extend(nums)
	return data

def main():
	data = [6,7,103,7,2020,7,1,92,3,4,5,10]#[2,4,5,3,1]
	insert_data = insertion_sort(data)
	shell_data = shell_sort(data)
	select_data = selection_sort(data)
	heap_data = heap_sort(data)
	bubble_data = bubble_sort(data)
	quick_data = quick_sort(data)#,True)
	merge_data = merge_sort(data)
	redix_data = redix_sort(data)

	# output
	print 'insertion:\n',insert_data 
	print 'shell:\n',shell_data
	print 'selection:\n',select_data
	print 'heap:\n',heap_data
	print 'bubble:\n',bubble_data
	print 'quick:\n',quick_data
	print 'merge:\n',merge_data
	print 'redix:\n',redix_data

if __name__ == '__main__':
	main()