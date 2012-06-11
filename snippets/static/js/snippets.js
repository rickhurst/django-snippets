// basic version: snippet editing in centered pop-up window
(function ($) {

	"use strict";

	jQuery.fn.snippetPopUps = function () {
		var self = this;
		self.find('.snippet').each(function(){
			var url = '/snippets/edit-snippet/' + $(this).attr('data-slug') + '/popup/';
			$(this).find('a:first').click(function(e){
				centeredPopUp(url, 'snippet', 600, 400, 'location=no');
				e.preventDefault();
			});
		});
	}
	
	$('body').snippetPopUps();
}(jQuery));

var win = null;
function centeredPopUp(url,winname,w,h,features) {
  var winl = (screen.width-w)/2;
  var wint = (screen.height-h)/2;
  if (winl < 0) winl = 0;
  if (wint < 0) wint = 0;
  var settings = 'height=' + h + ',';
  settings += 'width=' + w + ',';
  settings += 'top=' + wint + ',';
  settings += 'left=' + winl + ',';
  settings += features;
  win = window.open(url,winname,settings);
  win.window.focus();
}

function popUpCallBack(){
	if(win != null){
        win.close();
    }
    window.location.reload();
}