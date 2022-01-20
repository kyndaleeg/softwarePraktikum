from server.bo.Spo import Spo
from server.db.Mapper import Mapper


class SpoMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, creationdate, name, title, start_semester, end_semester, studycourse from spo")
        tuples = cursor.fetchall()
        
        print(tuples)

        for (id, creationdate, name, title, start_semester, end_semester, studycourse_id) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse_id)
            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM spo WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, start_semester, end_semester, studycourse_id) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse_id)

            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * spo WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, start_semester, end_semester, studycourse) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse)
            result = spo
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_hash(self, hashcode):

        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * spo WHERE spo_hash={}".format(hashcode)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, start_semester, end_semester, studycourse_id) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semster)
            spo.set_studycourse(studycourse_id)
            result = spo
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_all_by_studycourse(self, studycourse):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM spo WHERE studycourse LIKE '{}' ORDER BY studycourse".format(studycourse)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, creationdate, name, title, start_semester, end_semester, studycourse) = tuples[0]
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse)
            result = spo
        except IndexError:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_latest_by_studycourse(self, studycourse_hash):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM spo WHERE studycourse_id = '{}' ORDER BY creationdate DESC LIMIT 1".format(studycourse_hash)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, start_semester, end_semester, studycourse) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse)

            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_startsemester_and_studycourse(self, studycourse_id):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM spo WHERE studycourse_id='{}' AND start_semester='{}'".format(studycourse_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, creationdate, name, title, start_semester, end_semester, studycourse) in tuples:
            spo = Spo()
            spo.set_id(id)
            spo.set_name(name)
            spo.set_title(title)
            spo.set_start_semester(start_semester)
            spo.set_end_semester(end_semester)
            spo.set_studycourse(studycourse_id)

            result.append(spo)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, spo: Spo):

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM spo")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:

                spo.set_id(maxid[0] + 1)
            else:

                spo.set_id(1)

        ss = spo.get_start_semester()
        es = spo.get_end_semester()
        sc = spo.get_studycourse()
        command = "INSERT INTO spo (id, creationdate, name, title, start_semester, end_semester, studycourse, spo_hash) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (spo.get_id(), spo.get_creationdate(), spo.get_name(), spo.get_title(), ss, es, sc, hash(spo.get_title()))
        print(data)
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return spo

    def update(self, spo):

        cursor = self._cnx.cursor()

        command = "UPDATE spo " + "SET name=%s, SET title=%s, SET start_semester=%s, SET end_semester=%s, SET studycourse_id=%s WHERE id=%s "
        data = (spo.get_name(), spo.get_title(), spo.get_start_semester(), spo.get_end_semester(), spo.get_studycourse(), spo.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, spo):

        cursor = self._cnx.cursor()

        command = "DELETE FROM spo WHERE id={}".format(spo.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
