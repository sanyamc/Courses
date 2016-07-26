
import heapq

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        #newMatrix=[[0 for w in range(0,n)] for h in range(0,n)]
        heap = [i for i in range(n*n)]
        heapq.heapify(heap)

        for index,row in enumerate(matrix):

            count=0
            if(len(heap)==0):
                return
            
            start=heap.pop()
            row=start//n
            column=start%n
            while(count<n):
                count+=1
                newIndex=((start+1)*n-(index))%(n*n)-1
                newRow=newIndex//n
                newColumn=newIndex%n
                toSwap = matrix[row][column]
                matrix[row][column]=matrix[newRow][newColumn]
                start=newRow*newColumn
                row=newRow
                column=newColumn
                if(count!=1):
                    heap.remove(start)
                   
        """"    for i,val in enumerate(row):
                newIndex=((i+1)*n - (index))%(n*n)-1
                print("newIndex: "+str(newIndex))
                newRow = newIndex//n
                newColumn = newIndex%n
                print("row: "+str(row)+" newRow:"+ str(newRow))
                print("column: "+str(i)+" newColumn: "+str(newColumn))
                newMatrix[newRow][newColumn]=matrix[index][i]
        matrix=newMatrix""""
        print(matrix)


s=Solution()
matrix = [[1,2],[3,4]]
s.rotate(matrix)
print(matrix)
