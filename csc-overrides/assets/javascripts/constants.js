const selectors = {
  header: "html > body > header > nav.md-header__inner.md-grid",
  sidebar: "html > body > div.md-container > main.md-main > div.md-main__inner.md-grid > div.md-sidebar.md-sidebar--primary > div.md-sidebar__scrollwrap > div.md-sidebar__inner > nav.md-nav.md-nav--primary",
  navList: "ul.md-nav__list",
  search: "div.md-search[data-md-component='search']",
  repository: "div.md-header__source"
}

const headerElement = document.querySelector(selectors.header)
const searchElement = headerElement.querySelector(selectors.search)
const repositoryElement = headerElement.querySelector(selectors.repository)
const sidebarElement = document.querySelector(selectors.sidebar)
const navListElement = sidebarElement.querySelector(selectors.navList)

const dropdownSites = [
  {
    name: 'CSC.fi',
    description: 'main site',
    url: 'https://www.csc.fi',
    external: true,
    active: false
  },
  {
    name: 'My CSC',
    description: 'customer portal',
    url: 'https://my.csc.fi',
    external: true,
    active: false
  },
  {
    name: 'Research',
    description: 'solutions for research',
    url: 'https://research.csc.fi',
    external: true,
    active: false
  },
  {
    name: 'Docs CSC',
    description: 'user guides',
    url: 'https://docs.csc.fi',
    external: false,
    active: true
  }
]
