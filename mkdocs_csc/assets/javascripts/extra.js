// This enables opening main navigation tabs with enter key
var nav_links = document.getElementsByClassName("md-nav__link");
var openNavIfEnterClicked = function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    event.target.click();
  }
};

for (var i = 0; i < nav_links.length; i++) {
  nav_links[i].addEventListener("keyup", openNavIfEnterClicked, false);
}

// With Safari browser, tab key navigation gets stuck at search, this is hack to prevent it
var search_bar = document.getElementsByClassName("md-search__input");
var moveFocusFromSearch = function (event) {
  if (event.key === "Tab") {
    var home_nav = document.querySelector('[title="Home"]');
    home_nav.focus();
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