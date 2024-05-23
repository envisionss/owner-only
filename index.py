<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EnvisionV1</title>
<style>
  body {
    margin: 0;
    padding: 0;
    background-color: rgb(26, 23, 23);
    font-family: Arial, sans-serif;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  .snow-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
  }
  .snowflake {
    position: absolute;
    border-radius: 50%;
    width: 5px;
    height: 5px;
    animation: snowfall linear infinite;
  }
  @keyframes snowfall {
    0% {
      transform: translateY(-10vh);
    }
    100% {
      transform: translateY(110vh);
    }
  }
  .login-container {
    background-color: transparent;
    border: 2px solid purple;
    padding: 90px; /* Increased padding for a larger container */
    border-radius: 10px;
    text-align: center;
    animation: typing 2s infinite;
    z-index: 2;
    position: relative;
  }
  @keyframes typing {
    0% {
      border-color: black
    }
    50% {
      border-color: black
    }
    100% {
        border-color: black
    }
  }
  .login-button {
    width: 100%;
    padding: 10px;
    background-color: rgb(12, 12, 12);
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  .login-button:hover {
    background-color: rgb(22, 22, 22);
  }
</style>
</head>
<body>
<div class="snow-container">
  <!-- Create snowflakes dynamically using JavaScript -->
</div>
<div class="login-container">
  <button class="login-button" onclick="checkLicense()">Continue</button>
</div>
<script>
  const snowContainer = document.querySelector('.snow-container');
  const numberOfSnowflakes = 50;
  for (let i = 0; i < numberOfSnowflakes; i++) {
    const snowflake = document.createElement('div');
    snowflake.classList.add('snowflake');
    snowflake.style.left = `${Math.random() * 100}%`;
    snowflake.style.animationDuration = `${Math.random() * 3 + 2}s`;
    snowflake.style.animationDelay = `${Math.random() * -5}s`;
    snowContainer.appendChild(snowflake);
  }
  function changeSnowColor(color) {
    const snowflakes = document.querySelectorAll('.snowflake');
    snowflakes.forEach(snowflake => {
      snowflake.style.backgroundColor = color;
    });
  }
  changeSnowColor('black');
  function checkLicense() {
    window.location.href = 'main.html';
  }
</script>
</body>
</html>
