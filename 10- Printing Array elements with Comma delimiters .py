

'''
------Instructions------

Input: Array of elements
["h","o","l","a"]
Output: String with comma delimited elements of the array in th same order.
"h,o,l,a"
Note: if this seems too simple for you try the next level
Note2: the input data can be: boolean array, array of objects, array of string arrays



------Test Cases------'
  data = [2]
  Result= "2"

  data = [2,4,5,2]
  Result= "2,4,5,2"

  data = [2,4,5,2]
  Result= "2,4,5,2"

  data = [2.0,4.2,5.1,2.2]
  Result= "2.0,4.2,5.1,2.2"

  data = ["2","4","5","2"]
  Result= "2,4,5,2"

  data = [True,False,False]
  Result= "True,False,False"

  array1 = ["hello", "this", "is", "an", "array!"]
  array2 = ["a", "b", "c", "d", "e!"]
  data = array1+array2
  Result= "hello,this,is,an,array!,a,b,c,d,e!"

  array1 = ["hello", "this", "is", "an", "array!"]
  array2 = [1, 2, 3, 4, 5]
  data = [array1,array2]
  Result= "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]"
 

 

------Solution------
'''

def print_array(arr):
#    return ','.join(arr) #only works for an array of string. does not work for an array of numbers
    return ','.join(str(x) for x in arr)
