class BubbleSort(object):

  def swap(self, array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

  def sort(self, array):
    for i in range(len(array) - 1):
      for j in range(0, len(array) - 1 - i, 1): # (start, To, step)
        if array[j] > array[j + 1]:
          self.swap(array, j, j + 1)

    return array

# test It
if __name__ == '__main__':
  notSortedArray = [1, -2, 4, 0, 200, -299, 20]
  bubble = BubbleSort()
  sortedArray = bubble.sort(notSortedArray)

  print(sortedArray)