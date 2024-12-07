from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or
class QueryBuilder:
    def __init__(self):
        self._matchers = []
    
    def build(self):
        result = And(*self._matchers)
        self._matchers = []
        return result
        #return And(*self._matchers)
    
    def plays_in(self, team):
        self._matchers.append(PlaysIn(team))
        return self
    
    def has_at_least(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self
    
    def has_fewer_than(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self
    
    def one_of(self, *matchers):
        self._matchers.append(Or(*matchers))
        return self
    