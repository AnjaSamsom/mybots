import numpy
import matplotlib.pyplot

# A is the bipeds
# B is the quadrupeds
# the number after is the trial, a trial is using the same random placement of the two robts for fairness

def main():
    plot_all_best()

def plot_all_best():
    A_mins = [0,0,0,0,0,0,0,0,0,0]
    B_mins = [0,0,0,0,0,0,0,0,0,0]
    trials = [1,2,3,4,5,6,7,8,9,10]
    for i in range(1,11):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")

        i = int(i)

        A_mins [i-1] = A.min()
        B_mins [i-1] = B.min()

    matplotlib.pyplot.scatter(trials, A_mins, color="red", label = "two legged robots")
    matplotlib.pyplot.scatter(trials, B_mins, color="blue", label = "four legged robots")
    matplotlib.pyplot.legend(loc="upper left")

    matplotlib.pyplot.title("Best Fitness Achieved")
    matplotlib.pyplot.xlabel("Trial")
    matplotlib.pyplot.ylabel("Fitness Value")



    matplotlib.pyplot.show()




    print(A_mins)
    print(B_mins)

    i = int(i)

def plot_all_means():
    for i in range(1,11):
        i = str(i)
        A = numpy.load("matrixA" + i + ".npy")
        B = numpy.load("matrixB" + i + ".npy")
        A = numpy.mean(A, axis = 0)
        B = numpy.mean(B, axis = 0)

        if i == "1":
            matplotlib.pyplot.plot(A, color = "red", label = "two legged robots")
            matplotlib.pyplot.plot(B, color = "blue", label = "four legged robots")

        else:
            matplotlib.pyplot.plot(A, color = "red")
            matplotlib.pyplot.plot(B, color = "blue")
        print(i)


    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot All Means")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()
    i = int(i)


def plot_mean():
    A1 = numpy.load("matrixA1.npy")
    A2 = numpy.load("matrixA2.npy")
    A3 = numpy.load("matrixA3.npy")
    A4 = numpy.load("matrixA4.npy")
    A5 = numpy.load("matrixA5.npy")
    A6 = numpy.load("matrixA6.npy")
    A7 = numpy.load("matrixA7.npy")
    A8 = numpy.load("matrixA8.npy")
    A9 = numpy.load("matrixA9.npy")
    A10 = numpy.load("matrixA10.npy")
    
    A1 = numpy.mean(A1, axis = 0)
    A2 = numpy.mean(A2, axis = 0)
    A3 = numpy.mean(A3, axis = 0)
    A4 = numpy.mean(A4, axis = 0)
    A5 = numpy.mean(A5, axis = 0)
    A6 = numpy.mean(A6, axis = 0)
    A7 = numpy.mean(A7, axis = 0)
    A8 = numpy.mean(A8, axis = 0)
    A9 = numpy.mean(A9, axis = 0)
    A10 = numpy.mean(A10, axis = 0)


    A = numpy.mean(numpy.array([ A1, A2, A3, A4, A5, A6, A7, A8, A9, A10 ], dtype=object), axis=0)



    B1 = numpy.load("matrixB1.npy")
    B2 = numpy.load("matrixB2.npy")
    B3 = numpy.load("matrixB3.npy")
    B4 = numpy.load("matrixB4.npy")
    B5 = numpy.load("matrixB5.npy")
    B6 = numpy.load("matrixB6.npy")
    B7 = numpy.load("matrixB7.npy")
    B8 = numpy.load("matrixB8.npy")
    B9 = numpy.load("matrixB9.npy")
    B10 = numpy.load("matrixB10.npy")

    B1 = numpy.mean(B1, axis = 0)
    B2 = numpy.mean(B2, axis = 0)
    B3 = numpy.mean(B3, axis = 0)
    B4 = numpy.mean(B4, axis = 0)
    B5 = numpy.mean(B5, axis = 0)
    B6 = numpy.mean(B6, axis = 0)
    B7 = numpy.mean(B7, axis = 0)
    B8 = numpy.mean(B8, axis = 0)
    B9 = numpy.mean(B9, axis = 0)
    B10 = numpy.mean(B10, axis = 0)

    B = numpy.mean(numpy.array([ B1, B2, B3, B4, B5, B6, B7, B8, B9, B10 ], dtype=object), axis=0)

    sA = numpy.std(A)
    sB = numpy.std(B)

    matplotlib.pyplot.plot(A+sA, color = "hotpink", label = "two legged robots +-stdev")
    matplotlib.pyplot.plot(A, color = "red", label = "two legged robots")
    matplotlib.pyplot.plot(A-sA, color = "hotpink")
 
    matplotlib.pyplot.plot(B+sB, color = "cornflowerblue", label = "four legged robot +- stdev")    
    matplotlib.pyplot.plot(B, color = "blue", label = "four legged robots")
    matplotlib.pyplot.plot(B-sB, color = "cornflowerblue")



    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot Mean of all Trials")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


def plot_trial(i):
    i = str(i)
    two = numpy.load("matrixA" + i + ".npy")
    four = numpy.load("matrixB" + i + ".npy")

    two = numpy.mean(two, axis = 0)
    four = numpy.mean(four, axis = 0)

    s2 = numpy.std(two)
    s4 = numpy.std(four)



    matplotlib.pyplot.plot(two-s2, color = "hotpink", label = "two legged robots +-stdev")
    matplotlib.pyplot.plot(two, color = "red", label = "two legged robots")
    matplotlib.pyplot.plot(two+s2, color = "hotpink")

    matplotlib.pyplot.plot(four-s4, color = "cornflowerblue", label = "four legged robot +- stdev")
    matplotlib.pyplot.plot(four, color = "blue", label = "four legged robot")
    matplotlib.pyplot.plot(four+s4, color = "cornflowerblue")


    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot Trial " + i)
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()


main()
