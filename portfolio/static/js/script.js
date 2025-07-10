document.addEventListener("DOMContentLoaded", function() {
  const images = [
    { src: "static/images/web.jpg", caption: "Web Developer" },
    { src: "static/images/python.jpg", caption: "Python Programmer" },
    { src: "static/images/data.jpg", caption: "Data Enthusiast" },
    { src: "static/images/java.jpg", caption: "Java Developer" }
  ];

  const heroImage = document.getElementById("hero-image");
  const heroCaption = document.getElementById("hero-caption");
  let index = 0;

  function showSlide() {
    heroImage.src = `/static/${images[index].src}`;
    heroCaption.textContent = images[index].caption;
    index = (index + 1) % images.length;
  }

  showSlide();
  setInterval(showSlide, 3000); // 3 seconds
});
