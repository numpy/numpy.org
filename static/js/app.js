$(function () {
  if ($) {
    let interval = setInterval(() => {
      const exists = $('.thebelab-cell').length;
      if (exists) {
        $('.thebelab-cell').attr('id', 'demo-code');
        $('#demo-code').css('position', 'relative');
        $('#demo-code').prepend('<div class="demo-caret">&gt;</div>');
        $('.thebelab-input').attr('id', 'demo-input');
        $('.thebelab-button').each(function(idx) {
          if (idx == 0) {
            $(this).attr('id', 'demo-button-run');
            $(this).html('Run <span class="shift-enter">(Shift + Enter)</span>');
          } else {
            $(this).remove();
          }
        });
        $('.jp-OutputArea').parent().closest('div').attr('id', 'demo-output-parent');
        $('.jp-OutputArea').attr('id', 'demo-output');
        clearInterval(interval);
      }
    }, 250);
  }

  // Shortcuts
  const shortcutsTarget = $('#shortcuts');
  if (shortcutsTarget.length > 0) {
    $('.content-container h2, .content-container h3').map(function(idx, el) {
      const title = el.textContent;
      const elType = $(el).get(0).tagName;
      shortcutsTarget.append(`<div class="shortcuts-${elType}">${title}</div>`)
    });
  }
});