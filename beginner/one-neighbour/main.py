def euclidean_distance(p1, p2):
    sum_squared_differences = sum(pow(a-b, 2) for a,b in zip(p1,p2))
    return sum_squared_differences**0.5

def closest_point(new_p, dataset):
    min = 1000
    for data in dataset:
        temp = euclidean_distance(new_p, data[:2])
        print(str(new_p) + " | " + str(data) + " | " + str(temp) +"\n")
        if (temp < min):
            #temp = 0.2
            #min = 0
            # 0.2 < 0 false
            min = temp
            temp_var = data
            
    print(min)
    print(temp_var)


def main():
    dataset = \
    [
        [2,3, 'red'],
        [4,5, 'blue'],
        [1,1, 'red'], 
    ]

    new_point = [3,3]
    closest_point(new_point, dataset)

if __name__ == "__main__":
    main()


    