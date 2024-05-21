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
      responsive: [
        {
            breakpoint: 993,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1
            }
        },
        {
          breakpoint: 768,
          settings: {
              slidesToShow: 2,
              slidesToScroll: 1
          }
      },
      {
        breakpoint: 576,
        settings: {
            slidesToShow: 1,
            slidesToScroll: 1
        }
    }
      ],    
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

$('.header__burger-btn').on('click', function(e) {
  $(this).toggleClass('burger-active');
  $('.header__nav').toggleClass('nav-active');
});

const passwordInput = document.getElementById('id_password1');
const showPasswordButton = document.getElementById('showPasswordButton');
const eyeIcon = document.getElementById('eyeIcon1');

showPasswordButton.addEventListener('click', function() {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        eyeIcon.innerHTML = '<path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z"/>';
    } else {
        passwordInput.type = 'password';
        eyeIcon.innerHTML = '<path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/>';
    }
});

const passInput = document.getElementById('id_password2');
const showPassButton = document.getElementById('showPasswordButton1');
const eyesIcon = document.getElementById('eyeIcon2');

showPassButton.addEventListener('click', function() {
    if (passInput.type === 'password') {
        passInput.type = 'text';
        eyesIcon.innerHTML = '<path d="m644-428-58-58q9-47-27-88t-93-32l-58-58q17-8 34.5-12t37.5-4q75 0 127.5 52.5T660-500q0 20-4 37.5T644-428Zm128 126-58-56q38-29 67.5-63.5T832-500q-50-101-143.5-160.5T480-720q-29 0-57 4t-55 12l-62-62q41-17 84-25.5t90-8.5q151 0 269 83.5T920-500q-23 59-60.5 109.5T772-302Zm20 246L624-222q-35 11-70.5 16.5T480-200q-151 0-269-83.5T40-500q21-53 53-98.5t73-81.5L56-792l56-56 736 736-56 56ZM222-624q-29 26-53 57t-41 67q50 101 143.5 160.5T480-280q20 0 39-2.5t39-5.5l-36-38q-11 3-21 4.5t-21 1.5q-75 0-127.5-52.5T300-500q0-11 1.5-21t4.5-21l-84-82Zm319 93Zm-151 75Z"/>';
    } else {
        passInput.type = 'password';
        eyesIcon.innerHTML = '<path d="M480-320q75 0 127.5-52.5T660-500q0-75-52.5-127.5T480-680q-75 0-127.5 52.5T300-500q0 75 52.5 127.5T480-320Zm0-72q-45 0-76.5-31.5T372-500q0-45 31.5-76.5T480-608q45 0 76.5 31.5T588-500q0 45-31.5 76.5T480-392Zm0 192q-146 0-266-81.5T40-500q54-137 174-218.5T480-800q146 0 266 81.5T920-500q-54 137-174 218.5T480-200Zm0-300Zm0 220q113 0 207.5-59.5T832-500q-50-101-144.5-160.5T480-720q-113 0-207.5 59.5T128-500q50 101 144.5 160.5T480-280Z"/>';
    }
});