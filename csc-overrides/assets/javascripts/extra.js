// This enables opening main navigation tabs with enter key
var nav_links = document.getElementsByClassName("md-nav__link");
var openNavIfEnterClicked = function (event) {
  var keyCode = event.which || event.keyCode;
  if (keyCode === 13) {
    event.preventDefault();
    event.target.click();
  }
};

for (var i = 0; i < nav_links.length; i++) {
  nav_links[i].addEventListener("keyup", openNavIfEnterClicked, false);

  // Fix tab key navigation skipping items with nested items
  nav_links[i].setAttribute("tabindex", "0");
}

// With Safari/IE browser, tab key navigation gets stuck at search, this is hack to prevent it
var search_bar = document.getElementsByClassName("md-search__input");
var moveFocusFromSearch = function (event) {
  var keyCode = event.which || event.keyCode;
  if (keyCode === 9) {
    var dropdown = document.querySelector('nav.csc-dropdown.csc-dropdown--header');
    dropdown.focus();
  }
};
search_bar[0].addEventListener("keyup", moveFocusFromSearch, false);

// Disable shortcut key s for search as it messes with assistive technology apparently
document.onkeydown = function (event) {
  if (event.key == "s" && !document.activeElement.classList.contains('md-search__input')) {
    event.preventDefault();
    event.stopPropagation();
  }
};

// The branch 'getCookie("cookieconsent_status") == "allow"' was removed
function fix_youtube() {
  var frames = document.getElementsByTagName('iframe');

  for (var idx = 0; idx < frames.length; idx++) {
    frames[idx].scrolling = "no"
    s_url = frames[idx].srcdoc.split('/');

    if (!s_url[2].includes('youtube')) {
      frames[idx].src = frames[idx].srcdoc;
      frames[idx].removeAttribute("srcdoc");
      return true;
    }

    if (s_url.length == 1) {
      youtube_id = frames[idx].srcdoc;
    }
    else {
      id_index = 1 + s_url.findIndex(a => a == "embed");
      youtube_id = s_url[id_index];
    }

    youtube_link = `https://www.youtube.com/watch?v=${youtube_id}`
    youtube_embed_link = `https://www.youtube.com/embed/${youtube_id}`
    logo_w = frames[idx].width / 8;
    logo_h = frames[idx].height / 8;

    var content = `
              <style>
              .top {
                  position: absolute;
                  left: calc(50% - ${logo_w / 2}px);
                  top: calc(50% - ${logo_h / 2}px);
                  z-index: 1;
              }
              </style>
              <a href=${youtube_link} target="_blank"><img src=https://img.youtube.com/vi/${youtube_id}/0.jpg width=${frames[idx].width} height=${frames[idx].height} ></a>
              <a href=${youtube_link} target="_blank"><img class="top" width=${logo_w} src=https://www.pngkit.com/png/full/2-21145_youtube-logo-transparent-png-pictures-transparent-background-youtube.png></a>
          `
    frames[idx].srcdoc = content
  }
}

window.addEventListener('load', fix_youtube);
