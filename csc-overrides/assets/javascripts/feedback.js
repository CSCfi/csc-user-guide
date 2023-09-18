const feedbackForm = document.forms.feedback
const ratingKey = `${window.location.pathname} rating`
const pageEdited = Date.parse(feedbackForm.dataset.sourceEdited)

const ratingExists = () => {
  const item = window.localStorage.getItem(ratingKey)
  if (!item) return false

  const rating = JSON.parse(item)
  return rating.date > pageEdited
}

const getRating = () => {
  const item = window.localStorage.getItem(ratingKey)

  return JSON.parse(item).rating
}

const setRating = rating => {
  const item = JSON.stringify({ date: Date.now(), rating })

  window.localStorage.setItem(ratingKey, item)
  setForm()
}

const trackRating = rating => {
  const [ first, ...rest ] = rating
  const name = first.toUpperCase() + rest.join("")
  const value = rating === "positive" ? 1 : -1
  const event = [ "trackEvent", "Feedback", "Feedback Button Click", name, value ]

  _paq && _paq.push(event)
}

const handleSubmit = rating => {
  if (!ratingExists()) {
    setRating(rating)
    trackRating(rating)
  }
}

const setForm = () => {
  if (ratingExists()) {
    const rating = getRating()
    const feedbackFormContentElement = document.querySelector(".csc-feedback-content")
    feedbackFormContentElement.classList.add("csc-rated", `csc-rated--${rating}`)
  }
}

feedbackForm.addEventListener("submit", event => {
  event.preventDefault()

  const { submitter: { value: rating } } = event

  handleSubmit(rating)
})

window.addEventListener("load", setForm)
