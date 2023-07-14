import {
  iframeElements,
  anchorTargetAttributeName,
  anchorTargetAttributeKeyword,
  buttonElementClassNames,
  textOnlyAnchorNodeNames,
  articleAnchorElements
} from "./constants.js"

const getIdIndex = url => 1 + url.findIndex(a => a === "embed")

export const fixYoutube = () => {
  iframeElements.forEach(iframe => {
    const s_url = iframe.srcdoc.split('/')

    if (!s_url[2].includes("youtube")) {
      iframe.src = iframe.srcdoc;
      iframe.removeAttribute("srcdoc")
      return true
    }

    const youtube_id = s_url.length === 1
      ? iframe.srcdoc
      : s_url[getIdIndex(s_url)]

    const youtube_link = `https://www.youtube.com/watch?v=${youtube_id}`
    const logo_w = iframe.width / 8
    const logo_h = iframe.height / 8

    const content = `
      <style>
        .top {
          position: absolute;
          left: calc(50% - ${logo_w / 2}px);
          top: calc(50% - ${logo_h / 2}px);
          z-index: 1;
        }
      </style>
      <a href=${youtube_link} ${anchorTargetAttributeName}="${anchorTargetAttributeKeyword}"><img src=https://img.youtube.com/vi/${youtube_id}/0.jpg width=${iframe.width} height=${iframe.height}></a>
      <a href=${youtube_link} ${anchorTargetAttributeName}="${anchorTargetAttributeKeyword}"><img class="top" width=${logo_w} src=https://www.pngkit.com/png/full/2-21145_youtube-logo-transparent-png-pictures-transparent-background-youtube.png></a>
    `

    iframe.srcdoc = content
  })
}

export const disableSearchShortcuts = () => {
  // Disable shortcut keys for search as they mess with assistive technology apparently
  document.onkeydown = event => {
    if (["s","f","/"].includes(event.key) && !document.activeElement?.form) {
      event.preventDefault();
      event.stopPropagation();
    }
  }
}

export const decorateExternalLinks = () => {
  const hasHost = a => !!a.host
  const hasNoTarget = a => !a.hasAttribute(anchorTargetAttributeName)
  const notButton = a => buttonElementClassNames.every(className => !a.classList.contains(className))
  const isExternal = a => a.host !== window.location.host
  const isTextOnly = a => Array.from(a.childNodes)
    .map(node => node.nodeName)
    .every(nodeName => textOnlyAnchorNodeNames.includes(nodeName))

  const anchorFilterTests = [
    hasHost,
    isExternal,
    notButton,
    (a) => hasNoTarget(a) || isTextOnly(a),
  ]

  articleAnchorElements
    .filter(a => anchorFilterTests.every(t => t(a)))
    .forEach(a => {
      a.setAttribute(anchorTargetAttributeName, anchorTargetAttributeKeyword)
      if (isTextOnly(a)) a.classList.add("csc-external-link")
    })
}
