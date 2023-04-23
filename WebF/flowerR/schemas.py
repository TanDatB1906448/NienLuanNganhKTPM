from .extensions import ma

class FlowerSchema(ma.Schema):
    class Meta:
        fields = ('flowerID', 'flowerTen', 'flowerTenKH', 'flowerGioi', 'flowerBo', 'flowerHo', 'flowerNganh', 'flowerLop', 'flowerMota', 'flowerDD', 'flowerNoiss')