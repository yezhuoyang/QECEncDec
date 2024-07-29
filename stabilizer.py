import numpy as np

class QuantumState:

    def __init__(self,num_qubit):
        self._num_qubit=num_qubit
        self._state_vec={"0"*num_qubit:1}

    def show_state(self):
        for key in self._state_vec.keys():
            print(str(self._state_vec[key])+"|"+key+">")
    
    def normalize(self):
        summation=0
        for key in self._state_vec.keys():
            summation=summation+self._state_vec[key]*np.conjugate(self._state_vec[key])
        summation=np.sqrt(summation)
        for key in self._state_vec.keys():
            self._state_vec[key]=self._state_vec[key]/summation

    '''
    Multiply I+XZX
    '''
    def enc_stablizer(self,String):
        new_state_vec={}
        for key in self._state_vec.keys():
            if key in new_state_vec.keys():
                new_state_vec[key]=new_state_vec[key]+self._state_vec[key]
            else:
                new_state_vec[key]=self._state_vec[key]
            newstatekey=""
            sign=1
            for index in range(0,len(key)):
                if(String[index]=="I"):
                    newstatekey=newstatekey+key[index]
                elif(String[index]=="Z"):
                    newstatekey=newstatekey+key[index]
                    if(key[index]=="1"):
                        sign=(-1)*sign
                elif(String[index]=="X"):
                    if(key[index]=="1"):
                        newstatekey=newstatekey+"0"
                    else:
                        newstatekey=newstatekey+"1"
            if newstatekey in new_state_vec.keys(): 
                new_state_vec[newstatekey]=new_state_vec[newstatekey]+sign*self._state_vec[key]
            else:
                new_state_vec[newstatekey]=sign*self._state_vec[key]           
        self._state_vec=new_state_vec


    def enc_stabilizer_group(self,stabilizer):
        for stabstring in stabilizer._stringList:
            self.enc_stablizer(stabstring)
        self.normalize()


    '''
    Multiply I+XZX
    '''
    def act_stablizer(self,String):
        new_state_vec={}
        for key in self._state_vec.keys():
            if key in new_state_vec.keys():
                new_state_vec[key]=new_state_vec[key]+self._state_vec[key]
            else:
                new_state_vec[key]=self._state_vec[key]
            newstatekey=""
            sign=1
            for index in range(0,len(key)):
                if(String[index]=="I"):
                    newstatekey=newstatekey+key[index]
                elif(String[index]=="Z"):
                    newstatekey=newstatekey+key[index]
                    if(key[index]=="1"):
                        sign=(-1)*sign
                elif(String[index]=="X"):
                    if(key[index]=="1"):
                        newstatekey=newstatekey+"0"
                    else:
                        newstatekey=newstatekey+"1"
            if newstatekey in new_state_vec.keys(): 
                new_state_vec[newstatekey]=new_state_vec[newstatekey]+sign*self._state_vec[key]
            else:
                new_state_vec[newstatekey]=sign*self._state_vec[key]           
        self._state_vec=new_state_vec


    def act_stabilizer_group(self,stabilizer):
        for stabstring in stabilizer._stringList:
            self.act_stablizer(stabstring)
        self.normalize()

    '''
    check whether sthe stabilizer stabilize the state
    '''    
    def check_stablizer(self,String):
        pass



class Stabilizer:

    '''
    Initialize the stabilizer by a string list such as ["ZZI","ZIZ","IZZ"]
    '''
    def __init__(self,num_qubit,stringList):
        self._num_qubit=num_qubit
        self._stringList=stringList