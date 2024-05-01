!function(t){"use strict";window.qodefCore={},qodefCore.shortcodes={},qodefCore.body=t("body"),qodefCore.html=t("html"),qodefCore.windowWidth=t(window).width(),qodefCore.windowHeight=t(window).height(),qodefCore.scroll=0,t(document).ready(function(){qodefCore.scroll=t(window).scrollTop(),w.init(),e.init(),o.init()}),t(window).resize(function(){qodefCore.windowWidth=t(window).width(),qodefCore.windowHeight=t(window).height()}),t(window).scroll(function(){qodefCore.scroll=t(window).scrollTop()});var w={init:function(e){this.holder=t(".qodef-swiper-container"),t.extend(this.holder,e),this.holder.length&&this.holder.each(function(){w.createSlider(t(this))})},createSlider:function(e){var o=w.getOptions(e),i=w.getEvents(e,o);e.hasClass("qodef-swiper--initialized")||new Swiper(e,Object.assign(o,i))},getOptions:function(e){var o=void 0!==e.data("options")?e.data("options"):{},i=void 0!==o.spaceBetween&&""!==o.spaceBetween?o.spaceBetween:0,n=void 0!==o.slidesPerView&&""!==o.slidesPerView?o.slidesPerView:1,t=void 0!==o.centeredSlides&&""!==o.centeredSlides&&o.centeredSlides,d=void 0!==o.sliderScroll&&""!==o.sliderScroll&&o.sliderScroll,s=void 0===o.loop||""===o.loop||o.loop,a=void 0===o.autoplay||""===o.autoplay||o.autoplay,r=void 0!==o.speed&&""!==o.speed?parseInt(o.speed,10):5e3,l=void 0!==o.speedAnimation&&""!==o.speedAnimation?parseInt(o.speedAnimation,10):800,c=void 0!==o.customStages&&""!==o.customStages&&o.customStages,f=void 0!==o.outsideNavigation&&"yes"===o.outsideNavigation,u=f?".swiper-button-next-"+o.unique:e.find(".swiper-button-next"),h=f?".swiper-button-prev-"+o.unique:e.find(".swiper-button-prev"),p=e.find(".swiper-pagination");!1!==a&&5e3!==r&&(a={delay:r});var q=void 0!==o.slidesPerView1440&&""!==o.slidesPerView1440?parseInt(o.slidesPerView1440,10):5,v=void 0!==o.slidesPerView1366&&""!==o.slidesPerView1366?parseInt(o.slidesPerView1366,10):4,m=void 0!==o.slidesPerView1024&&""!==o.slidesPerView1024?parseInt(o.slidesPerView1024,10):3,f=void 0!==o.slidesPerView768&&""!==o.slidesPerView768?parseInt(o.slidesPerView768,10):2,r=void 0!==o.slidesPerView680&&""!==o.slidesPerView680?parseInt(o.slidesPerView680,10):1,o=void 0!==o.slidesPerView480&&""!==o.slidesPerView480?parseInt(o.slidesPerView480,10):1;return c||(n<2?f=m=v=q=n:n<3?m=v=q=n:n<4?v=q=n:n<5&&(q=n)),Object.assign({slidesPerView:n,centeredSlides:t,sliderScroll:d,spaceBetween:i,autoplay:a,loop:s,speed:l,navigation:{nextEl:u,prevEl:h},pagination:{el:p,type:"bullets",clickable:!0},breakpoints:{0:{slidesPerView:o},481:{slidesPerView:r},681:{slidesPerView:f},769:{slidesPerView:m},1025:{slidesPerView:v},1367:{slidesPerView:q},1441:{slidesPerView:n}}},w.getSliderDatas(e))},getSliderDatas:function(e){var o,i=e.data(),n={};for(o in i)i.hasOwnProperty(o)&&"options"!==o&&void 0!==i[o]&&""!==i[o]&&(n[o]=i[o]);return n},getEvents:function(i,e){return{on:{init:function(){var o;i.addClass("qodef-swiper--initialized"),e.sliderScroll&&(o=!1,i.on("mousewheel",function(e){e.preventDefault(),o||(o=!0,e.deltaY<0?i[0].swiper.slideNext():i[0].swiper.slidePrev(),setTimeout(function(){o=!1},1e3))}))}}}}};qodefCore.qodefSwiper=w,"function"!=typeof Object.assign&&(Object.assign=function(e){if(null==e)throw new TypeError("Cannot convert undefined or null to object");e=Object(e);for(var o=1;o<arguments.length;o++){var i=arguments[o];if(null!==i)for(var n in i)Object.prototype.hasOwnProperty.call(i,n)&&(e[n]=i[n])}return e});var e={init:function(){if(this.holder=t(".qodef-fslightbox-popup"),this.holder.length){refreshFsLightbox();for(const n in fsLightboxInstances)fsLightboxInstances[n].props.onInit=()=>{var e=fsLightboxInstances[n].elements.container,o=e.querySelectorAll(".fslightbox-slide-btn-container-previous > .fslightbox-slide-btn"),i=e.querySelectorAll(".fslightbox-slide-btn-container-next > .fslightbox-slide-btn"),e=e.querySelectorAll('[title="Close"]');o[0].innerHTML=qodefGlobal.vars.iconArrowLeft,i[0].innerHTML=qodefGlobal.vars.iconArrowRight,e[0].innerHTML=qodefGlobal.vars.iconClose}}}};qodefCore.qodefFsLightboxPopup=e;var o={init:function(){var e;this.holder=t("#qode-essential-addons-page-inline-style"),!this.holder.length||(e=this.holder.data("style")).length&&t("head").append('<style type="text/css">'+e+"</style>")}};qodefCore.qodefWaitForImages={check:function(e,o){if(e.length){var i=e.find("img");if(i.length)for(var n=0,t=0;t<i.length;t++){var d,s=i[t];s.complete?++n===i.length&&o.call(e):((d=new Image).addEventListener("load",function(){if(++n===i.length)return o.call(e),!1},!1),d.src=s.src)}else o.call(e)}}},qodefCore.qodefInfoFollow={init:function(e,o=""){var i,n;e.length&&(qodefCore.body.append('<div class="qodef-e-content-follow '+o+'"><div class="qodef-e-content"></div></div>'),i=t(".qodef-e-content-follow"),n=i.find(".qodef-e-content"),1024<qodefCore.windowWidth&&e.each(function(){t(this).find(".qodef-e-inner").each(function(){var e=t(this);e.on("mousemove",function(e){e.clientX+i.width()+20>qodefCore.windowWidth?i.addClass("qodef-right"):i.removeClass("qodef-right"),i.css({top:e.clientY+20,left:e.clientX+20})}),e.on("mouseenter",function(){var e=t(this).find(".qodef-e-content");e.length&&n.html(e.html()),i.hasClass("qodef-is-active")?(i.removeClass("qodef-is-active"),setTimeout(function(){i.addClass("qodef-is-active")},10)):i.addClass("qodef-is-active")}).on("mouseleave",function(){i.hasClass("qodef-is-active")&&i.removeClass("qodef-is-active")}),t(window).on("wheel",function(){i.hasClass("qodef-is-active")&&i.removeClass("qodef-is-active")})})}))}}}(jQuery),function(d){"use strict";d(document).ready(function(){s.init()});var s={init:function(){this.holder=d("#qodef-back-to-top"),this.holder.length&&(this.holder.on("click",function(e){e.preventDefault(),s.animateScrollToTop()}),s.showHideBackToTop())},animateScrollToTop:function(){function o(){var e;0!==t&&(t<1e-4&&(t=0),e=s.easingFunction((n-t)/n),d("html, body").scrollTop(n-(n-t)*e),t*=.9,i=requestAnimationFrame(o))}var i,n=qodefCore.scroll,t=qodefCore.scroll;o(),d(window).one("wheel touchstart",function(){cancelAnimationFrame(i)})},easingFunction:function(e){return 0===e?0:Math.pow(1024,e-1)},showHideBackToTop:function(){d(window).scroll(function(){var e=d(this),o=e.scrollTop(),e=e.height(),e=0<o?o+e/2:1;e<1e3?s.addClass("off"):s.addClass("on")})},addClass:function(e){this.holder.removeClass("qodef--off qodef--on"),"on"===e?this.holder.addClass("qodef--on"):this.holder.addClass("qodef--off")}}}(jQuery),function(t){"use strict";t(document).ready(function(){d.init()});var d={init:function(){var i=t("a.qodef-fullscreen-menu-opener"),n=t("a.qodef-fullscreen-menu-close"),e=t("#qodef-fullscreen-area nav ul li a");i.on("click",function(e){e.preventDefault();var o=t(this);qodefCore.body.hasClass("qodef-fullscreen-menu--opened")?d.closeFullscreen(o):(d.openFullscreen(o),n.on("click",function(e){e.preventDefault(),d.closeFullscreen(o)}),t(document).keyup(function(e){27===e.keyCode&&d.closeFullscreen(o)}))}),e.on("tap click",function(e){var o=t(this);o.parent().hasClass("menu-item-has-children")?(e.preventDefault(),d.clickItemWithChild(o)):"http://#"!==o.attr("href")&&"#"!==o.attr("href")&&d.closeFullscreen(i)})},openFullscreen:function(e){e.addClass("qodef--opened").attr("aria-expanded","true"),qodefCore.body.removeClass("qodef-fullscreen-menu-animate--out").addClass("qodef-fullscreen-menu--opened qodef-fullscreen-menu-animate--in")},closeFullscreen:function(e){e.removeClass("qodef--opened").attr("aria-expanded","false"),qodefCore.body.removeClass("qodef-fullscreen-menu--opened qodef-fullscreen-menu-animate--in").addClass("qodef-fullscreen-menu-animate--out"),t("nav.qodef-fullscreen-menu ul.sub_menu").slideUp(200)},clickItemWithChild:function(e){var o=e.parent(),e=o.find(".sub-menu").first();e.is(":visible")?(e.slideUp(300),o.removeClass("qodef--opened")):(e.slideDown(300),o.addClass("qodef--opened").siblings().find(".sub-menu").slideUp(400))}}}(jQuery),function(s){"use strict";s(document).ready(function(){o.init()});var o={init:function(){var e=s("#qodef-page-header .qodef-header-vertical-navigation");o.dropdownClickToggle(e)},dropdownClickToggle:function(e){var d=e.find("ul li.menu-item-has-children");d.each(function(){var o=s(this),i=o.find("> ul"),n=o.find("> a"),t="fast";n.on("click tap",function(e){e.preventDefault(),e.stopPropagation();e=s(this);i.is(":visible")?(o.removeClass("qodef--opened"),i.slideUp(t)):(n.parent().parent().children().hasClass("qodef--opened")?(e.parent().parent().children().removeClass("qodef--opened"),e.parent().parent().children().find("> ul").slideUp(t)):(e.parents("li").hasClass("qodef--opened")||(d.removeClass("qodef--opened"),d.find("> ul").slideUp(t)),e.parent().parent().children().hasClass("qodef--opened")&&(e.parent().parent().children().removeClass("qodef--opened"),e.parent().parent().children().find("> ul").slideUp(t))),o.addClass("qodef--opened"),i.slideDown("slow"))})})}}}(jQuery),function(){"use strict";jQuery(document).ready(function(){e.init()});var e={appearanceType:function(){return-1!==qodefCore.body.attr("class").indexOf("qodef-header-appearance--")?qodefCore.body.attr("class").match(/qodef-header-appearance--([\w]+)/)[1]:""},init:function(){var e=this.appearanceType();""!==e&&"none"!==e&&qodefCore[e+"HeaderAppearance"]()}}}(),function(t){"use strict";t(document).ready(function(){d.init()}),t(window).resize(function(){d.reInit()}),t(window).on("elementor/frontend/init",function(){elementorFrontend.isEditMode()&&elementor.channels.editor.on("change",function(){d.reInit()})});var d={init:function(e){this.holder=t(".qodef-layout--masonry"),t.extend(this.holder,e),this.holder.length&&this.holder.each(function(){d.createMasonry(t(this))})},reInit:function(e){this.holder=t(".qodef-layout--masonry"),t.extend(this.holder,e),this.holder.length&&this.holder.each(function(){var e=t(this).hasClass("qodef-woo-product-list")?t(this).find("ul.products"):t(this).find(".qodef-grid-inner"),o=e.find(".qodef-grid-item"),i=e.find(".qodef-grid-masonry-sizer").width(),n=parseInt(e.css("column-gap"));o.css("width",i),"function"==typeof e.isotope&&void 0!==e.data("isotope")&&(t(this).hasClass("qodef-items--fixed")&&d.setFixedImageProportionSize(e,o,i,n),e.isotope({layoutMode:"packery",itemSelector:".qodef-grid-item",percentPosition:!0,packery:{columnWidth:".qodef-grid-masonry-sizer",gutter:n}}))})},createMasonry:function(e){e.hasClass("qodef-woo-product-list")&&e.find("ul.products").prepend('<li class="qodef-grid-masonry-sizer"></li>');var o=e.hasClass("qodef-woo-product-list")?e.find("ul.products"):e.find(".qodef-grid-inner"),i=o.find(".qodef-grid-item"),n=o.find(".qodef-grid-masonry-sizer").width(),t=parseInt(o.css("column-gap"));i.css("width",n),qodefCore.qodefWaitForImages.check(o,function(){"function"!=typeof o.isotope||o.hasClass("qodef--masonry-init")||(e.hasClass("qodef-items--fixed")&&d.setFixedImageProportionSize(o,i,n,t),o.isotope({layoutMode:"packery",itemSelector:".qodef-grid-item",percentPosition:!0,packery:{columnWidth:".qodef-grid-masonry-sizer",gutter:t}})),o.addClass("qodef--masonry-init")})},setFixedImageProportionSize:function(e,o,i,n){var t=e.find(".qodef-item--square"),d=e.find(".qodef-item--landscape"),s=e.find(".qodef-item--portrait"),a=e.find(".qodef-item--huge-square"),r=qodefCore.windowWidth<=680;e.parent().hasClass("qodef-col-num--1")?(o.css({height:i}),t.length&&t.css({width:i}),d.length&&d.css({height:Math.round(i/2)}),s.length&&s.css({height:Math.round(2*i)}),a.length&&a.css({width:i})):(o.css({height:i}),d.length&&d.css({width:Math.round(2*i+n)}),s.length&&s.css({height:Math.round(2*i+n)}),a.length&&a.css({height:Math.round(2*i+n),width:Math.round(2*i+n)}),r&&(d.length&&d.css({height:Math.round(i/2),width:Math.round(i)}),a.length&&a.css({height:Math.round(i),width:Math.round(i)})))}};qodefCore.qodefMasonryLayout=d}(jQuery),function(i){"use strict";i(document).ready(function(){n.init()});var n={init:function(){var e=i("a.qodef-side-area-opener"),o=i("#qodef-side-area-close");n.openerHoverColor(e),e.on("click",function(e){e.preventDefault();e=i(this);qodefCore.body.hasClass("qodef-side-area--opened")?n.closeSideArea():(n.openSideArea(e),i(document).keyup(function(e){27===e.keyCode&&n.closeSideArea()}))}),o.on("click",function(e){e.preventDefault(),n.closeSideArea()}),n.initScroll()},openSideArea:function(e){e.attr("aria-expanded","true");var e=i("#qodef-page-wrapper"),o=i(window).scrollTop();i(".qodef-side-area-cover").remove(),e.prepend('<div class="qodef-side-area-cover"/>'),qodefCore.body.removeClass("qodef-side-area-animate--out").addClass("qodef-side-area--opened qodef-side-area-animate--in"),i(".qodef-side-area-cover").on("click",function(e){e.preventDefault(),n.closeSideArea()}),i(window).scroll(function(){400<Math.abs(qodefCore.scroll-o)&&n.closeSideArea()})},closeSideArea:function(){i("a.qodef-side-area-opener").attr("aria-expanded","false"),qodefCore.body.removeClass("qodef-side-area--opened qodef-side-area-animate--in").addClass("qodef-side-area-animate--out")},openerHoverColor:function(e){var o,i;void 0!==e.data("hover-color")&&(o=e.data("hover-color"),i=e.css("color"),e.on("mouseenter",function(){e.css("color",o)}).on("mouseleave",function(){e.css("color",i)}))},initScroll:function(){var e,o=i("#qodef-side-area-inner");o.length&&(e=new PerfectScrollbar(o.parent()[0],{wheelSpeed:.6,suppressScrollX:!0}),i(window).resize(function(){e.update()}))}}}(jQuery),function(d){"use strict";d(document).ready(function(){s.init()});var s={init:function(){this.deactivationLink=d("#the-list").find('[data-slug="qode-essential-addons"] span.deactivate a'),this.deactivationModal=d("#qode-essential-addons-deactivation-modal"),this.deactivationLink.length&&this.deactivationModal.length&&this.initModal()},initModal:function(){this.deactivationLink.on("click",function(e){e.preventDefault(),s.deactivationModal.fadeIn("fast")}),this.enableModalCloseFunctionality(),this.initSubmitFunctionality(),this.initSkipFunctionality()},enableSubmitButton:function(){var e=this.deactivationModal.find('input[name="reason_key"]'),o=this.deactivationModal.find(".qodef-deactivation-modal-button-submit");e.on("change",function(){o.removeClass("qodef--disabled")})},initSubmitFunctionality:function(){var i=this.deactivationModal.find(".qodef-deactivation-modal-button-submit"),n=this.deactivationModal.find(".qodef-deactivation-modal-button-skip"),t=this.deactivationModal.find("#qode-essential-addons-deactivation-nonce");i.length&&i.on("click",function(e){e.preventDefault(),i.addClass("qodef--processing"),n.addClass("qodef--disabled");var o,e=s.deactivationModal.find('input[name="reason_key"]:checked').val();switch(e){case"found_a_better_plugin":o=s.deactivationModal.find('input[name="reason_found_a_better_plugin"]').val();break;case"other":o=s.deactivationModal.find('input[name="reason_other"]').val();break;default:o=""}d.ajax({type:"POST",data:{action:"qode_essential_addons_deactivation",reason:e,additionalInfo:o,nonce:t.val()},url:ajaxurl,success:function(e){d.parseJSON(e);s.deactivatePlugin()}})})},initSkipFunctionality:function(){var o=this.deactivationModal.find(".qodef-deactivation-modal-button-submit"),i=this.deactivationModal.find(".qodef-deactivation-modal-button-skip");i.length&&i.on("click",function(e){e.preventDefault(),i.addClass("qodef--processing"),o.addClass("qodef--disabled"),s.deactivatePlugin()})},deactivatePlugin:function(){location.href=this.deactivationLink.attr("href")},enableModalCloseFunctionality:function(){var e=this.deactivationModal.find(".qodef-deactivation-modal-close");e.length&&e.on("click",function(e){e.preventDefault(),s.deactivationModal.fadeOut("fast")})}}}(jQuery),function(n){"use strict";var e="qode_essential_addons_blog_list";qodefCore.shortcodes[e]={},n(document).ready(function(){o.init()}),n(window).resize(function(){o.init()});var o={init:function(){var e=n(".qodef-blog-shortcode");e.length&&o.resize(e)},resize:function(e){e=e.find(".qodef-e-media iframe");e.length&&e.each(function(){var e=n(this),o=e.attr("width"),i=e.attr("height"),i=e.width()/o*i;e.css("height",i)})}};qodefCore.shortcodes[e].qodefSwiper=qodefCore.qodefSwiper,qodefCore.shortcodes[e].qodefFsLightboxPopup=qodefCore.qodefFsLightboxPopup,qodefCore.shortcodes[e].qodefMasonryLayout=qodefCore.qodefMasonryLayout,qodefCore.shortcodes[e].qodefCoreResizeIframes=o}(jQuery),function(t){"use strict";var i={showHideHeader:function(e,o){var i,n=parseInt(o.css("margin-top"))+parseInt(o.css("margin-bottom"));1024<qodefCore.windowWidth&&(i=(i=t(".qodef-elementor-section-before-header")).length?i.height():0,qodefCore.scroll<=i?(qodefCore.body.removeClass("qodef-header--fixed-display"),e.css("padding-top","0"),o.css("top","")):(qodefCore.body.addClass("qodef-header--fixed-display"),e.css("padding-top",parseInt(qodefGlobal.vars.headerHeight+qodefGlobal.vars.topAreaHeight+n)+"px"),o.css("top",parseInt(qodefGlobal.vars.topAreaHeight+qodefGlobal.vars.adminBarHeight)+"px")))},init:function(){var e,o;qodefCore.body.hasClass("qodef-header--vertical")||(e=t("#qodef-page-outer"),o=t("#qodef-page-header"),i.showHideHeader(e,o),t(window).scroll(function(){i.showHideHeader(e,o)}),t(window).resize(function(){e.css("padding-top","0"),i.showHideHeader(e,o)}))}};qodefCore.fixedHeaderAppearance=i.init}(jQuery),function(n){"use strict";var t={header:"",docYScroll:0,init:function(){var e=t.displayAmount();t.header=n(".qodef-header-sticky"),t.docYScroll=n(document).scrollTop(),t.setVisibility(e),n(window).scroll(function(){t.setVisibility(e)})},displayAmount:function(){if(0!==qodefGlobal.vars.qodefStickyHeaderScrollAmount)return parseInt(qodefGlobal.vars.qodefStickyHeaderScrollAmount,10);var e=n(".qodef-elementor-section-before-header"),e=e.length?e.height():0;return parseInt(qodefGlobal.vars.headerHeight+qodefGlobal.vars.adminBarHeight+e,10)},setVisibility:function(e){var o,i=qodefCore.scroll<e;t.header.hasClass("qodef-appearance--up")&&(i=(o=n(document).scrollTop())>t.docYScroll&&e<o||o<e,t.docYScroll=n(document).scrollTop()),t.showHideHeader(i)},showHideHeader:function(e){e?qodefCore.body.removeClass("qodef-header--sticky-display"):qodefCore.body.addClass("qodef-header--sticky-display")}};qodefCore.stickyHeaderAppearance=t.init}(jQuery),function(i){"use strict";i(document).ready(function(){n.init()});var n={init:function(){var e=i("a.qodef-search-opener");e.length&&e.each(function(){var o=i(this).closest(".qodef-header-sticky, #qodef-page-header").find(".qodef-search-cover-form"),e=o.find(".qodef-m-close");o.length&&(i(this).on("click",function(e){e.preventDefault(),n.openCoversHeader(o)}),e.on("click",function(e){e.preventDefault(),n.closeCoversHeader(o)}))})},openCoversHeader:function(e){qodefCore.body.addClass("qodef-covers-search--opened qodef-covers-search--fadein"),qodefCore.body.removeClass("qodef-covers-search--fadeout"),setTimeout(function(){e.find(".qodef-m-form-field").focus()},600)},closeCoversHeader:function(e){qodefCore.body.removeClass("qodef-covers-search--opened qodef-covers-search--fadein"),qodefCore.body.addClass("qodef-covers-search--fadeout"),setTimeout(function(){e.find(".qodef-m-form-field").val(""),e.find(".qodef-m-form-field").blur(),qodefCore.body.removeClass("qodef-covers-search--fadeout")},300)}}}(jQuery),function(o){"use strict";o(document).ready(function(){i.init()});var i={init:function(){this.search=o("a.qodef-search-opener"),this.search.length&&this.search.each(function(){var e=o(this);i.searchHoverColor(e)})},searchHoverColor:function(e){var o,i;void 0!==e.data("hover-color")&&(o=e.data("hover-color"),i=e.css("color"),e.on("mouseenter",function(){e.css("color",o)}).on("mouseleave",function(){e.css("color",i)}))}}}(jQuery),function(){"use strict";var e="qode_essential_addons_product_list";qodefCore.shortcodes[e]={},qodefCore.shortcodes[e].qodefSwiper=qodefCore.qodefSwiper,qodefCore.shortcodes[e].qodefFsLightboxPopup=qodefCore.qodefFsLightboxPopup,qodefCore.shortcodes[e].qodefMasonryLayout=qodefCore.qodefMasonryLayout}(jQuery),function(o){"use strict";var e="qode_essential_addons_portfolio_list";qodefCore.shortcodes[e]={},qodefCore.shortcodes[e].qodefSwiper=qodefCore.qodefSwiper,qodefCore.shortcodes[e].qodefFsLightboxPopup=qodefCore.qodefFsLightboxPopup,qodefCore.shortcodes[e].qodefMasonryLayout=qodefCore.qodefMasonryLayout,o(document).ready(function(){i.init()});var i={init:function(){var e=o(".qodef-item-layout--info-follow");e.length&&e.each(function(){i.initItem(o(this))})},initItem:function(e){e.hasClass("qodef-item-layout--info-follow")&&qodefCore.qodefInfoFollow.init(e)}};qodefCore.shortcodes[e].qodefFloatingPortfolio=i}(jQuery);