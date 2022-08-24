const generateAnchor = site => {
  const anchor = document.createElement('a')
  const linkText = document.createTextNode(
    `${site.name}, ${site.description}`
  )
  anchor.classList.add('csc-dropdown__link')
  anchor.href = site.url
  anchor.target = site.external ? "_blank" : "_self"
  anchor.setAttribute('active', site.active)
  anchor.appendChild(linkText)
  return anchor
}

const anchorToItem = anchor => {
  const item = document.createElement('div')
  item.classList.add('csc-dropdown__item')
  item.appendChild(anchor)
  return item
}

const generateContent = items => {
  const content = document.createElement('div')
  content.classList.add('csc-dropdown__content')
  items.forEach(item => {
    content.appendChild(item)
  })
  return content
}

const generateButtonText = text => {
  const buttonText = document.createElement('span')
  buttonText.classList.add('csc-dropdown__text')
  const textNode = document.createTextNode(text)
  buttonText.appendChild(textNode)
  return buttonText
}

const generateButton = () => {
  const button = document.createElement('button')
  button.type = 'button'
  button.classList.add('csc-dropdown__button')
  button.appendChild(generateButtonText('Visit other CSC sites'))
  return button
}

const generateDropdown = () => {
  const dropdown = document.createElement('nav')
  dropdown.classList.add('csc-dropdown')
  dropdown.appendChild(generateButton())
  const dropdownAnchors = dropdownSites.map(site => generateAnchor(site))
  const dropdownItems = dropdownAnchors.map(anchor => anchorToItem(anchor))
  const dropdownContent = generateContent(dropdownItems)
  dropdown.appendChild(dropdownContent)

  return dropdown
}
