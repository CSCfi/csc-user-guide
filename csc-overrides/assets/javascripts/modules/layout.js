import { generateDropdown } from "./dropdown.js"
import {
  headerElement,
  searchElement,
  repositoryElement,
  sidebarElement,
  navListElement,
  dropdownSites
} from "./constants.js"


/* Reorder the Material for MkDocs header flex element, so that the
   repository link is rendered on the left of the search field. */
export const swapHeaderElements = () => {
  headerElement.insertBefore(repositoryElement, searchElement)
}

/* Insert a dropdown menu into header and sidebar (when the one in
   header is hidden) for visiting other CSC sites. */
export const insertDropdown = () => {
  const dropdownElement = generateDropdown(dropdownSites)
  const dropdownSidebarElement = dropdownElement.cloneNode(true)

  dropdownElement.classList.add('csc-dropdown--header')
  dropdownSidebarElement.classList.add("csc-dropdown--sidebar")

  headerElement.appendChild(dropdownElement)
  sidebarElement.insertBefore(dropdownSidebarElement, navListElement)
}
