from MathOperations.addition import Addition

class Median:
    @staticmethod
    def median(data):
        n = len(data)
        s = sorted(data)
        return (Addition.sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None