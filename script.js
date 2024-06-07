//Задание 1 которое 2
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(7));
console.log(factorial(0));
console.log(factorial(1));
console.log(factorial(8));
//Задание 2 которое 3
function geolocation() {
  let intervalID = setInterval(function () {
    let result = confirm("Включите геолокацию");
    if (result) {
      clearInterval(intervalID);
    }
  }, 1000);
}
geolocation();
//Второй способ
function geolocation2() {
  function ask() {
    let result = confirm("Включите геолокацию");
    if (result) {
      return;
    }
    setTimeout(ask, 1000);
  }
  ask();
}
geolocation2();
