// Module preload links are defined inside {% block libs %} in main.html template

const main = async () => {
  const layout = await import("./modules/layout.js")
  layout.swapHeaderElements()
  layout.insertDropdown()

  const feedback = await import("./modules/feedback.js")
  feedback.initialize()

  const utils = await import("./modules/utils.js")
  utils.disableSearchShortcuts()
  utils.fixYoutube()
  utils.decorateExternalLinks()
}

window.addEventListener('load', main, false)
