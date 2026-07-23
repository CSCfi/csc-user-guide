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
