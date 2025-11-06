class dynamicArray:
    def __init__(self):
        self.capacity = 2
        self.array = self._make_array(self.capacity)
        self.n = 0

    def _make_array(self,capacity):
        "Creates a low-level array"
        return [None] * capacity
    
    def __len__(self):
        return self.n
    
    def __getitem__(self,index):
        if not 0 <= index < self.n:
            raise IndexError("Index out of bounds")
        return self.array[index]
    

    def append(self,value):
        "Add Element in the array"
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.array[self.n] = value
        self.n += 1

    def _resize(self,new_capacity):
        "Resize internal array to new capacity"
        new_array = self._make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        print(f"Resized to {new_capacity}")

    def _shrink(self):
        """Shrinking the size of the array"""
        if self.capacity > 2 and self.n <= self.capacity // 4:
            new_capacity = max(2,self.capacity // 2)
            new_array = self._make_array(new_capacity)
            for i in range(self.n):
                new_array[i] = self.array[i]
            self.array = new_array
            self.capacity = new_capacity
            print(f"Shrunk to {new_capacity}")

    def pop(self):
        "Remove and return last element"
        if self.n == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.n-1]
        self.array[self.n-1] = None
        self.n -= 1
        self._shrink()
        return value
    
    def insert(self,num,target):
        "Insert any element in the array "
        if target > self.n or target<0:
            raise IndexError("Index out of bound")
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        for i in range(self.n-1,target-1,-1):
            self.array[i+1] = self.array[i]
        self.array[target] = num
        self.n += 1

    def delete(self,target):
        "Delete any element in the array"
        if target > self.n or target < 0:
            raise IndexError("Index out of bound")
        for i in range(target,self.n-1):
            self.array[i] = self.array[i+1]
        self.array[self.n-1] = None
        self.n -= 1
        self._shrink()

    def maxElement(self):
        "Find the max element in the array"
        max = self.array[0]
        for i in range(self.n):
            if self.array[i] > max:
                max = self.array[i]
        return max
    
    def reverse(self):
        "Reverse of the array"
        ar = []
        for i in range(self.n-1,0,-1):
            ar.append(self.array[i])
        return ar
    
    def countGreater(self,num):
        "Count number greater than num"
        cnt = 0
        for i in range(self.n):
            if self.array[i] > num:
                cnt += 1

        return cnt 
    
    
    
    def __repr__(self):
        return str([self.array[i] for i in range(self.n)])


arr = dynamicArray()
for i in range(10):
    arr.append(i)
# for i in range(75):
#     arr.pop()
# for i in range(5000,10000):
#     arr.append(i)
print(arr)    
arr.insert(12,5)
arr.delete(2)
max = arr.maxElement()
print(arr)
print("Max element is : ",max)
ar = arr.reverse()
print("Reverse of the array is : ",ar)
cnt = arr.countGreater(4)
print("Number greater than 4 are : ",cnt)
print(arr.__len__())