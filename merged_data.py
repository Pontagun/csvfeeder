from os import listdir
import mysql.connector
import csv

if __name__ == "__main__":

    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Dsp123admin"
    )

    path = r"C:\Users\psonc001\PycharmProjects\csvfeeder\Data30Subjects\Raw1Recordings"
    onlyfilestxt = [f for f in listdir(path) if f.endswith("1.txt")]

    for f_name in onlyfilestxt:
        f_name = f_name
        filename = f_name[0:6]

        sql = "select * FROM dsp_gmv_rawdata.gmv0_rawdata v0 left join dsp_gmv_rawdata.gmv1_rawdata v1 on v0.Time = v1.Time and substring(v0.f_name, 1, 6) = substring(v1.f_name, 1, 6) " \
              "where v0.f_name like '%{}%' order by v0.IOID".format(filename)
        conn = mydb.cursor()

        conn.execute(sql)

        result = conn.fetchall()
        with open(filename+'.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for x in result:
                writer.writerow(x)
            # print(type(x))
        f.close()
