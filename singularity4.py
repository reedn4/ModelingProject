import copy
class Sig:
    def __init__(self, a, p, f=1):
        self.pow = p
        self.loc = a
        self.fact = f
        self.func = self.toFunc()
        self.integF = self.integ().toFunc()
        self.integS = self.integ().integ().toFunc()

    def toFunc(self):
        if self.pow < 0:
            def helper(x):
                if x == self.loc:
                    return 0
                else:
                    return 0
        else:
            def helper(x):
                if x < self.loc:
                    return 0
                else:
                    return self.fact*(x-self.loc)**self.pow
        return helper

    def integ(self):
        temp = copy.deepcopy(self)
        temp.pow += 1
        if temp.pow > 0:
            temp.fact = temp.fact*(1/temp.pow)
        return temp

    def deriv(self):
        temp = copy.deepcopy(self)
        if temp.pow > 0:
            temp.fact = temp.fact*temp.pow
        temp.pow -= 1
        return temp
    
class SigCol:
    def __init__(self, lst=[]):
        for sig in lst:
            assert isinstance(sig, Sig)
        self.lst = lst
        self.func = self.sumSig()
        self.integF = self.integ1()
        self.integS = self.integ2()
        
    def sumSig(self):
        def helper(x):
            temp = 0
            for obj in self.lst:
                temp += obj.func(x)
            return temp
        return helper

    def addSig(self,sLst):
        for sig in sLst:
            assert isinstance(sig, Sig)
            self.lst += [sig]
        self.func = self.sumSig()

    def integ1(self):
        def helper(x):
            temp = 0
            for obj in self.lst:
                temp += obj.integF(x)
            return temp
        return helper

    def integ2(self):
        def helper(x):
            temp = 0
            for obj in self.lst:
                temp += obj.integS(x)
            return temp
        return helper

    def deriv(self):
        def helper(x):
            temp = 0
            for obj in self.lst:
                temp += obj.deriv().toFunc()(x)
            return temp
        return helper
