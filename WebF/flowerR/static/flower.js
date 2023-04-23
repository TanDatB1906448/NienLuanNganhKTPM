const getFlowerInfoAPI = "http://127.0.0.1:5000/getAllFlowers"

flowers = []
fetch(getFlowerInfoAPI)
    .then(response => response.json())
    .then(function (result) {
        for (var i = 0; i < result.length; i++) {
            flowers.push(result[i])
        }
    })
    .catch(error => console.log('error', error));

console.log(flowers)

function renderFlower(flowers) {
    var servicebottom = document.querySelector('.service-bottom')
    var htmls = flowers.map((flower) => {
        return `
        <div class="service-item">
            <h2>${flower.flowerTen}</h2>
            <p></p>
            <p class="cta">Xem Thêm</p>
        </div>
        `
    })
}