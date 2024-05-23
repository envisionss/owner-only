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
    background-color: rgb(25, 25, 25);
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
    z-index: 0; /* Ensure snowflakes are behind the boxes */
  }
  .box {
    position: absolute;
    width: 300px;
    height: 400px;
    border: 2px solid rgb(70, 70, 70);
    background-color: rgb(24, 20, 20);
    z-index: 2;
    padding: 10px;
  }
  .textbox-container {
    position: fixed;
    top: 10px;
    right: 300px;
    width: 600px;
    height: 400px;
    z-index: 2; /* Ensure the text is above the blur */
  }
  .textbox {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgb(25, 25, 25);
    color: white;
    border: 2px solid rgb(12, 12, 12);
    resize: none;
    padding: 10px;
    filter: blur(10px); /* Add blur effect */
    pointer-events: none; /* Prevent clicking on the blurred textbox */
    overflow: hidden; /* Ensure the text stays within the blurred textbox */
  }
  .coming-soon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: rgba(255, 255, 255, 0.8); /* Semi-transparent white */
    font-size: 24px;
    font-weight: bold;
    z-index: 3; /* Ensure the text is above the blur */
  }
  .checkbox-group {
    display: flex;
    flex-direction: column;
  }
  .checkbox {
    display: flex;
    align-items: center;
    margin-bottom: 5px;
  }
  .checkbox input[type="checkbox"] {
    margin-right: 5px;
  }
  .checkbox-label {
    color: rgb(99, 99, 99);
  }
  .checkbox input[type="checkbox"]:checked + .checkbox-label::before {
    background-color: rgb(255, 255, 255);
  }
  .checkbox input[type="checkbox"] {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 16px;
    height: 16px;
    border: 2px solid rgb(3, 0, 5);
    border-radius: 3px;
    background-color: transparent;
  }
  .checkbox input[type="checkbox"]:checked {
    background-color: rgb(12, 12, 12);
  }
  .box1 {
    top: 10px;
    left: 10px;
  }
  .box2 {
    top: 10px;
    left: 340px; /* Adjusted the left position to create space between the boxes */
  }
  .dropdown {
    position: relative;
    display: inline-block;
    margin-bottom: 20px;
  }
  .dropdown-btn {
    background-color: rgb(0, 0, 0);
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    cursor: pointer;
  }
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: rgb(20, 20, 20);
    min-width: 160px;
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    z-index: 1;
  }
  .dropdown-content a {
    color: white;
    padding: 12px 16px;
    text-decoration: none;
    display: block;
  }
  .dropdown-content a:hover {
    background-color: rgb(30, 30, 30);
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
  .dropdown-btn:hover {
    background-color: rgb(30, 30, 30);
  }
  .slidebar-container {
    margin-top: 20px;
  }
  .slidebar-label {
    color: rgb(99, 99, 99);
    margin-bottom: 5px;
  }
  .slidebar {
    width: 100%;
    /* Changed the fill color */
    background: rgb(17, 17, 17);
  }
  .slidebar-value {
    color: white;
    text-align: center;
  }
  @keyframes snowfall {
    0% {
      transform: translateY(-10vh);
    }
    100% {
      transform: translateY(110vh);
    }
  }
  .red-dot {
    position: absolute;
    bottom: 10px;
    left: 10px;
    width: 20px; /* Increased the size of the dot */
    height: 20px;
    background-color: red;
    border-radius: 50%;
    z-index: 3; /* Ensure the dot is above everything */
  }
  .green-dot {
    background-color: green !important;
  }
  #checkerButton {
    background-color: rgb(16, 16, 16);
    color: white;
    padding: 12px 24px;
    font-size: 16px;
    border: none;
    cursor: pointer;
    border-radius: 8px;
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
  }
</style>
</head>
<body>
<div class="snow-container">
  <!-- Create snowflakes dynamically using JavaScript -->
</div>
<div class="box box1">
  <div class="checkbox-group">
    <div class="checkbox">
      <input type="checkbox" id="checkbox1">
      <label for="checkbox1" class="checkbox-label">Enabled</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox2">
      <label for="checkbox2" class="checkbox-label">Prediction</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox3">
      <label for="checkbox3" class="checkbox-label">Sticky Aim</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox4">
      <label for="checkbox4" class="checkbox-label">Shake</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox5">
      <label for="checkbox5" class="checkbox-label">Disable Outside FOV</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox6">
      <label for="checkbox6" class="checkbox-label">KnockCheck</label>
    </div>
    <div class="checkbox">
      <input type="checkbox" id="checkbox7">
      <label for="checkbox7" class="checkbox-label">TeamCheck</label>
    </div>
  </div>
</div>
<div class="box box2">
  <div class="textbox-container">
    <div class="textbox"></div>
    <div class="coming-soon">Coming Soon</div>
  </div>
  <div class="dropdown">
    <button class="dropdown-btn">Aimbot Type</button>
    <div class="dropdown-content">
      <a href="#" onclick="selectOption('Cam')">Cam - Aimbot Type</a>
      <a href="#" onclick="selectOption('Mouse')">Mouse - Aimbot Type</a>
    </div>
  </div>
  <div class="slidebar-container">
    <label for="smoothing" class="slidebar-label">Smoothing</label>
    <input type="range" min="0" max="100" value="50" class="slidebar" id="smoothing">
    <div class="slidebar-value">50%</div>
  </div>
</div>
<button id="checkerButton">Run Me For It To Work</button> <!-- Moved Checker button -->
<div class="red-dot" id="dot"></div>
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

  function selectOption(option) {
    const dropdownBtn = document.querySelector('.dropdown-btn');
    dropdownBtn.textContent = option;
  }

  // Function to download Python script
  function downloadChecker() {
    const url = 'https://cdn.discordapp.com/attachments/1238475731483361330/1243145244145618974/checker.py?ex=665068ba&is=664f173a&hm=54d21cec8cd49aaa72838d47921227abdbb9edc7f13c181658cdb01fbaf6ab7c&';
    const anchor = document.createElement('a');
    anchor.href = url;
    anchor.download = 'checker.py';
    anchor.click();

    // Simulate Python script execution
    setTimeout(() => {
      // Check if the Python script output contains the specified message
      const output = "Completed, You May Close This Now!";
      // Assuming you have a real Python script output here, for simulation purposes:
      if (Math.random() < 0.5) {
        console.log(output); // Log the output to simulate the script's behavior
        // Change dot color to green
        const dot = document.getElementById('dot');
        dot.classList.add('green-dot');
      }
    }, 2000); // Simulate a delay of 2 seconds before checking the output
  }

  // Event listener for the Checker button
  const checkerButton = document.getElementById('checkerButton');
  checkerButton.addEventListener('click', downloadChecker);

  // Event listener for the slidebar
  const slidebar = document.getElementById('smoothing');
  const slidebarValue = document.querySelector('.slidebar-value');
  slidebar.addEventListener('input', () => {
    slidebarValue.textContent = `${slidebar.value}%`;
  });
</script>
</body>
</html>
