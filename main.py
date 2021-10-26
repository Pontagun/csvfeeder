from os import listdir
import mysql.connector

if __name__ == "__main__":

    mydb = mysql.connector.connect(
        host="34.134.233.161",
        user="root",
        password="DSP123admin"
    )

    conn = mydb.cursor()

    # path = r"C:\Users\ponta\Downloads\Data30Subjects-20211024T204355Z-001\Data30Subjects\Raw1Marks"
    # onlyfilestxt = [f for f in listdir(path) if f.endswith("txt")]
    path = r"C:\Users\ponta\Downloads\Data30Subjects-20211024T204355Z-001\Data30Subjects\Raw1Recordings"
    onlyfilestxt = [f for f in listdir(path) if f.endswith("0.txt")]


    for f_name in onlyfilestxt:
        full_path = path + "\\" + f_name
        with open(full_path) as f:
            lines = f.readlines()

            for inx, line in enumerate(lines):
                line = line.split(',')
                sql = "INSERT INTO dsplab.gmvd VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
                sql_1 = ",'{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(line[10], line[11], line[12], line[13], line[14], line[15], f_name)

                sql = sql + sql_1
                conn.execute(sql)

                if inx % 1000 == 0:
                    mydb.commit()
            # for line in lines:
            #     line = line.split(',')
            #     sql = "INSERT INTO dsplab.gmv_marks VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            #     sql_1 = ",'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17], line[18], line[19])
            #     sql_2 = ",'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(line[20], line[21], line[22], line[23], line[24], line[25], line[26], line[27], line[28], line[29])
            #     sql_3 = ",'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'".format(line[30], line[31], line[32], line[33], line[34], line[35], line[36], line[37], line[38], line[39])
            #     sql_4 = ",'{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(line[40], line[41], line[42], line[43], line[44], line[45], line[46], f_name)
            #
            #     sql = sql + sql_1 + sql_2 + sql_3 + sql_4
            #     conn.execute(sql)
            #
            #     mydb.commit()
