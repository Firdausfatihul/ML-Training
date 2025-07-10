

class SimpleLinearRegresion:
    def __init__(self, data):
        self.data = data
        self.x = [i[0] for i in data]
        self.y = [i[1] for i in data]
        self.x_mean = self.mean(self.x)
        self.y_mean = self.mean(self.y)

    def mean(self, data):
        return sum(data) / len(data)

    def numerator_denominator_slope(self):
        numerator = sum((x - self.x_mean) * (y - self.y_mean)for x, y in zip(self.x, self.y))
        denominator = sum(pow(x - self.x_mean, 2) for x in self.x)
        return numerator / denominator
    
    def intercept(self):
        return self.y_mean - self.numerator_denominator_slope() * self.x_mean

def main():
    #coordinate in xy
    data = [
        [0, 4],
        [1, 2],
        [2, 0],
        [3, -2]
    ]
    
    linear = SimpleLinearRegresion(data)

    print(linear.numerator_denominator_slope())
    print(linear.intercept())
    

if __name__ == "__main__":
    main()


