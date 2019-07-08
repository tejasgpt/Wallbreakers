class Solution(object):
    def countOfAtoms(self, formula):
        """
        PROBLEM STATEMENT:
        Given a formula, output the count of all elements as a string in the following form: 
        the first name (in sorted order), 
        followed by its count (if that count is more than 1), 
        followed by the second name (in sorted order), 
        followed by its count (if that count is more than 1), and so on.
        :type formula: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(formula):
            char = formula[i]
            if char == '(':
                stack.append(char)
            elif char == ')':
                temp = dict()
                while stack[len(stack)-1] != '(':
                    curr = stack.pop()
                    for element, count in curr.items():
                        if element in temp:
                            temp[element] += count
                        else:
                            temp[element] = count
                stack.pop()
                stack.append(temp)
        
            elif char.isdigit():
                num = int(char)
                j = i + 1
                while j < len(formula) and formula[j].isdigit():
                    num *= 10
                    num += int(formula[j])
                    j += 1
                i = j-1
                
                pre = stack.pop()
                new = dict()
                for element, count in pre.items():
                    new[element] = count * num
                stack.append(new)
                
            else:
                t = char + ""
                j = i+1
                while j < len(formula) and formula[j].islower():
                    t = t + formula[j]
                    j += 1
                i = j-1
                stack.append({str(t): 1})
            i += 1
            
        res = dict()
        while len(stack) != 0:
            curr = stack.pop()
            for element, count in curr.items():
                if element in res:
                    res[element] += count
                else:
                    res[element] = count
                    
        atoms = ""
        total = []
        for element, count in res.items():
            total.append((element, count))
            
        total.sort(key = lambda x: x[0])
        
        for element, count in total:
            if count == 1:
                atoms += element
            else:
                atoms += element + str(count)
        
        return atoms
