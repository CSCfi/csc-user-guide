const handleSubmit = rating => {
  console.log(rating)
}

const feedbackFormElement = document.forms.feedback
feedbackFormElement.addEventListener("submit", event => {
  event.preventDefault()
  handleSubmit(event.submitter.value)
})
