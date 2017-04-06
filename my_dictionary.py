class MyDictionary:

   def __init__(self):
       self.keys = []
       self.values=[]

   def insert_element(self,key,element):
       if (self.find_element[key] == -1):
           self.keys.append[key]
           self.values.append[element]

   def find_element(self, key):
       for x in xrange(0,self.size):
           if (self.keys[x] == key):
               return x
       return -1;

   def remove_element(self, key):
       if(self.find_element != -1):
           self.keys.remove(self.keys.find_element[keys])
           self.values.remove(self.keys.find_element[keys])

   def keys(self):
       return self.keys

   def elements(self):
       return self.values

   def isEmpty(self):
       if (self.size() == 0):
           return True
       else:
           return False
   def size(self):
       return len(self.keys)

dictionary = MyDictionary()

dictionary.insert_element(‘james’,100)
dictionary.insert_element(‘doug’,50)
dictionary.insert_element(‘jim’,10)
dictionary.insert_element(‘julie’,11)
dictionary.insert_element(‘keyur’,77)

dictionary.find_element(‘james’)
dictionary.remove_element(‘james’)
dictionary.keys()
dictionary.elements()
dictionary.size()
dictionary.remove(‘doug’)
dictionary.remove(‘jim’)
dictionary.remove(‘julie’)
dictionary.remove(‘keyur’)

dictionary.isEmpty()
