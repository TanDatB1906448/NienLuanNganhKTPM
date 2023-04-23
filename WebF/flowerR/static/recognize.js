const inputImage = document.querySelector('#img');
const uploadedImage = document.querySelector('.uploaded-image');
const flowerResultInfo = document.querySelector('.col-right');
var formData = new FormData();

const getResultOfRecAPI = "http://127.0.0.1:5000/getResult"

inputImage.addEventListener('change', (event) => {
    formData = new FormData();
    formData.append('file', inputImage.files[0]);
    uploadedImage.style.backgroundImage = "url(" + URL.createObjectURL(event.target.files[0]) + ")";
    getResult()
});

function getResult() {
    var options = {
        method: 'POST',
        body: formData,
    };
    fetch(getResultOfRecAPI, options)
        .then(response => response.json())
        .then((data) => {
            return flowers.filter((f) => f.flowerID == data.flowerID + 1)[0]
        })
        .then((flower) => {
            console.log("AA")
            console.log(flower)
            var FIHTML = `
            <h1 class=\"section-title\">${flower.flowerTen}</h1>
            <h2>${flower.flowerTenKH}</h2>
            <p>${flower.flowerMota}</p>
            <a href=\#\" class=\"cta\">Xem thêm</a>`;
            flowerResultInfo.innerHTML = FIHTML
        })
}