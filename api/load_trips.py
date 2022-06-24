import csv
import MySQLdb


class load_trips_class():

    def load_trips_prc(self):

        mydb = MySQLdb.connect(host="127.0.0.1", user="root", password='', database='jobsity')

        with open("C:/trips.csv") as csv_file:
            csvfile = csv.reader(csv_file, delimiter=',')
            all_value = []
            for row in csvfile:
                value = (row[0], row[1], row[2], row[3], row[4])
                all_value.append(value)

        query = "insert into `api_trips`(`region`, `origin_coord`, `destination_coord`, `datetime`, `datasource`) values (%s, %s, %s, %s, %s) "

        mycursor = mydb.cursor()
        mycursor.executemany(query, all_value)
        mydb.commit()
