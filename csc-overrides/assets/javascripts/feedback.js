const RatingStorage = class {
  static #disabled
  static #storage = window.localStorage
  static #key = "pageRatings"
  static {
    try {
      if (!this.#storage.getItem(this.#key)) {
        this.#storage.setItem(this.#key, JSON.stringify({}))
      }
    } catch(exception) {
      console.error(exception)
      this.#disabled = true
    }
    this.#disabled = false
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
    } catch(exception) {
      console.error(exception)
      this.#disabled = true
    }
  }
}

const PageRating = class {
  #storage
  #sourcePath
  #sourceEditDate
  #announcementTarget
  static #values = { "positive": 1, "negative": -1 }
  static #itemKey = window.location.pathname
  constructor(announcementTarget, page) {
    this.#storage = RatingStorage
    this.#sourcePath = page.sourcePath
    this.#sourceEditDate = Date.parse(page.sourceEdited)
    this.#announcementTarget = announcementTarget
    this.#validateRating()
  }
  get #current() {
    const ratings = this.#storage.getRatings()
    return ratings[PageRating.#itemKey]
  }
  get #value() {
    const rating = this.#current
    const type = rating.type.toLowerCase()
    return Object.keys(PageRating.#values).includes(type)
      ? PageRating.#values[type]
      : null
  }
  get #exists() {
    return this.#current && this.#value
  }
  get #outdated() {
    return this.#current.date < this.#sourceEditDate ||
           this.#current.source !== this.#sourcePath
  }
  #validateRating() {
    if (this.#exists) {
      if (this.#outdated) {
        this.#removeRating()
      } else {
        this.#announceRating()
      }
    }
  }
  #removeRating() {
    const ratings = this.#storage.getRatings()
    delete ratings[PageRating.#itemKey]
  }
  #newRating(type) {
    return ({ date: Date.now(), source: this.#sourcePath, type })
  }
  #announceRating() {
    if (this.#current) {
      const ratingEvent = new CustomEvent("rated", {
        detail: {
           rating: this.#current.type,
        },
      })
      this.#announcementTarget.dispatchEvent(ratingEvent)
    }
  }
  #trackRating() {
    const rating = this.#current
    const value = this.#value
    if (rating && value) {
      const category = "Page Feedback"
      const action = `${rating.type} Rating`
      const name = this.#sourcePath
      const feedbackEvent = [ "trackEvent", category, action, name, value ]
      window._paq && window._paq.push(feedbackEvent)
    }
  }
  give(type) {
    const ratings = this.#storage.getRatings()
    ratings[PageRating.#itemKey] = this.#newRating(type)
    this.#storage.setRatings(ratings)
    this.#announceRating()
    if (!this.#storage.disabled) this.#trackRating()
  }
}

const FormState = class extends EventTarget {
  #targetForm
  constructor(form) {
    super()
    this.#targetForm = form
  }
  static #formContentClassName = "csc-feedback-content"
  static #submittedFormClassNames(rating) {
    const base = "csc-rated"
    return [base, `${base}--${rating.toLowerCase()}`]
  }
  #setFormState(rating) {
    const selector = `.${FormState.#formContentClassName}`
    const contentElement = this.#targetForm.querySelector(selector)
    contentElement.classList.add(...FormState.#submittedFormClassNames(rating))
  }
  handleRatingEvent(event) {
    const rating = event.detail.rating
    this.#setFormState(rating)
  }
}

const FeedbackForm = class {
  static #rating
  static #handleSubmitEvent(event) {
    event.preventDefault()
    const rating = event.submitter.value
    FeedbackForm.#rating.give(rating)
  }
  static init(formElement) {
    if (formElement) {
      const ratingTarget = new FormState(formElement)
      ratingTarget.addEventListener("rated", ratingTarget.handleRatingEvent)
      FeedbackForm.#rating = new PageRating(ratingTarget, formElement.dataset)
      formElement.addEventListener("submit", FeedbackForm.#handleSubmitEvent)
    }
  }
}

window.addEventListener("load", () => FeedbackForm.init(document.forms.feedback))
