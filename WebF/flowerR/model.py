# import pyodbc


# class Flowers:
#     con = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-CDPM50KT;Database=FlowerRecognition;UID=sa;PWD=sa2019')

#     def __init__(self, flowerID, flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDD, flowerNoiss):
#         self.flowerID = flowerID
#         self.flowerTen = flowerTen
#         self.flowerTenKH = flowerTenKH
#         self.flowerGioi = flowerGioi
#         self.flowerBo = flowerBo
#         self.flowerHo = flowerHo
#         self.flowerNganh = flowerNganh
#         self.flowerLop = flowerLop
#         self.flowerMota = flowerMota
#         self.flowerDD = flowerDD
#         self.flowerNoiss = flowerNoiss

#     @classmethod
#     def getAllFlowers(cls):
#         flowerData = []
#         cursor = Flowers.con.cursor()
#         cursor.execute("SELECT * FROM [dbo].[Flower]")
#         for row in cursor.fetchall():
#             flower = {}
#             flower['flowerID'] = row[0]
#             flower['flowerTen'] = row[1]
#             flower['flowerTenKH'] = row[2]
#             flower['flowerGioi'] = row[3]
#             flower['flowerBo'] = row[4]
#             flower['flowerHo'] = row[5]
#             flower['flowerNganh'] = row[6]
#             flower['flowerLop'] = row[7]
#             flower['flowerMota'] = row[8]
#             flower['flowerDD'] = row[9]
#             flower['flowerNoiss'] = row[10]
#             flowerData.append(flower)

#         return flowerData

#     @classmethod
#     def insertAFlower(cls, flowerID, flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDD, flowerNoiss):
#         cursor = Flowers.con.cursor()
#         cursor.execute(
#             f"INSERT INTO Flower VALUES ({flowerID} ,N'{flowerTen}','{flowerTenKH}','{flowerGioi}','{flowerBo}','{flowerHo}','{flowerNganh}','{flowerLop}',N'{flowerMota}',N'{flowerDD}',N'{flowerNoiss}')")
#         Flowers.con.commit()

#     @classmethod
#     def updateAFlower(cls, flowerID, flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDD, flowerNoiss):
#         cursor = Flowers.con.cursor()
#         cursor.execute(
#             f"UPDATE [dbo].[Flower] SET [flowerTen]=N'{flowerTen}',[flowerTenKH]='{flowerTenKH}',[flowerGioi]='{flowerGioi}',[flowerBo]='{flowerBo}',[flowerHo]='{flowerHo}',[flowerNganh]='{flowerNganh}',[flowerLop]='{flowerLop}',[flowerMota]=N'{flowerMota}',[flowerDD]=N'{flowerDD}',[flowerNoiss] =N'{flowerNoiss}' WHERE flowerID = {flowerID}")
#         Flowers.con.commit()

#     @classmethod
#     def deleteAFlower(cls, flowerID):
#         cursor = Flowers.con.cursor()
#         cursor.execute(
#             f"DELETE FROM [dbo].[Flower]  WHERE flowerID = {flowerID}")
#         Flowers.con.commit()


from .extensions import db

class Flowers(db.Model):
    __tablename__ = 'Flowers'
    flowerID = db.Column(db.Integer, primary_key = True)
    flowerTen = db.Column(db.UnicodeText, nullable = False)
    flowerTenKH = db.Column(db.String(50))
    flowerGioi = db.Column(db.String(50))
    flowerBo = db.Column(db.String(50))
    flowerHo = db.Column(db.String(50))
    flowerNganh = db.Column(db.String(50))
    flowerLop = db.Column(db.String(50))
    flowerMota = db.Column(db.UnicodeText)
    flowerDacdiem = db.Column(db.UnicodeText)
    flowerNoipb = db.Column(db.UnicodeText)


    def __init__(self, flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDD, flowerNoiss):
        self.flowerTen = flowerTen
        self.flowerTenKH = flowerTenKH
        self.flowerGioi = flowerGioi
        self.flowerBo = flowerBo
        self.flowerHo = flowerHo
        self.flowerNganh = flowerNganh
        self.flowerLop = flowerLop
        self.flowerMota = flowerMota
        self.flowerDacdiem = flowerDD
        self.flowerNoipb = flowerNoiss