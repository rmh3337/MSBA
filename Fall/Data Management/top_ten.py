from mrjob.job import MRJob

class MRTopTen(MRJob):
    
    def mapper(self, _, line):
        # mapper code goes here
        for num in line.split('\t'):
            yield 1, int(num)
   
    def reducer(self, key, value):
        #reducer code goes here
        list1 = []
        for num in value:
            list1.append(int(num))
        for x in range(10):
            best = max(list1)
            list1.remove(max(list1))
            yield key, best
        
        
if __name__ == '__main__':
    MRTopTen.run()