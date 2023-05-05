// const tx = document.getElementsByTagName("textarea");
// for (let i = 0; i < tx.length; i++) {
//     tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
//     tx[i].addEventListener("input", OnInput, false);
// }

// function OnInput() {
//     this.style.height = 0;
//     this.style.height = (this.scrollHeight) + "px";
//     var pr = this.parentNode.getElementsByTagName('label');
//     pr[0].style.setProperty('transform', `translateY(-${this.scrollHeight - 15}px)`);
// }

// const form = document.getElementById('flower-form');
// const flowerTenInput = document.getElementById('flowerTen');
// const flowerTenKHInput = document.getElementById('flowerTenKH');
// const flowerGioiInput = document.getElementById('flowerGioi');
// const flowerBoInput = document.getElementById('flowerBo');
// const flowerHoInput = document.getElementById('flowerHo');
// const flowerNganhInput = document.getElementById('flowerNganh');
// const flowerLopInput = document.getElementById('flowerLop');
// const flowerMotaInput = document.getElementById('flowerMota');
// const flowerDacdiemInput = document.getElementById('flowerDacdiem');
// const flowerNoipbInput = document.getElementById('flowerNoipb');

// Swal.fire({
//     title: 'Thành công!',
//     text: `Dữ liệu của đã được thêm vào cơ sở dữ liệu`,
//     icon: 'success',
//     iconColor: '#2B884E'}
// )

// function resetForm(){
//     const searchParams = new URLSearchParams(window.location.search);
//     const flowerID = searchParams.get("flowerID");
//     if (flowerID){
//         console.log(flowerID)
//     } else {
//         Swal.fire({
//             title: 'Lỗi!',
//             text: `Đã có lỗi phát sinh trong quá trình xữ lý`,
//             icon: 'error',
//             iconColor: '#AC2626'}
//         )
//     }
// }

// resetForm()