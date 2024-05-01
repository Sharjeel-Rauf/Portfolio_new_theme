(function ( $ ) {
	'use strict';

	window.qiDemosToolbar = {};

	qiDemosToolbar.body          = $( 'body' );
	qiDemosToolbar.html          = $( 'html' );
	qiDemosToolbar.window        = $( window );
	qiDemosToolbar.windowWidth   = $( window ).width();
	qiDemosToolbar.windowHeight  = $( window ).height();
	qiDemosToolbar.scroll        = 0;
	qiDemosToolbar.currentScroll = 0;

	$( document ).on(
		'ready',
		qodefOnDocumentReady

	);

	$( window ).on(
		'scroll',
		qodefOnWindowScroll
	);
	/*
	 All functions to be called on $(window).load() should be in this function
	 */
	function qodefOnDocumentReady() {
		qiDemosToolbar.scroll = $( window ).scrollTop();
		qiDemosToolbar.currentScroll = $( window ).scrollTop();
		qodefQiToolbar()
	}

	function qodefOnWindowScroll() {

	}

	function qodefQiToolbar() {
		var opener = $('.qi-demos-toolbar-holder .qi-demos-toolbar-tab'),
			holder = $('.qi-demos-toolbar-holder');

		// opener.on('click', function () {
		// 	if (holder.hasClass('qi-toolbar-open')) {
		// 		holder.removeClass('qi-toolbar-open');
		// 	} else {
		// 		holder.addClass('qi-toolbar-open');
		// 	}
		// });

		$(window).scroll(function () {
			qiDemosToolbar.currentScroll = $( window ).scrollTop();
			if ( Math.abs( qiDemosToolbar.scroll - qiDemosToolbar.currentScroll ) > 1000 ) {
				if ( ! holder.hasClass( 'qi-toolbar-open' ) ) {
					holder.addClass( 'qi-toolbar-open' );
				}
			}
		});

	}

})( jQuery );
