const hamburger = document.querySelector('.header .nav-bar .nav-list .hamburger');
const mobile_menu = document.querySelector('.header .nav-bar .nav-list ul');
const menu_item = document.querySelectorAll('.header .nav-bar .nav-list ul li a');
const header = document.querySelector('.header.container');



hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('active');
    mobile_menu.classList.toggle('active');
});

// document.addEventListener('scroll', () => {
//     var scroll_position = window.scrollY;
//     if (scroll_position > 250) {
//         header.style.backgroundColor = '#29323c';
//     } else {
//         header.style.backgroundColor = 'transparent';
//     }
// });

menu_item.forEach((item) => {
    item.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        mobile_menu.classList.toggle('active');
    });
});

const getFlowerInfosAPI = "http://127.0.0.1:5000/getAllFlowers"

flowers = []
fetch(getFlowerInfosAPI)
    .then(response => response.json())
    .then(function (result) {
        for (var i = 0; i < result.length; i++) {
            flowers.push(result[i])
        }
        console.log(flowers)
        var servicebottom = document.querySelector('.service-bottom')
        var htmls = flowers.map((flower) => {
            return `
            <div class="service-item">
                <h2>${flower.flowerTen}</h2>
                <p>Tên khoa học: ${flower.flowerTenKH}</p>
                <p>Giới: ${flower.flowerGioi}</p>
                <p>Nghành: ${flower.flowerNganh}</p>
                <p>Lớp: ${flower.flowerLop}</p>
                <p>Bộ: ${flower.flowerBo}</p>
                <p>Họ: ${flower.flowerHo}</p>
                <a href="#" class = 'cta'>Xem thêm</a>
            </div>
            `
        })
        servicebottom.innerHTML = htmls.join('');
    })
    .catch(error => console.log('error', error));