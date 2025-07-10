import math


def euclidean_distance(p1, p2):
    sum_squared_differences = sum(pow(p2[i]-p1[i], 2) for i in range(len(p1)))
    return math.sqrt(sum_squared_differences)

def main():
    p1 = [1,1]
    p2 = [2,2]

    print(euclidean_distance(p1, p2))

    p1_5d = [10, 20, 30, 40, 50]
    p2_5d = [12, 23, 31, 45, 50]
    print(f"5D distance: {euclidean_distance(p1_5d, p2_5d)}")

    p1_5d = [10, 20, 30]
    p2_5d = [12, 23, 31]
    print(f"3D distance: {euclidean_distance(p1_5d, p2_5d)}")

if __name__ == "__main__":
    main()