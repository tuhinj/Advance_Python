(function ($) {
    "use strict";

    /*-------------------------------------
    Category Switcher 
    -------------------------------------*/

    $('.product-view-trigger').on('click', function (e) {
        var self = $(this),
            data = self.attr("data-type"),
            target = $("#category-view");
        self.parents('.layout-switcher').find('li.active').removeClass('active');
        self.parent('li').addClass('active');
        target.children('.row').find('>div').animate({
            opacity: 0,
        }, 200, function () {
            if (data === "category-grid-layout1") {
                target.removeClass('category-list-layout1');
                target.addClass('category-grid-layout1');
            } else if (data === "category-list-layout1") {
                target.removeClass('category-grid-layout1');
                target.addClass('category-list-layout1');
            } else if (data === "category-grid-layout2") {
                target.removeClass('category-list-layout2');
                target.addClass('category-grid-layout2');
            } else if (data === "category-list-layout2") {
                target.removeClass('category-grid-layout2');
                target.addClass('category-list-layout2');
            } else if (data === "category-grid-layout3") {
                target.removeClass('category-list-layout3');
                target.addClass('category-grid-layout3');
            } else if (data === "category-list-layout3") {
                target.removeClass('category-grid-layout3');
                target.addClass('category-list-layout3');
            }
            target.children('.row').find('>div').animate({
                opacity: 1,
            }, 100);
        });
        e.preventDefault();
        return false;
    });
    headerNsliderResize();
    var priceSlider = document.getElementById('price-range-filter');
    if (priceSlider) {
        noUiSlider.create(priceSlider, {
            start: [20, 80],
            connect: true,
            /*tooltips: true,*/
            range: {
                'min': 0,
                'max': 100
            },
            format: wNumb({
                decimals: 0
            }),
        });
        var marginMin = document.getElementById('price-range-min'),
            marginMax = document.getElementById('price-range-max');
        priceSlider.noUiSlider.on('update', function (values, handle) {
            if (handle) {
                marginMax.innerHTML = "$" + values[handle];
            } else {
                marginMin.innerHTML = "$" + values[handle];
            }
        });
    }

    /*-------------------------------------
    // Tooltips
    -------------------------------------*/
    $(document).on('mouseover', '.trending-sign', function () {
        var self = $(this),
            tips = self.attr('data-tips');
        $tooltip = '<div class="fox-tooltip">' + '<div class="fox-tooltip-content">' + tips + '</div>' + '<div class="fox-tooltip-bottom"></div>' + '</div>';
        $('body').append($tooltip);
        var $tooltip = $('body > .fox-tooltip');
        var tHeight = $tooltip.outerHeight();
        var tBottomHeight = $tooltip.find('.fox-tooltip-bottom').outerHeight();
        var tWidth = $tooltip.outerWidth();
        var tHolderWidth = self.outerWidth();
        var top = self.offset().top - (tHeight + tBottomHeight);
        var left = self.offset().left;
        $tooltip.css({
            'top': top + 'px',
            'left': left + 'px',
            'opacity': 1
        }).show();
        if (tWidth <= tHolderWidth) {
            var itemLeft = (tHolderWidth - tWidth) / 2;
            left = left + itemLeft;
            $tooltip.css('left', left + 'px');
        } else {
            var itemLeft = (tWidth - tHolderWidth) / 2;
            left = left - itemLeft;
            if (left < 0) {
                left = 0;
            }
            $tooltip.css('left', left + 'px');
        }
    }).on('mouseout', '.trending-sign', function () {
        $('body > .fox-tooltip').remove();
    });

    /*-------------------------------------
    // Popup
    -------------------------------------*/
    var yPopup = $(".popup-youtube");
    if (yPopup.length) {
        yPopup.magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: false,
            fixedContentPos: false
        });
    }
    if ($('.elv-zoom-single').length) {
        $('.elv-zoom-single').magnificPopup({type: 'image'});
    }
    if ($('.zoom-gallery').length) {
        $('.zoom-gallery').each(function () { // the containers for all your galleries
            $(this).magnificPopup({
                delegate: 'a.elv-zoom', // the selector for gallery item
                type: 'image',
                gallery: {
                    enabled: true
                }
            });
        });
    }
    /*-------------------------------------
    // On click loadmore functionality
    -------------------------------------*/
    $('.loadmore').on('click', 'a', function (e) {
        e.preventDefault();
        var _this = $(this),
            _parent = _this.parents('.menu-list-wrapper'),
            _target = _parent.find('.menu-list'),
            _set = _target.find('.menu-item.hidden').slice(0, 4); // Herre 2 is the limit
        if (_set.length) {
            _set.animate({opacity: 0});
            _set.promise().done(function () {
                _set.removeClass('hidden');
                _set.show().animate({opacity: 1}, 1000);
            });
        } else {
            _this.text('No more items to display');
        }
        return false;
    });
    /*-------------------------------------
    // jQuery MeanMenu activation code
     --------------------------------------*/
    $('nav#dropdown').meanmenu({siteLogo: "<div class='mobile-menu-nav-back'><a href='index.html' class='logo-mobile'><img src='img/logo.png' /></a></div>"});
  
    /*-------------------------------------
    // jquery zoom activation code
    -------------------------------------*/
    var ecomZoom = $('.ex1');
    if (ecomZoom.length) {
        $('.ex1').zoom();
    }
    /*-------------------------------------
    // Jquery Scollup
     -------------------------------------*/
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-double-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    /*-------------------------------------
    // Select2 activation code
    -------------------------------------*/
    if ($('#cp-search-form select.select2, #cp-search-form2 select.select2, #post-add-form select.select2').length) {
        $('#cp-search-form select.select2, #cp-search-form2 select.select2, #post-add-form select.select2').select2({
            theme: 'classic',
            dropdownAutoWidth: true,
            width: '100%'
        });
    }
    /*-------------------------------------
    // Window load function
     -------------------------------------*/
    $(window).on('load', function () {
        /*-------------------------------------
        Page Preloader
        -------------------------------------*/
        $('#preloader').fadeOut('slow', function () {
            $(this).remove();
        });
        /*-------------------------------------
        // jQuery for Isotope initialization
         -------------------------------------*/
        var $container = $('#isotope-container');
        if ($container.length > 0) {
            var selector = $container.find('.isotope-classes-tab a.current').attr('data-filter');
            console.log(selector);
            // Isotope initialization
            var $isotope = $container.find('.featuredContainer').isotope({
                filter: selector,
                animationOptions: {
                    duration: 750,
                    easing: 'linear',
                    queue: false
                }
            });
            // Isotope filter
            $container.find('.isotope-classes-tab').on('click', 'a', function () {
                var $this = $(this);
                $this.parent('.isotope-classes-tab').find('a').removeClass('current');
                $this.addClass('current');
                var selector = $this.attr('data-filter');
                $isotope.isotope({
                    filter: selector,
                    animationOptions: {
                        duration: 750,
                        easing: 'linear',
                        queue: false
                    }
                });
                return false;
            });
        }

    });
    /*-------------------------------------
    // About Counter
     -------------------------------------*/
    var counterContainer = $('.counter');
    if (counterContainer.length) {
        counterContainer.counterUp({
            delay: 50,
            time: 5000
        });
    }
    /*-------------------------------------
    // Accordion
     -------------------------------------*/
    var accordion = $('#accordion');
    accordion.children('.panel').children('.panel-collapse').each(function () {
        if ($(this).hasClass('in')) {
            $(this).parent('.panel').children('.panel-heading').addClass('active');
        }
    });
    accordion.on('show.bs.collapse', function (e) {
        $(e.target).prev('.panel-heading').addClass('active');
    }).on('hide.bs.collapse', function (e) {
        $(e.target).prev('.panel-heading').removeClass('active');
    });
    /*-------------------------------------
    // Contact Form initiating
     -------------------------------------*/
    var contactForm = $('#contact-form');
    if (contactForm.length) {
        contactForm.validator().on('submit', function (e) {
            var $this = $(this),
                $target = contactForm.find('.form-response');
            if (e.isDefaultPrevented()) {
                $target.html("<div class='alert alert-success'><p>Please select all required field.</p></div>");
            } else {
                $.ajax({
                    url: "vendor/php/form-process.php",
                    type: "POST",
                    data: contactForm.serialize(),
                    beforeSend: function () {
                        $target.html("<div class='alert alert-info'><p>Loading ...</p></div>");
                    },
                    success: function (text) {
                        if (text === "success") {
                            $this[0].reset();
                            $target.html("<div class='alert alert-success'><p>Message has been sent successfully.</p></div>");
                        } else {
                            $target.html("<div class='alert alert-success'><p>" + text + "</p></div>");
                        }
                    }
                });
                return false;
            }
        });
    }
    /*-------------------------------------
    // login pop up form
    -------------------------------------*/
    $('#login-button').on('click', function (e) {
        e.preventDefault();
        var self = $(this),
            target = self.next('#login-form');
        if (self.hasClass('open')) {
            target.slideUp('slow');
            self.removeClass('open');
        } else {
            target.slideDown('slow');
            self.addClass('open');
        }
    });
    $('#login-form').on('click', '.form-cancel', function (e) {
        e.preventDefault();
        var self = $(this),
            parent = self.parents('#login-form'),
            loginButton = parent.prev('#login-button');
        parent.slideUp('slow');
        loginButton.removeClass('open');
    });
    /*-------------------------------------
    // Google Map
    -------------------------------------*/
    if ($("#googleMap").length) {
        window.onload = function () {
            var styles = [{
                featureType: 'water',
                elementType: 'geometry.fill',
                stylers: [{color: '#b7d0ea'}]
            }, {
                featureType: 'road',
                elementType: 'labels.text.fill',
                stylers: [{visibility: 'off'}]
            }, {
                featureType: 'road',
                elementType: 'geometry.stroke',
                stylers: [{visibility: 'off'}]
            }, {
                featureType: 'road.highway',
                elementType: 'geometry',
                stylers: [{color: '#c2c2aa'}]
            }, {
                featureType: 'poi.park',
                elementType: 'geometry',
                stylers: [{color: '#b6d1b0'}]
            }, {
                featureType: 'poi.park',
                elementType: 'labels.text.fill',
                stylers: [{color: '#6b9a76'}]
            }];
            var options = {
                mapTypeControlOptions: {
                    mapTypeIds: ['Styled']
                },
                center: new google.maps.LatLng(-37.81618, 144.95692),
                zoom: 11,
                disableDefaultUI: true,
                mapTypeId: 'Styled'
            };
            var div = document.getElementById('googleMap');
            var map = new google.maps.Map(div, options);
            var styledMapType = new google.maps.StyledMapType(styles, {name: 'Styled'});
            map.mapTypes.set('Styled', styledMapType);
        };
    }
    /*-------------------------------------
    // Carousel slider initiation
    -------------------------------------*/
    $('.cp-carousel').each(function () {
        var carousel = $(this),
            loop = carousel.data('loop'),
            items = carousel.data('items'),
            margin = carousel.data('margin'),
            stagePadding = carousel.data('stage-padding'),
            autoplay = carousel.data('autoplay'),
            autoplayTimeout = carousel.data('autoplay-timeout'),
            smartSpeed = carousel.data('smart-speed'),
            dots = carousel.data('dots'),
            nav = carousel.data('nav'),
            navSpeed = carousel.data('nav-speed'),
            rXsmall = carousel.data('r-x-small'),
            rXsmallNav = carousel.data('r-x-small-nav'),
            rXsmallDots = carousel.data('r-x-small-dots'),
            rXmedium = carousel.data('r-x-medium'),
            rXmediumNav = carousel.data('r-x-medium-nav'),
            rXmediumDots = carousel.data('r-x-medium-dots'),
            rSmall = carousel.data('r-small'),
            rSmallNav = carousel.data('r-small-nav'),
            rSmallDots = carousel.data('r-small-dots'),
            rMedium = carousel.data('r-medium'),
            rMediumNav = carousel.data('r-medium-nav'),
            rMediumDots = carousel.data('r-medium-dots'),
            rLarge = carousel.data('r-large'),
            rLargeNav = carousel.data('r-large-nav'),
            rLargeDots = carousel.data('r-large-dots'),
            center = carousel.data('center');
            carousel.addClass('owl-carousel');
        carousel.owlCarousel({
            loop: (loop ? true : false),
            items: (items ? items : 4),
            lazyLoad: true,
            margin: (margin ? margin : 0),
            autoplay: (autoplay ? true : false),
            autoplayTimeout: (autoplayTimeout ? autoplayTimeout : 1000),
            smartSpeed: (smartSpeed ? smartSpeed : 250),
            dots: (dots ? true : false),
            nav: (nav ? true : false),
            navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
            navSpeed: (navSpeed ? true : false),
            center: (center ? true : false),
            responsiveClass: true,
            responsive: {
                0: {
                    items: (rXsmall ? rXsmall : 1),
                    nav: (rXsmallNav ? true : false),
                    dots: (rXsmallDots ? true : false)
                },
                480: {
                    items: (rXmedium ? rXmedium : 2),
                    nav: (rXmediumNav ? true : false),
                    dots: (rXmediumDots ? true : false)
                },
                768: {
                    items: (rSmall ? rSmall : 3),
                    nav: (rSmallNav ? true : false),
                    dots: (rSmallDots ? true : false)
                },
                992: {
                    items: (rMedium ? rMedium : 4),
                    nav: (rMediumNav ? true : false),
                    dots: (rMediumDots ? true : false)
                },
                1200: {
                    items: (rLarge ? rLarge : 5),
                    nav: (rLargeNav ? true : false),
                    dots: (rLargeDots ? true : false)
                }
            }
        });
    });
    /*-----------------------------------------
    // Window onLoad and onResize event trigger
    ------------------------------------------*/
    $(window).on('load resize', function () {
        var wHeight = $(window).height(),
            mLogoH = $('a.logo-mobile-menu').outerHeight();
        wHeight = wHeight - 50;
        $('.mean-nav > ul').css('height', wHeight + 'px');
        headerNsliderResize();
    });
    /*-------------------------------------
    // Jquery Stiky Menu at Window Load
    -------------------------------------*/
    $(window).on('scroll', function () {
        var s = $('#sticker'),
            w = $('body'),
            h = s.outerHeight(),
            windowpos = $(window).scrollTop(),
            windowWidth = $(window).width(),
            h3 = s.parent('#header-three'),
            h3H = h3.find('.header-top-bar').outerHeight(),
            topBar = s.prev('.header-top-bar'),
            tempMenu;
        if (windowWidth > 991) {
            w.css('padding-top', '');
            var topBarH, mBottom = 0;
            if (h3.length) {
                topBarH = topBar.outerHeight();
                if (windowpos <= topBarH) {
                    if (h3.hasClass('header-fixed')) {
                        h3.css('top', '-' + windowpos + 'px');
                    }
                }
            }
            if (windowpos >= topBarH) {
                if (h3.length) {
                    s.addClass('stick');
                    if (h3.hasClass('header-fixed')) {
                        h3.css('top', '-' + topBarH + 'px');
                    } else {
                        w.css('padding-top', h + 'px');
                    }
                }
            } else {
                s.removeClass('stick');
                if (h3.length) {
                    w.css('padding-top', 0);
                } else if (h2.length) {
                    h2.removeClass('hide-menu');
                    h2.find('.stick.temp-main-menu').remove();
                }
            }
        }
    });

    function headerNsliderResize() {
        var Hh3 = $('#header-three'),
            wWidth = $(window).width(),
            Hh3slider = Hh3.parents('#wrapper').find("#fixed-type-slider"),
            mHeight = Hh3.outerHeight();
        if (wWidth < 992) {
            mHeight = $('body > .mean-bar').outerHeight();
        }
        Hh3slider.css("margin-top", mHeight + 'px');
    }
})(jQuery);