import sys, random, math

class MockComputer:
    
    def __init__(self):
        '''Initialises the MockComputer's id
           to a random value
        '''
        self.ID = self.round()

    def round(self, i = None):
        '''Computes ids of length at most O(log i) many bits.      
        '''
        if i == None:
            return random.randint(0,10)
        ID = random.randint(0,((2**i.bit_length())))
        self.ID = ID

    def getId(self):
        '''Returns the ID of the MockComputer
        '''
        return self.ID

class UIDNetworkDriver:
    
    def __init__(self, n):
        '''Creates a list of MockComputers
        '''
        self.computers = [ MockComputer() for i in range (n)]

    def __refree(self, out):
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
           MockComputers until the refree declares that 
           they are unique
        '''
        i = 1
        while(1):
            output = [comp.getId() for comp in self.computers]
            print_output = [str(id) for id in output]
            if self.__refree(output) is False:
                for comp in self.computers:
                    comp.round(len(self.computers) + i - 1) 
            else:
                print("Round ", i , ": "," ". join(print_output), "Max Bits ", max(output).bit_length())
                break
            if mode == "verbose":
                print("Round ", i , ": "," ". join(print_output), "Max Bits ", max(output).bit_length())
            i = i + 1


if __name__ == '__main__' :
    if len(sys.argv) != 3:
        print ("Please supply the correct arguments")
        raise SystemExit(1)

    test = UIDNetworkDriver(int(sys.argv[1]))
    test.permute(str(sys.argv[2]))

    