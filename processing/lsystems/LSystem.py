# Ported version from:
# https://github.com/nature-of-code/noc-examples-processing/blob/master/chp08_fractals/NOC_8_09_LSystem/Turtle.pde

class Turtle:
    def __init__(self, sentence, linelen, theta):
        self.sentence = sentence
        self.linelen = linelen
        self.theta = theta

    def render(self):
        stroke(0, 175);
        for c in self.sentence:
            if c == 'F':
                line(0, 0, self.linelen, 0)
                translate(self.linelen, 0)
            elif c == 'G':
                translate(self.linelen, 0)
            elif c == '+':
                rotate(self.theta)
            elif c == '-':
                rotate(-self.theta)
            elif c == '[':
                pushMatrix()
            elif c == ']':
                popMatrix()
    

class LSystem:
    '''
    axiom -> (str)
    
    ruleset -> (dict)
        + key: str to replace
        + val: str to replace with
        
    Example:
    ========
    
    ruleset = {
      "A" : "AB", # replace instances of "A" with "AB"
      "B" : "BA", # replace instances of "B" with "BA"
    }
    '''
    def __init__(self, axiom, ruleset):
        self.axiom = axiom
        self.ruleset = ruleset
        
    def generate(self):
        next_gen = ''
        for c in self.axiom:
            if c in self.ruleset.keys():
                next_gen += self.ruleset[c]
            else:
                next_gen += c
        
        self.axiom = next_gen
        return next_gen
