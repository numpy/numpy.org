function waitForKernel() {
  let kernelInterval = setInterval(() => {
    try {
      if (thebeKernel) {
        // Hide the enable button & copy, show the shell
        $('#demo-code.fake-shell').css('display', 'none');
        $('#numpy-shell.real-shell').css('display', 'flex');
        $('#numpy-shell').addClass('numpy-shell-border');

        // We need a more specific attribute to add the caret.
        $('.thebelab-cell').attr('id', 'demo-code');
        // Adds the caret
        $('#numpy-shell #demo-code').prepend('<div class="demo-caret" aria-label="interactive shell prompt">&gt;</div>');

        // Style the 'Run' button
        $('.thebelab-button').each(function(idx) {
          if (idx == 0) {
            $(this).attr('id', 'demo-button-run');
            $(this).attr('class', 'shell-button');
            $(this).html('Run <span class="shift-enter">(Shift + Enter)</span>');
          } else {
            $(this).remove();
          }
        });
        // Style the output elements
        $('.jp-OutputArea').parent().closest('div').attr('id', 'demo-output-parent');
        $('.jp-OutputArea').attr('id', 'demo-output');

        // Show the lesson & hide the 'wait' text
        $('.shell-wait').css('display', 'none');
        $('.shell-lesson').css('display', 'flex');
        clearInterval(kernelInterval);
      }
    } catch (err) {
      if (err != 'ReferenceError: thebeKernel is not defined') {
        console.log('Error loading the shell: ', err)
      }
    }
  }, 500);
}

function loadShell() {
  $('#shell-loader').css('display', 'inline-block');
  // Add 'wait' text
  $('.shell-intro').css('display', 'none');
  $('.shell-wait').css('display', 'flex');
  thebelab.bootstrap();
  waitForKernel();
}

// Email Form
$('.sign-up-input').focus(function(e) {
  if ($(window).width() > 850) {
    $('.submission-instructions').css('display', 'block');
  }
}).blur(function(e) {
  if ($(window).width() > 850) {
    $('.submission-instructions').css('display', 'none');
  }
});


function sendThankYou() {
  // Hides the email form to show a thank you
  $('.sign-up-container').css('display', 'none');
  $('.thank-you').css('display', 'flex');

  setTimeout(() => {
    // Resets email input to empty string
    $('#mce-EMAIL').val('');
    $('.thank-you').css('display', 'none');
    $( ".sign-up-container" ).fadeIn( "slow");
  }, 8000);
}

// Content Page Shortcuts
const shortcutsTarget = $('#shortcuts');
if (shortcutsTarget.length > 0) {
  $('.content-container h2, .content-container h3').map(function(idx, el) {
    const title = el.textContent;
    // transforms title into snake-case
    const elTitle = title.replace(/\s/g, '-').toLowerCase();
    // Gets the element type (e.g. h2, h3)
    const elType = $(el).get(0).tagName;
    // Adds snake-case title as an id attribute to target element
    $(el).attr('id', elTitle);
    shortcutsTarget.append(`<div id="${elTitle}-shortcut" class="shortcuts-${elType}">${title}</div>`);

    $(`#${elTitle}-shortcut`).click(function() {
      $([document.documentElement, document.body]).animate({
        scrollTop: $(`#${elTitle}`).offset().top-60
    }, 1000);
    })
  });
}

// Removes the shortcuts container if no shortcuts exist.
// Also removes the 'Get Help' link.
if ($('#shortcuts div').length < 1) {
  $('.shortcuts-container').css('display', 'none');
}