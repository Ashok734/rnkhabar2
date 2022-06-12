document.addEventListener("DOMContentLoaded", function () {

  window.addEventListener('scroll', function () {

    if (window.scrollY > 200) {
      document.getElementById('navbar_top').classList.add('fixed-top');
      // add padding top to show content behind navbar
      navbar_height = document.querySelector('.navbar').offsetHeight;
      document.body.style.paddingTop = navbar_height + 'px';
    } else {
      document.getElementById('navbar_top').classList.remove('fixed-top');
      // remove padding top from body
      document.body.style.paddingTop = '0';
    }
  });
});

// mobile navigation
document.addEventListener("DOMContentLoaded", function () {

  window.addEventListener('scroll', function () {

    if (window.scrollY > 200) {
      document.getElementById('mobile-navigation').classList.add('fixed-top');
      // add padding top to show content behind navbar
      navbar_height = document.querySelector('.navbar').offsetHeight;
      document.body.style.paddingTop = navbar_height + 'px';
    } else {
      document.getElementById('mobile-navigation').classList.remove('fixed-top');
      // remove padding top from body
      document.body.style.paddingTop = '0';
    }
  });
});

$('.newss').owlCarousel({
  loop: true,
  margin: 10,
  dots: false,
  nav: true,
  mouseDrag: false,
  autoplay: true,
  animateOut: 'fadeOut',
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 1
    },
    1000: {
      items: 1
    }
  }
});
$('.news').owlCarousel({
  loop: true,
  margin: 10,
  nav: false,
  dots: false,
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 1
    },
    1000: {
      items: 1
    }
  }
})
