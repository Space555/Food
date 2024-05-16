$(document).ready(function(){
    $('.slider__main-wrapper').slick({
      arrows: false,
      adaptiveHeight: false,
      slidesToShow: 5, //количество отображаемых элементов
      //slidesToScroll: 3,
      speed: 1000,
      infinite: true, //бесконечный слайдер
      autoplay: true, // 
      autoplaySpeed: 2000,
      pauseOnFocus: true,
      pauseOnHover: true,
      touchThreshold: 30,
      touchMove: true,
      waitForAnimate: false,
      centerMode: false,
      variableWidth: false,
    });
    $('.slider__main-wrapper').slick('setPosition');
  });


// document.querySelector('.header__profile-btn').addEventListener('click', function() {
//    document.querySelector('.header__profile-dp').style.display = 'block';
// });

$("#btn-dpw").click(function(e) {
  e.stopPropagation();
  $("#block-dpw").toggleClass("down");
});

$("#btn-dpw").click(function() {
  $("block-dpw").removeClass("down");
  // $("#cats_list").removeClass("act");
});

// document.querySelector('.header__profile-btn').addEventListener(
//   'click', function() {
//   var dropdownContent = document.querySelector('.header__profile-dp');
//   if (dropdownContent.style.display === 'block') {
//     dropdownContent.style.display = 'none';
//   } else {
//     dropdownContent.style.display = 'block';
//   }
// });

$("#comment-btn").click(function(e) {
  e.stopPropagation();
  $("#comment-content").toggleClass("act");
});

$("#comment-btn").click(function() {
  $("comment-content").removeClass("act");
  // $("#cats_list").removeClass("act");
});

//select
// const element = document.querySelector('.add__select')

// const choices = new Choices(element, {
//   searchEnabled: false,
//   itemSelectText: '',
// });


$("#open").click(function(e) {
  $("#len").toggleClass("close");
  $("#all").toggleClass("open");
});

$("#close").click(function() {
  $("#len").removeClass("close");
  $("#all").removeClass("open");
});