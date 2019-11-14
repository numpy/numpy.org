$(function () {
  if ($) {
    let interval = setInterval(() => {
      const exists = $('.thebelab-cell').length;
      if (exists) {
        $('.thebelab-cell').attr('id', 'demo-code');
        $('.thebelab-input').attr('id', 'demo-input');
        $('.thebelab-button').each(function(idx) {
          if (idx == 0) {
            $(this).attr('id', 'demo-button-run');
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
});