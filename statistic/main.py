class Statistics:
    def __init__(self, data):
        if not isinstance(data, list) or not data:
            raise ValueError("Data must be a non-empty list.")
        
        self.data = data

    def _bubble_sort(self):
        data = self.data.copy()
        n = self.len()

        for i in range(n):
            for j in range(n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
            
        return data

    def _backward_bubble_sort(self):
        data = self.data.copy()
        n = self.len()

        for i in range(n):
            for j in range(n-i-1):
                if data[j] < data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
            
        return data

    def sum(self):
        n = self.len()
        sum = 0
        for i in range(n):
            sum += self.data[i]

        return sum

    def len(self):
        len = 0
        for i in self.data:
            len += 1

        return len

    def mean(self):
        return self.sum() / self.len()

    def median(self):
        n = self.len()
        sorted_data = self._bubble_sort()
        median_pos = n//2
        if n % 2 != 0:
            return sorted_data[int(median_pos)]

        median_avg = sorted_data[median_pos] + sorted_data[median_pos-1]
        
        return median_avg / 2

    def map_data(self):
        map_data = {}
        n = self.len()

        for i in range(n):
            if self.data[i] in map_data:
                map_data[self.data[i]] += 1
            else:
                map_data[self.data[i]] = 1
        return map_data

    def range(self):
        return self.max()-self.min()

    def mode_number(self):
        map_data = self.map_data()
        max = 0
        for num, count in map_data.items():
            max = count
            if count > max:
                max = count
        return max


    def variance(self):
        n = self.len()
        variance = 0
        for i in range(n):
            variance += pow(self.data[i]-self.mean(),2)
        return variance/n

    def max(self):
        n = self.len()
        max = self.data[0]
        for i in range(n):
            if max < self.data[i]:
                max = self.data[i]
        return max


    def min(self):
        n = self.len()
        min = self.data[0]
        for i in range(n):
            if min > self.data[i]:
                min = self.data[i]
        return min

    def std_dev(self):
        return (self.variance())**0.5

        



def main():
    data = [0,2,1,5,6,9,3,3]
    stats = Statistics(data)
    sorted_data = stats._bubble_sort()
    backward_sort = stats._backward_bubble_sort()
    print(backward_sort)
    print(sorted_data)

    summed = stats.sum()
    print(summed)

    mean = stats.mean()
    print(mean)

    median = stats.median()
    print(median)

    range = stats.range()
    print(range)

    mode = stats.mode_number()
    print(mode)

    variance = stats.variance()
    print(variance)

    std_dev = stats.std_dev()
    print(std_dev)
    

if __name__ == "__main__":
    main()