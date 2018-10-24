from HeapInt import *

'''*
 * An implementation of a minimum heap with handles
 * By Peter Unrein 2/15/17
 '''

class Heap:

    def __init__(self):
        '''
          The constructor has been set up with an initial array of size 4
          so that your doubleHeap() method will be tested.  Don't change
          this!
        '''
        self.array = [0]*4
        self.heapsize = 0
        self.arraysize = 4


    def exchange(self, pos1, pos2):
        '''
          Exchanges that values at positions pos1 and pos2 in the heap array.
          Handles must be exchanged correctly as well.
          Uses pythons tuple swap pattern
          x, y = y, x
          is supposedly the most efficient way to swap variables in python
          Running time = O(1)
        '''
        self.array[pos1],self.array[pos2] = self.array[pos2], self.array[pos1]
        pos1Handle = self.array[pos1].getHandle()
        self.array[pos1].setHandle(self.array[pos2].getHandle())
        self.array[pos2].setHandle(pos1Handle)


    def doubleHeap(self):
        '''
          Doubles the size of the array.  A new array is created, the elements in
          the heap are copied to the new array, and the array data member is set
          to the new array.  Data member arraysize is set to the size of the
          new array.

          Running time = O(n)
        '''
        newarray =  [0]*self.arraysize*2
        for i in range(self.arraysize):
            newarray[i] = self.array[i]
        self.array = newarray
        self.arraysize = self.arraysize * 2
        # Provide your implementation here



    def heapifyDown(self, pos):
        '''
          Fixes the heap if the value at position pos may be bigger than one of
          its children.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(????)
        '''
        left = pos * 2
        right = pos * 2 +1
        if left <= self.heapsize and self.array[left].getKey() < self.array[pos].getKey():
            smallest = left
        else:
            smallest = pos
        if right <= self.heapsize and self.array[right].getKey() < self.array[smallest].getKey():
            smallest = right
        if pos != smallest:

            self.exchange(pos,smallest)
            self.heapifyDown(smallest)
        # Provide your implementation here



    def heapifyUp(self, pos):
        """
          Fixes the heap if the value at position pos may be smaller than its
          parent.  Using exchange() to swap elements will simplify your
          implementation.  HeapElts contain records, and records contain
          keys; you will need to decide how to handle comparisons.

          Running time = O(lg(n))
        """
        parent = pos//2
        while pos > 1 and self.array[pos].getKey() < self.array[parent].getKey():

            self.exchange(pos,parent)
            pos = parent
            parent = pos//2
        # Provide your implementation here



    def insert(self, inElt):
        '''
          Insert inElt into the heap.  Before doing so, make sure that there is
          an open spot in the array for doing so.  If you need more space, call
          doubleHeap() before doing the insertion.

          Running time = O(lg(n)) (NOTE that there are a couple of different cases
          here!)
        '''
        self.heapsize += 1
        if self.heapsize == self.arraysize -1:

            self.doubleHeap()
        self.array[self.heapsize] = inElt
        self.array[self.heapsize].setHandle(self.heapsize)
        self.heapifyUp(self.heapsize)

        # Provide your implementation here


    def removeMin(self):
        '''
          Remove the minimum element from the heap and return it.  Restore
          the heap to heap order.  Assumes heap is not empty, and will
          cause an exception if the heap is empty.

          Running time = O(lg(n))
        '''
        assert(self.heapsize > 0), "heap is empty!"
        if(self.heapsize == 1):
            self.heapsize = self.heapsize-1
            return self.array[1]
        else:
            self.exchange(1,self.heapsize)
            self.heapsize -= 1
            self.heapifyDown(1)
            return self.array[self.heapsize+1]
        # Provide your implementation here


    def getHeapsize(self):
        '''
          Return the number of elements in the heap..

          Running time = O(1)
        '''
        return self.heapsize
        # Provide your implementation here


    def printHeap(self):
        '''
          Print out the heap for debugging purposes.  It is recommended to
          print both the key from the record and the handle.

          Running time = O(n)
        '''
        i = 1
        while i <= self.heapsize:
            print(self.array[i])
            i += 1


        # Provide your implementation here
