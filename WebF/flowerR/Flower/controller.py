from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from .services import getAllFlowersService, postAFlowerService, updateAFlowerService, deleteAFlowerService

Flowers = Blueprint("Flowers", __name__)

@Flowers.route("/getAllFlowers", methods = ['GET'])
def getAllFlowers():
    return getAllFlowersService()

@Flowers.route("/postAFlower", methods = ['POST'])
def postAFlower():
    return postAFlowerService()

@Flowers.route("/updateAFlower/<flowerID>", methods = ['PUT'])
def updateAFlower(flowerID):
    return updateAFlowerService(flowerID)

@Flowers.route("/deleteAFlower/<flowerID>", methods = ['DELETE'])
def deleteAFlower(flowerID):
    return deleteAFlowerService(flowerID)