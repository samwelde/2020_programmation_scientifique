import numpy as np
import matplotlib.pyplot as plt
import csv
import math

# Ex 1
# a)

iris_data_file = open("06_iris.csv", "r")
csv_reader = csv.reader(iris_data_file)
iris_data_mat = np.array(list(csv_reader))
iris_data_file.close()

print(iris_data_mat)
print("here")
# b)
def print_info():
    row1 = iris_data_mat[0]     #header
    print("{} | {} | {} | {} | {} ".format(row1[0], row1[1], row1[2], row1[3], row1[4]))

    for row in iris_data_mat[1:]:
        print("{:>12.6f} | {:>11.6f} | {:>12.6f} | {:11.6f} | {} ".format(float(row[0]), float(row[1]), float(row[2]), float(row[3]), row[4]))

print_info()

# Ex 2

# b)
def mean(mat, col):
    col_sum = 0
    for row in mat[1:]:
        col_sum += float(row[col])
    mean = col_sum / len(mat[1:])
    return mean

def std_dev(mat, col):
    mat_mean = mean(mat, col)
    sum = 0
    for row in mat[1:]:
        sum += (float(row[col]) - mat_mean) ** 2
    sd = math.sqrt(sum/len(mat[1:]))
    return sd

# a)
# i)
def print_info():
    print("Statistiques")
    print("Nombre de caractéristiques: {}".format(len(iris_data_mat[0])-1))
    print("Nombre total d'iris. {}".format(len(iris_data_mat)-1))
    print("Nombre total de versicolor. {}".format(len([0 for row in iris_data_mat[1:] if row[4] == "versicolor"])))
    print("Mean sepal length: {:.3f}".format(mean(iris_data_mat, 0)))
    print("Std deviation of petal width: {:.3f}".format(std_dev(iris_data_mat, 3)))
    print("")


    row1 = iris_data_mat[0]
    print("{} | {} | {} | {} | {}".format(row1[0], row1[1], row1[2],row1[3], row1[4]))
    print("-----------------------------------------------------------------")

    for row in iris_data_mat[1:]:
        print("{:>12.6f} | {:>11.6f} | {:>12.6f} | {:>11.6f} |{}".format(float(row[0]), float(row[1]), float(row[2]),float(row[3]), row[4]))
print_info()


# d) Understand these codes!
# Load the iris values as float
iris_values = np.genfromtxt('06_iris.csv', delimiter=',', skip_header=1,usecols=[0, 1, 2, 3], dtype=float)

# Load the iris labels as strings
iris_labels = np.genfromtxt('06_iris.csv', delimiter=',', skip_header=1, usecols=[4], dtype='str')

print(iris_values.shape)
print(iris_labels.shape)

mean_sepal_length = iris_values[:, 0].mean()
print("Mean of sepal length = {:.3f} [cm]".format(mean_sepal_length))

sdev_sepal_length = iris_values[:, 0].std()
print("Std. dev. of sepal length = {:.3f} [cm]".format(sdev_sepal_length))

mean_petal_width = iris_values[:, 3].mean()
print("Mean of petal width = {:.3f} [cm]".format(mean_petal_width))

sdev_petal_width = iris_values[:, 3].std()
print("Std. dev. of petal width = {:.3f} [cm]".format(sdev_petal_width))

#e)

setosas_sepal_lengths = []
setosas_sepal_widths = []
setosas_petal_lengths = []
setosas_petal_widths = []

for index, label in enumerate(iris_labels):
    if label == 'setosa':
     setosas_sepal_lengths.append(iris_values[index][0])
     setosas_sepal_widths.append(iris_values[index][1])
     setosas_petal_lengths.append(iris_values[index][2])
     setosas_petal_widths.append(iris_values[index][3])

xs = np.arange(len(setosas_petal_widths))

plt.subplot(221)
plt.scatter(xs, setosas_sepal_lengths)
plt.axhline(np.array(setosas_sepal_lengths).mean(), color='red')
plt.ylabel("cm")
plt.title("sepal_lengths")

plt.subplot(222)
plt.scatter(xs, setosas_sepal_widths)
plt.axhline(np.array(setosas_sepal_widths).mean(), color='red')
plt.title("sepal_widths")

plt.subplot(223)
plt.scatter(xs, setosas_petal_lengths)
plt.axhline(np.array(setosas_petal_lengths).mean(), color='red')
plt.ylabel("cm")
plt.title("petal_lengths")

plt.subplot(224)
plt.scatter(xs, setosas_petal_widths)
plt.axhline(np.array(setosas_petal_widths).mean(), color='red')
plt.title("petal_widths")

plt.show()

#Ex 3
#a )

column_names = iris_data_mat[0][:-1] # ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

def insert_hist(ax, feature_col_name):
    feature_col_index = -1
    for index, name in enumerate(column_names):
        if name == feature_col_name:
            feature_col_index = index

    feature_vals = []

    for row in iris_values:
        feature_vals.append(row[feature_col_index])
    ax.hist(feature_vals)

