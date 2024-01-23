import numpy as np

def data_synthetic():
    data_dimension = 100
    data_nums = 1000
    c = 0.3
    p = 0.5
    m = 5

    # step 1:  get the orthogonal unit vector m1, m2
    m1 = np.random.normal(size=data_dimension)
    # z score normalization
    m1 = (m1 - np.mean(m1)) / (np.std(m1) * np.sqrt(data_dimension))

    m2 = np.random.normal(size=data_dimension)
    # calculate the orthogonal vector
    dot_product = np.dot(m1, m2)
    m2 = m2 - dot_product * m1
    # normalization
    m2 = m2 / np.linalg.norm(m2)

    # step 2: get w1, w2
    w1 = c * m1
    w2 = c * (p * m1 + np.sqrt(1-p**2) * m2)

    # step 3: get alpha and beta
    alpha = np.random.normal(size=m)
    beta = np.random.normal(size=m)
    y1 = []
    y2 = []
    input = []

    # step 4: get y1 and y2
    for i in range(data_nums):
        x = np.random.normal(size=data_dimension)
        input.append(x)

        linear_part1 = w1.dot(input)
        linear_part2 = w2.dot(input)

        nolinear_part1, nolinear_part2 = 0.0, 0.0
        for j in range(m):
            nolinear_part1 += np.sin(alpha[j]*linear_part1 + beta[j])
            nolinear_part2 += np.sin(alpha[j]*linear_part2 + beta[j])

        y1.append(linear_part1 + nolinear_part1 + np.random.normal(scale=0.1, size=1))
        y2.append(linear_part2 + nolinear_part2 + np.random.normal(scale=0.1, size=1))