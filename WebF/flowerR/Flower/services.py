from flowerR.extensions import ma, db
from flowerR.schemas import FlowerSchema
from flowerR.model import Flowers
from flask import jsonify, request
import traceback

fSchema = FlowerSchema
fsSchema = FlowerSchema(many=True)


def getAllFlowersService():
    data = Flowers.query.all()
    if data:
        return fsSchema.jsonify(data)
    else: return "No flowers has found!"


def postAFlowerService():
    flowerTen = request.json['flowerTen']
    flowerTenKH = request.json['flowerTenKH']
    flowerGioi = request.json['flowerGioi']
    flowerBo = request.json['flowerBo']
    flowerHo = request.json['flowerHo']
    flowerNganh = request.json['flowerNganh']
    flowerLop = request.json['flowerLop']
    flowerMota = request.json['flowerMota']
    flowerDacdiem = request.json['flowerDacdiem']
    flowerNoipb = request.json['flowerNoipb']
    try:
        newFlower = Flowers(flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDacdiem, flowerNoipb)
        db.session.add(newFlower)
        db.session.commit()
        return "Successful adding"
    except:
        print(traceback.format_exc())
        return "Unsuccessful adding"

def updateAFlowerService(flowerID):
    flower = Flowers.query.get(flowerID)
    if not flower:
        return "Unsuccess"
    flower.flowerTen = request.json['flowerTen']
    flower.flowerTenKH = request.json['flowerTenKH']
    flower.flowerGioi = request.json['flowerGioi']
    flower.flowerBo = request.json['flowerBo']
    flower.flowerHo = request.json['flowerHo']
    flower.flowerNganh = request.json['flowerNganh']
    flower.flowerLop = request.json['flowerLop']
    flower.flowerMota = request.json['flowerMota']
    flower.flowerDD = request.json['flowerDD']
    flower.flowerNoiss = request.json['flowerNoiss']
    db.session.commit()
    return "Successfully update"

def deleteAFlowerService(flowerID):
    flower = Flowers.query.get(flowerID)
    if flower:
        db.session.delete(flower)
        db.session.commit()
        return "Successfully delete"
    else: return "Unsuccessfully delete"