def insert_scatter(ax, feature1_col_name, feature2_col_name):
    feature1_col_index = feature2_col_index = -1

    for index, name in enumerate(column_names):
        if name == feature1_col_name:
            feature1_col_index = index
        elif name == feature2_col_name:
            feature2_col_index = index

    setosa_f1_vals = []
    setosa_f2_vals = []
    versicolor_f1_vals = []
    versicolor_f2_vals = []
    virginica_f1_vals = []
    virginica_f2_vals = []

    for index, row in enumerate(iris_values):
        if iris_labels[index] == 'setosa':
            setosa_f1_vals.append(row[feature1_col_index])
            setosa_f2_vals.append(row[feature2_col_index])
        elif iris_labels[index] == 'versicolor':
             versicolor_f1_vals.append(row[feature1_col_index])
             versicolor_f2_vals.append(row[feature2_col_index])
        elif iris_labels[index] == 'virginica':
             virginica_f1_vals.append(row[feature1_col_index])
             virginica_f2_vals.append(row[feature2_col_index])

    ax.scatter(setosa_f1_vals, setosa_f2_vals, color='red', marker='o')
    ax.scatter(versicolor_f1_vals, versicolor_f2_vals, color='green',marker='d')
    ax.scatter(virginica_f1_vals, virginica_f2_vals, color='blue',marker='*')

def show_plot():
    fig = plt.figure(figsize=(10, 10))
 # 1 row
    ax11 = fig.add_subplot(441)
    insert_hist(ax11, 'sepal_length')
    ax11.set_xlabel('sepallength')
    ax11.xaxis.set_label_position('top')
    ax11.set_ylabel('sepal length')
    ax11.yaxis.set_label_position('left')

    ax12 = fig.add_subplot(442)
    ax12.set_xlabel('sepal width')
    ax12.xaxis.set_label_position('top')
    insert_scatter(ax12, 'sepal_width', 'sepal_length')

    ax13 = fig.add_subplot(443)
    ax13.set_xlabel('petal length')
    ax13.xaxis.set_label_position('top')
    insert_scatter(ax13, 'petal_length', 'sepal_length')

    ax14 = fig.add_subplot(444)
    ax14.set_xlabel('petal width')
    ax14.xaxis.set_label_position('top')
    insert_scatter(ax14, 'petal_width', 'sepal_length')

    # 2 row
    ax21 = fig.add_subplot(445)
    ax21.yaxis.set_label_position('left')
    ax21.set_ylabel('petal width')
    insert_scatter(ax21, 'sepal_length', 'sepal_width')

    ax22 = fig.add_subplot(446)
    # ax22.hist(df.loc[:,['Sepal.Width']].values)
    insert_hist(ax22, 'sepal_width')

    ax23 = fig.add_subplot(447)
    insert_scatter(ax23, 'petal_length', 'sepal_width')

    ax24 = fig.add_subplot(448)
    insert_scatter(ax24, 'petal_width', 'sepal_width')

    # 3 row
    ax31 = fig.add_subplot(449)
    ax31.yaxis.set_label_position('left')
    ax31.set_ylabel('petal length')
    insert_scatter(ax31, 'sepal_length', 'petal_length')

    ax32 = fig.add_subplot(4, 4, 10)
    insert_scatter(ax32, 'sepal_width', 'petal_length')

    ax33 = fig.add_subplot(4, 4, 11)
    # ax33.hist(df.loc[:,['Petal.Length']].values)
    insert_hist(ax33, 'petal_length')

    ax34 = fig.add_subplot(4, 4, 12)
    insert_scatter(ax34, 'petal_width', 'petal_length')

    # 4 row
    ax41 = fig.add_subplot(4, 4, 13)
    ax41.yaxis.set_label_position('left')
    ax41.set_ylabel('petal width')
    insert_scatter(ax41, 'sepal_length', 'petal_width')

    ax42 = fig.add_subplot(4, 4, 14)
    insert_scatter(ax42, 'sepal_width', 'petal_width')

    ax43 = fig.add_subplot(4, 4, 15)
    insert_scatter(ax43, 'petal_length', 'petal_width')

    ax44 = fig.add_subplot(4, 4, 16)
    # ax44.hist(df.loc[:,['Petal.Width']].values)

    insert_hist(ax44, 'petal_width')
    plt.tight_layout()
    plt.savefig('iris_features_scatter_matrix.png')
    plt.show()

    # Delete the outlier
    index_to_delete = np.argmax(iris_values[:, 0])
    iris_values = np.delete(iris_values, index_to_delete, 0)
    iris_labels = np.delete(iris_labels, index_to_delete, 0)

    show_plot()

# Ex 4

# a)
# b)
# c)

def classify (iris_values):
    predicted_labels = []

    for iris_value in iris_values:
        petal_length = iris_value[2]
        if petal_length < 2.5:
            predicted_labels.append('setosa')
        elif petal_length < 5:
            predicted_labels.append('versicolor')
        else:
            predicted_labels.append('virginica')
    return predicted_labels

# d)
def compute_accuracy(predicted_labels):
    correctly_predicted = 0
    for i in range(iris_labels.size):
        if predicted_labels[i] == iris_labels[i]:
            correctly_predicted += 1

    accuracy = correctly_predicted / iris_labels.size
    return accuracy

# or
def compute_accuracy2(predicted_labels):
    return (np.array(predicted_labels) == iris_labels).size

print("The accuracy of my classification is {:.3f}".format(compute_accuracy(predicted_labels)))
print("The accuracy of my classification is {:.3f}".format(compute_accuracy2(predicted_labels)))


# f)
predicted_labels = []
for row in iris_values:

    label = nn_classify(row)
    predicted_labels.append(label)

print("The accuracy of neural network classification is {:.3f}".format(compute_accuracy2(predicted_labels)))