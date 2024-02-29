document.addEventListener('DOMContentLoaded', function() {
    var countResultPY = document.getElementById('countResultPy');
    var countResultJS = document.getElementById('countResultJs');
    const count = countResultPY.innerHTML;

    // // Define the interval time and calculate the increment value
    // var increment = Math.ceil(count / (3000 / intervalTime)); // Counting duration: 3000ms (3 seconds)

    var currentCount = 0;
    var interval = setInterval(function() {
      currentCount += 1;

      // Ensure the final count is not exceeded
      if (currentCount >= count) {
        currentCount = count;
        clearInterval(interval);
      }

      countResultJS.innerText = currentCount;
    }, 200);
  });
