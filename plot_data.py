from os import listdir
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    path = r"C:\Users\psonc001\PycharmProjects\csvfeeder\Data30Subjects\Raw1Recordings"
    onlyfilestxt = [f for f in listdir(path) if f.endswith("GMV0.txt")]


    for f_name in onlyfilestxt:
        orientation_q = []
        full_path = path + "\\" + f_name
        with open(full_path) as f:
            lines = f.readlines()

            for inx, line in enumerate(lines):
                line = line.split(',')
                orientation_q.append([line[12], line[13], line[14], line[15]])

        orientation_q = np.array(orientation_q)

        qx = [float(x) for x in orientation_q[:, 0]]
        qy = [float(y) for y in orientation_q[:, 1]]
        qz = [float(z) for z in orientation_q[:, 2]]
        qw = [float(w) for w in orientation_q[:, 3]]

        tdistort = int(len(qx)*0.6)

        plt.plot(qx[:tdistort])
        plt.plot(qy[:tdistort])
        plt.plot(qz[:tdistort])
        plt.plot(qw[:tdistort])
        plt.savefig('./plot_normal/{}.png'.format(f_name[0:6]))
        plt.close()

        plt.plot(qx[tdistort:])
        plt.plot(qy[tdistort:])
        plt.plot(qz[tdistort:])
        plt.plot(qw[tdistort:])
        plt.savefig('./plot_distroted/{}.png'.format(f_name[0:6]))
        plt.close()

        plt.plot(qx[:])
        plt.plot(qy[:])
        plt.plot(qz[:])
        plt.plot(qw[:])
        plt.savefig('./plot/{}.png'.format(f_name[0:6]))
        plt.close()
