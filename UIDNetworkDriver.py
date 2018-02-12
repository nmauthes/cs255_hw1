import sys, random, math 
# remove commented out part to generate the plot.
#import matplotlib.pyplot as plt
#import numpy as np

class MockComputer:
    
    def __init__(self):
        '''Initialises the MockComputer's id
           to a random value
        '''
        self.__ID = self.round()

    def round(self, i = None):
        '''Computes ids of length at most O(log i) many bits.      
        '''
        if i == None:
            return random.randint(0,10)
        ID = random.randint(0,((2**i.bit_length())))
        self.__ID = ID

    def getId(self):
        '''Returns the ID of the MockComputer
        '''
        return self.__ID

class UIDNetworkDriver(MockComputer):
    
    def __init__(self, n):
        '''Creates a list of MockComputers
        '''
        self.computers = [ MockComputer() for i in range (n)]

    def __referee(self, out):
        '''Checks to ensure that no two MockComputers
           have the same id
        '''
        elements = set()
        for x in out:
            if x in elements:
                return False
            elements.add(x)
        return True

    def permute(self , mode):
        '''Repeatedly assigns a new set of ids to the
           MockComputers until the referee declares that 
           they are unique
        '''
        i = 1
        while(1):
            output = [comp.getId() for comp in self.computers]
            print_output = [str(id) for id in output]
            if self.__referee(output) is False:
                for comp in self.computers:
                    comp.round(len(self.computers) + i - 1) 
            else:
                result = max(output).bit_length()
                print("Round ", i , ": "," ". join(print_output), "Max Bits ", result)
                return  result
                break
            if mode == "verbose":
                print("Round ", i , ": "," ". join(print_output), "Max Bits ", max(output).bit_length())
            i = i + 1

if __name__ == '__main__' :
    if len(sys.argv) != 3:
        print ("Please supply the correct arguments")
        raise SystemExit(1)
    n = int(sys.argv[1])
    mode = str(sys.argv[2])
    result = []
#    for n in range (2,200):
    test = UIDNetworkDriver(n)
    result.append(test.permute(mode))
#    plt.plot(np.array(range(2,200)),np.array(result))
#    plt.xlabel('n')
#    plt.ylabel("max bits")
#    plt.show()

    
