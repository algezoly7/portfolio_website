document.addEventListener("DOMContentLoaded", function () {
  const ones = document.querySelectorAll(".fade-in");
  const ugly3_id = document.getElementById("ugly3_id");
  document.getElementById("ugly2_id").style.visibility = "hidden";
  ///////////////////////////////////////
  //mario animation
  animate(ugly3_id);
  ///////////////////////////////////////
  //to make the pipe disappear
  var count = 0;
  var btn = document.getElementById("btn");
  btn.addEventListener("click", function () {
    if (count % 2 === 0) {
      document.getElementById("ugly2_id").style.visibility = "hidden";
      document.getElementById("ugly2_id_2").style.visibility = "hidden";
    } else {
      document.getElementById("ugly2_id_2").style.visibility = "visible";
    }
    count = count + 1;
  });
  /////////////////////////////////////////
  //for the coinsound
  document.querySelectorAll(".song").forEach((item) => {
    item.addEventListener("click", (event) => {
      var audio = document.getElementById("audio");
      audio.play();
    });
  });
  ////////////////////////////////////////
  //for the jump sound
  document.querySelectorAll(".song2").forEach((item) => {
    item.addEventListener("click", (event) => {
      var audio = document.getElementById("audio3");
      audio.play();
    });
  });
  //////////////////////////////////////
  //for stage clear sound
  var audio4 = document.getElementById("audio4");
  document
    .getElementById("submint_btn")
    .addEventListener("click", audio4.play());
  //on scroll animation
  const options = {
    threshold: 0.8,
    rootMargin: "0px 0px 0px 0px",
  };

  const observer = new IntersectionObserver(function (entries, observer) {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) {
        return;
      }
      console.log(entry);
      entry.target.classList.add("appear");
      observer.unobserve(entry.target);
    });
  }, options);
  ones.forEach((one) => {
    observer.observe(one);
  });
  //////////////////////////////////////////////////////////////////////////////
});

function animate(element) {
  let elementWidth = element.offsetWidth;
  let parentWidth = element.parentElement.offsetWidth;
  let flag = 0;

  setInterval(() => {
    flag = flag + 5;
    element.style.marginLeft = flag + "px";
    if (element.parentElement.offsetWidth - element.offsetLeft < 45) {
      document.getElementById("ugly3_id").remove();
      document.getElementById("ugly2_id").style.visibility = "visible";
      setTimeout(function () {
        console.log("hello");
        var audio2 = document.getElementById("audio2");
        document.onclick = function () {
          audio2.play();
        };
      }, 1000);

      setTimeout(function () {
        document.getElementById("ugly2_id").style.visibility = "hidden";
      }, 2000);
    }
  }, 10);
}
