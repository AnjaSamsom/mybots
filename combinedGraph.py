import numpy
import matplotlib.pyplot

# A is the bipeds
# B is the quadrupeds
# the number after is the trial, a trial is using the same random placement of the two robts for fairness

def main():
    #plot_mean(50)
    #plot_trial(10)
    #plot_all_best(50)
    plot_all_means(50)


def plot_all_best(num_trials):
    A_mins = numpy.zeros(num_trials)
    B_mins = numpy.zeros(num_trials)
    trials = []
    for i in range(num_trials):
        trials.append(i+1)

    for i in range(1,num_trials+1):
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


def plot_all_means(num_trials):
    for i in range(1,num_trials+1):
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


    matplotlib.pyplot.legend(loc="upper left")
    matplotlib.pyplot.title("Plot All Means")
    matplotlib.pyplot.xlabel("Generation")
    matplotlib.pyplot.ylabel("Fitness Value")

    matplotlib.pyplot.show()
    i = int(i)


def plot_mean(num_trials):
    A = []
    B = []

    for i in range(num_trials):
        Ai = numpy.load("matrixA" + str(num_trials) + ".npy")
        Ai = numpy.mean(Ai, axis = 0)
        A.append(Ai)

        Bi = numpy.load("matrixB" + str(num_trials) + ".npy")
        Bi = numpy.mean(Bi, axis = 0)
        B.append(Bi)

    A = numpy.mean(A, axis=0)
    B = numpy.mean(B, axis=0)

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
