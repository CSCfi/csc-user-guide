const RatingStorage = class {
  static #disabled = false
  static #storage = window.localStorage
  static #key = "pageRatings"
  static {
    try {
      if (!this.#storage.getItem(this.#key)) {
        this.#storage.setItem(this.#key, JSON.stringify({}))
      }
    } catch (exception) {
      console.error("Error initializing localStorage for pageRatings:", exception)
      this.#disabled = true
    }
  }
  static get disabled() {
    return this.#disabled
  }
  static getRatings() {
    return this.#disabled
      ? null
      : JSON.parse(this.#storage.getItem(this.#key))
  }
  static setRatings(ratings) {
    try {
      this.#storage.setItem(this.#key, JSON.stringify(ratings))
    } catch (exception) {
      console.error("Error saving ratings to localStorage:", exception)
      this.#disabled = true
    }
  }
}

const PageRating = class {
  #value
  #storage
  #sourcePath
  #sourceEditDate
  static #itemKey = window.location.pathname
  constructor(page) {
    this.#value = null
    this.#storage = RatingStorage
    this.#sourcePath = page.sourcePath
    this.#sourceEditDate = Date.parse(page.sourceEdited)

    if (this.exists && this.#outdated) {
      this.#removeRating()
    }
  }
  get #current() {
    const ratings = this.#storage.getRatings()

    return ratings[PageRating.#itemKey]
  }
  get #type() {
    return this.#value >= 0
      ? "Positive"
      : "Negative"
  }
  get #outdated() {
    return this.#current.date < this.#sourceEditDate ||
      this.#current.source !== this.#sourcePath ||
      typeof this.#current.value === "undefined"
  }
  get exists() {
    return typeof this.#current !== "undefined"
  }
  get value() {
    return this.#current.value
  }
  #removeRating() {
    const ratings = this.#storage.getRatings()
    delete ratings[PageRating.#itemKey]

    this.#storage.setRatings(ratings)
  }
  #newRating() {
    return ({ date: Date.now(), source: this.#sourcePath, type: this.#type, value: this.#value })
  }
  #trackRating() {
    const rating = this.#current

    if (rating && typeof rating.value === "number") {
      const category = "Page Feedback"
      const action = `${rating.type} Rating`
      const name = this.#sourcePath
      const feedbackEvent = ["trackEvent", category, action, name, rating.value]

      window._paq && window._paq.push(feedbackEvent)
    }
  }
  give(value) {
    this.#value = value
    const ratings = this.#storage.getRatings()

    ratings[PageRating.#itemKey] = this.#newRating()
    this.#storage.setRatings(ratings)
    if (!this.#storage.disabled) this.#trackRating()
  }
}

const disableWith = (feedback, value) => {
  feedback.firstElementChild.disabled = true

  const noteElement = feedback.querySelector(
    `.md-feedback__note [data-md-value="${value}"]`
  )
  const buttonElement = feedback.querySelector(
    `.md-feedback__list button.md-feedback__icon[data-md-value="${value}"]`
  )

  if (noteElement)
    noteElement.hidden = false
  if (buttonElement)
    buttonElement.classList.add("feedback-received")
}

window.addEventListener("DOMContentLoaded", () => {
  const feedback = document.forms.feedback
  if (typeof feedback === "undefined") return

  feedback.hidden = false

  const rating = new PageRating(feedback.dataset)

  if (rating.exists && typeof rating.value !== "undefined") {
    disableWith(feedback, rating.value.toString())
  }

  feedback.addEventListener("submit", event => {
    event.preventDefault()

    const submittedValue = event.submitter.dataset.mdValue

    rating.give(
      Number.parseInt(submittedValue)
    )

    disableWith(feedback, submittedValue)
  })
})
