document
  .getElementById("registrationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;
    let error = document.getElementById("error");
    if (username.length < 2) {
      error.textContent = "Имя пользователя должно быть минимум из 2 букв";
      return;
    }
    if (password !== confirmPassword) {
      error.textContent = "Пароли не совпадают";
      return;
    }
    error.textContent = "";
    alert("Регистрация успешна");
  });
